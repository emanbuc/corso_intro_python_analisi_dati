# Esempio realistico — Le presenze turistiche a Milano nel 2023

[![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/emanbuc/corso_intro_python_analisi_dati/blob/main/docs/esempi/turismo-milano.ipynb) · [Scarica il notebook](turismo-milano.ipynb)

Questo esempio percorre un'analisi completa, dalla domanda alle conclusioni, su **dati
aperti reali**: le presenze turistiche mensili a Milano per regione italiana di provenienza,
pubblicate dal Comune di Milano
([«Turismo: presenze mensili per regioni»](https://dati.comune.milano.it/dataset/ds370-turismotempolibero-presenze-regione-mese),
licenza CC BY 4.0). Il file è usato così come viene pubblicato, senza ritocchi: i problemi
che incontreremo sono quelli veri.

È lo schema da seguire nel [mini-progetto finale](../esercitazioni/04-mini-progetto.md):
domanda → caricamento → pulizia → analisi → due grafici → conclusioni.

## 1. Le domande

Prima di aprire il file scriviamo che cosa vogliamo sapere:

1. Come si distribuiscono le presenze nei mesi dell'anno?
2. Da quali regioni proviene la quota maggiore di presenze?
3. Il calo estivo riguarda tutte le regioni allo stesso modo?

## 2. Caricamento

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

URL_DATI = "https://raw.githubusercontent.com/emanbuc/corso_intro_python_analisi_dati/main/docs/dati/"
percorso = URL_DATI + "ds370_presenze_mensili_regioni_2023.csv"

grezzo = pd.read_csv(percorso)
print(grezzo.shape)
grezzo.head(3)
```

Qualcosa non va: la tabella ha **una sola colonna**, il cui nome contiene dei punti e
virgola. Il file usa `;` come separatore al posto della virgola, cosa frequente nei CSV
prodotti in Italia. Lo indichiamo con `sep`.

```python
presenze = pd.read_csv(percorso, sep=";")
print(presenze.shape)
presenze.head()
```

```python
presenze.info()
```

Ora le colonne sono quattro e le righe 252. Il conto torna: 21 voci (19 regioni più le
province autonome di Bolzano e Trento) per 12 mesi. `info` dice anche che non ci sono
valori mancanti e che `anno` e `Presenze` sono numeri interi.

## 3. Pulizia

Il file è ordinato, ma tre cose vanno sistemate prima di analizzarlo.

**Nomi delle colonne.** La prima colonna si chiama `Paese di provenienza` ma contiene
regioni; i nomi mescolano maiuscole e spazi. Li rinominiamo in modo breve e coerente.

```python
presenze = presenze.rename(columns={
    "Paese di provenienza": "regione",
    "Presenze": "presenze",
})
print(presenze.columns.tolist())
```

**Testo.** I nomi delle regioni sono tutti in maiuscolo. Controlliamo che non ci siano
varianti dello stesso nome (spazi, errori di battitura), poi li rendiamo più leggibili per
i grafici.

```python
print(presenze["regione"].nunique())
print(sorted(presenze["regione"].unique()))

presenze["regione"] = presenze["regione"].str.strip().str.title()
print(presenze["regione"].unique()[:5])
```

`title` mette in maiuscolo l'iniziale di ogni parola, quindi scrive «Valle D'Aosta»: un
difetto estetico che qui accettiamo, perché non cambia i risultati.

**Mesi.** Il mese è testo abbreviato in italiano (`Gen`, `Feb`…). Come testo si ordinerebbe
in ordine alfabetico (`Ago`, `Apr`, `Dic`…), che per una serie temporale è sbagliato. Lo
traduciamo in numero e costruiamo una vera data, fissata al primo giorno del mese.

```python
print(presenze["mese"].unique())

numero_mese = {"Gen": 1, "Feb": 2, "Mar": 3, "Apr": 4, "Mag": 5, "Giu": 6,
               "Lug": 7, "Ago": 8, "Set": 9, "Ott": 10, "Nov": 11, "Dic": 12}

presenze["mese_num"] = presenze["mese"].map(numero_mese)
print(presenze["mese_num"].isna().sum())      # 0: tutte le abbreviazioni sono state riconosciute

presenze["data"] = pd.to_datetime(
    {"year": presenze["anno"], "month": presenze["mese_num"], "day": 1}
)
presenze.head(3)
```

**Controlli di qualità.** Prima di fidarci dei numeri verifichiamo che non ci siano righe
duplicate, che ogni regione abbia esattamente 12 mesi e che i valori siano plausibili.

```python
print("Righe duplicate:", presenze.duplicated().sum())
print("Mesi per regione:", presenze.groupby("regione")["mese"].count().unique())
print(presenze["presenze"].describe().round(0))
```

Nessun duplicato, 12 mesi per ogni regione, nessun valore negativo o nullo. La tabella è
pronta. Notate che il file originale non è stato toccato: ogni correzione è una riga di
codice, quindi è documentata e ripetibile.

## 4. Analisi

### Domanda 1 — Come si distribuiscono le presenze nei mesi?

```python
totale = presenze["presenze"].sum()
print(f"Presenze totali nel 2023: {totale:,}".replace(",", "."))

per_mese = presenze.groupby("data")["presenze"].sum().reset_index()
per_mese["quota_pct"] = (per_mese["presenze"] / totale * 100).round(1)
per_mese
```

```python
fig, ax = plt.subplots(figsize=(8, 4))
sns.lineplot(data=per_mese, x="data", y="presenze", marker="o", ax=ax)
ax.set(
    title="Presenze turistiche a Milano dalle regioni italiane, 2023",
    xlabel="Mese",
    ylabel="Presenze",
)
ax.set_ylim(0, None)
ax.set_xticks(per_mese["data"])
ax.set_xticklabels(per_mese["data"].dt.strftime("%m/%y"))
fig.tight_layout()
fig.savefig("presenze_per_mese.png", dpi=150)
plt.show()
```

Nel 2023 il dataset conta circa 3,86 milioni di presenze. Per undici mesi su dodici il
valore mensile sta tra 295.000 e 390.000 circa, con il massimo a novembre (388.307, il
10,1% dell'anno). **Agosto è l'eccezione**: 121.085 presenze, il 3,1% del totale annuo.

L'asse verticale parte da zero di proposito: così la distanza tra agosto e gli altri mesi
è rappresentata nella sua proporzione reale.

### Domanda 2 — Da quali regioni proviene la quota maggiore?

```python
per_regione = (
    presenze.groupby("regione")["presenze"].sum()
    .sort_values(ascending=False)
    .reset_index()
)
per_regione["quota_pct"] = (per_regione["presenze"] / totale * 100).round(1)
per_regione.head(10)
```

```python
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=per_regione.head(10), x="presenze", y="regione", color="steelblue", ax=ax)
ax.set(
    title="Le 10 regioni con più presenze a Milano, 2023",
    xlabel="Presenze nell'anno",
    ylabel="Regione di provenienza",
)
fig.tight_layout()
fig.savefig("presenze_per_regione.png", dpi=150)
plt.show()
```

Il Lazio è la prima regione di provenienza (14,9% delle presenze), seguito dalla Lombardia
stessa (12,3%), da Campania (9,5%), Sicilia (8,7%) e Puglia (8,5%). Le barre sono
orizzontali perché i nomi delle regioni sono lunghi: così si leggono senza ruotare il testo.

### Domanda 3 — Il calo di agosto riguarda tutte le regioni allo stesso modo?

Per ogni regione confrontiamo le presenze di agosto con la media degli altri undici mesi.
Un rapporto di 0,30 significa che ad agosto quella regione fa il 30% del suo mese tipico.

```python
agosto = presenze[presenze["mese_num"] == 8].set_index("regione")["presenze"]
altri_mesi = presenze[presenze["mese_num"] != 8].groupby("regione")["presenze"].mean()

rapporto = (agosto / altri_mesi).sort_values(ascending=False).round(2)
print(rapporto.head(5))
print(rapporto.tail(5))
```

Il calo riguarda tutte le regioni: il rapporto va da 0,28 a 0,53. La Lombardia è quella
che cala meno (0,53); per quasi tutte le altre agosto vale tra il 28% e il 43% di un
mese tipico.

## 5. Conclusioni

- Le presenze a Milano provenienti dalle regioni italiane sono distribuite in modo
  abbastanza uniforme nell'anno, **tranne ad agosto**, quando scendono a circa un terzo
  di un mese normale.
- **Lazio e Lombardia** da sole valgono oltre un quarto delle presenze; seguono tre grandi
  regioni del Sud (Campania, Sicilia, Puglia).
- Il calo di agosto è generale, meno marcato per la Lombardia.

**Che cosa i dati non dicono.** I numeri descrivono *quanto* e *quando*, non *perché*:
attribuire l'andamento a turismo d'affari, fiere o ferie è un'ipotesi ragionevole che questi
dati da soli non possono confermare. Inoltre le regioni hanno popolazioni molto diverse:
per dire quale regione "viaggia di più verso Milano" servirebbe rapportare le presenze agli
abitanti, con una tabella aggiuntiva. Infine un solo anno non basta per parlare di tendenze:
il confronto con il 2024 è l'oggetto del mini-progetto.

---

[← Lezione 3](../lezioni/03-analisi-visualizzazione.md) · [Dataset](../dati.md) · [Mini-progetto finale →](../esercitazioni/04-mini-progetto.md)
