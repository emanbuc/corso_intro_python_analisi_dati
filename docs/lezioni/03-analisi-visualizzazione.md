# Lezione 3 — Analisi esplorativa, visualizzazione e mini-progetto

La terza lezione trasforma la tabella pulita in risposte: aggregazioni, grafici e
un'analisi completa svolta dall'inizio alla fine.

!!! abstract "Obiettivi"
    - Riassumere i dati con `value_counts`, `groupby`, `agg` e `pivot_table`.
    - Combinare tabelle con `merge` e `concat`, controllando le righe prima e dopo.
    - Scegliere e realizzare il grafico adatto alla domanda con Matplotlib e seaborn.
    - Svolgere un'analisi completa: dalla domanda alle conclusioni scritte.

**Esercitazione collegata:** [Esercitazione 3](../esercitazioni/03-analisi-visualizzazione.md) ·
**Esempio completo:** [Turismo a Milano](../esempi/turismo-milano.md) ·
**Verifica finale:** [Mini-progetto](../esercitazioni/04-mini-progetto.md)

## 1. Aggregazioni (40 min)

```python
import pandas as pd

URL_DATI = "https://raw.githubusercontent.com/emanbuc/corso_intro_python_analisi_dati/main/docs/dati/"
tips = pd.read_csv(URL_DATI + "tips.csv")
tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100
```

### `value_counts`

Conta quante volte compare ogni valore di una colonna: è il primo sguardo a una variabile categorica.

```python
print(tips["day"].value_counts())
print(tips["day"].value_counts(normalize=True).round(3))     # frequenze relative
```

### `groupby` con `agg`

`groupby` segue lo schema **dividi → applica → combina**: divide le righe in gruppi secondo
una o più colonne, applica una funzione a ciascun gruppo e combina i risultati in una nuova tabella.

```python
# Una statistica su una colonna
print(tips.groupby("day")["tip"].mean())

# Più statistiche sulla stessa colonna
print(tips.groupby("day")["tip"].agg(["count", "mean", "median", "max"]).round(2))

# Statistiche diverse su colonne diverse, con nomi scelti da noi
riepilogo = tips.groupby("time").agg(
    conti=("total_bill", "count"),
    incasso=("total_bill", "sum"),
    mancia_media_pct=("tip_pct", "mean"),
)
print(riepilogo.round(2))
```

Raggruppando per più colonne si ottiene una riga per ogni combinazione; `reset_index`
riporta le chiavi del gruppo tra le colonne normali.

```python
per_giorno_e_pasto = tips.groupby(["day", "time"])["total_bill"].mean().reset_index()
print(per_giorno_e_pasto.round(2))
```

### `pivot_table`

Una tabella pivot mette una variabile categorica sulle righe, una sulle colonne e una
statistica nelle celle: la stessa cosa del `groupby` su due colonne, ma in forma di
tabella a doppia entrata.

```python
pivot = tips.pivot_table(
    values="tip_pct", index="day", columns="time", aggfunc="mean"
)
print(pivot.round(1))
```

Le celle `NaN` indicano combinazioni che nei dati non esistono.

!!! warning "Errore tipico: aggregazioni su colonne con valori mancanti"
    `mean`, `sum` e le altre statistiche **ignorano** i valori mancanti senza avvisare, e
    `count` conta solo i valori presenti. Una media calcolata su 10 valori su 100 è poco
    affidabile anche se il numero sembra plausibile: affiancate sempre il conteggio alla
    statistica e confrontatelo con `size`, che conta tutte le righe del gruppo.

```python
import numpy as np

esempio = pd.DataFrame({"gruppo": ["a", "a", "a", "b"], "valore": [10, np.nan, np.nan, 4]})
print(esempio.groupby("gruppo")["valore"].agg(["size", "count", "mean"]))
```

## 2. Combinare tabelle (25 min)

### `merge` e tipi di join

`merge` affianca due tabelle usando una colonna in comune (la **chiave**), come il
CERCA.VERT di un foglio di calcolo. Arricchiamo `tips` con una tabella di anagrafica dei giorni.

```python
giorni = pd.read_csv(URL_DATI + "giorni.csv")
print(giorni)

arricchito = tips.merge(giorni, on="day", how="left")
print(arricchito[["total_bill", "day", "giorno", "fine_settimana"]].head(3))
```

Il parametro `how` decide quali righe tenere:

| `how` | Righe nel risultato |
|---|---|
| `"inner"` (predefinito) | solo le chiavi presenti in **entrambe** le tabelle |
| `"left"` | tutte le righe della tabella di sinistra; dove manca la corrispondenza, `NaN` |
| `"right"` | tutte le righe della tabella di destra |
| `"outer"` | tutte le righe di entrambe |

Per arricchire una tabella principale si usa quasi sempre `how="left"`: nessuna riga va
persa, e le chiavi senza corrispondenza si riconoscono dai `NaN`.

### Controllare le righe prima e dopo

```python
print(len(tips), len(arricchito))                 # devono coincidere
print(arricchito["giorno"].isna().sum())          # chiavi senza corrispondenza: 0
```

!!! warning "Errore tipico: join che moltiplicano le righe"
    Se nella tabella di anagrafica una chiave compare **più volte**, ogni riga
    corrispondente della tabella principale viene duplicata, e somme e conteggi risultano
    gonfiati. Controllate sempre il numero di righe prima e dopo.

```python
anagrafica_sbagliata = pd.concat([giorni, giorni.iloc[[0]]])      # "Thur" compare due volte
gonfiato = tips.merge(anagrafica_sbagliata, on="day", how="left")
print(len(tips), len(gonfiato))                                   # le righe sono aumentate

# validate fa fallire il merge se la chiave non è unica nella tabella di destra
try:
    tips.merge(anagrafica_sbagliata, on="day", how="left", validate="many_to_one")
except pd.errors.MergeError as errore:
    print("Merge rifiutato:", errore)
```

### `concat`

`concat` impila tabelle con le stesse colonne una sotto l'altra: serve, ad esempio, per
unire file dello stesso tipo relativi a periodi diversi.

```python
pranzi = tips[tips["time"] == "Lunch"]
cene = tips[tips["time"] == "Dinner"]
tutti = pd.concat([pranzi, cene], ignore_index=True)       # ignore_index: rinumera le righe
print(len(pranzi), len(cene), len(tutti))
```

## 3. Visualizzazione (50 min)

### Matplotlib: figura e assi

In Matplotlib una **figura** (`fig`) è il foglio, gli **assi** (`ax`) sono il riquadro in
cui si disegna. Si creano insieme con `plt.subplots`, poi si lavora sull'oggetto `ax`.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 4))
ax.scatter(tips["total_bill"], tips["tip"], alpha=0.6)
ax.set_title("Mancia e importo del conto")
ax.set_xlabel("Conto ($)")
ax.set_ylabel("Mancia ($)")
plt.show()
```

### Grafici da pandas

Series e DataFrame hanno un metodo `plot` che usa Matplotlib: comodo per un grafico
veloce a partire da una tabella aggregata.

```python
incasso = tips.groupby("day")["total_bill"].sum().loc[["Thur", "Fri", "Sat", "Sun"]]

fig, ax = plt.subplots(figsize=(6, 4))
incasso.plot(kind="bar", ax=ax)
ax.set_title("Incasso totale per giorno")
ax.set_xlabel("Giorno")
ax.set_ylabel("Incasso ($)")
plt.show()
```

### seaborn

seaborn lavora direttamente sui DataFrame: si indica la tabella (`data`) e quali colonne
usare per gli assi e per il colore (`hue`). Ogni funzione restituisce gli assi di Matplotlib,
su cui si impostano titoli ed etichette.

```python
import seaborn as sns

sns.set_theme(style="whitegrid")
ordine = ["Thur", "Fri", "Sat", "Sun"]
```

**Istogramma** — com'è distribuita una variabile numerica?

```python
ax = sns.histplot(data=tips, x="total_bill", bins=20)
ax.set(title="Distribuzione dell'importo dei conti", xlabel="Conto ($)", ylabel="Numero di conti")
plt.show()
```

**Boxplot** — come cambia la distribuzione tra gruppi? La scatola copre dal primo al terzo
quartile, la linea interna è la mediana, i punti isolati sono valori anomali.

```python
ax = sns.boxplot(data=tips, x="day", y="total_bill", order=ordine)
ax.set(title="Importo dei conti per giorno", xlabel="Giorno", ylabel="Conto ($)")
plt.show()
```

**Scatter** — che relazione c'è tra due variabili numeriche?

```python
ax = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
ax.set(title="Mancia e importo del conto", xlabel="Conto ($)", ylabel="Mancia ($)")
plt.show()
```

**Barre** — come si confronta una statistica tra categorie? `barplot` calcola la media di
ogni gruppo; il segmento nero è l'intervallo di confidenza della media.

```python
ax = sns.barplot(data=tips, x="day", y="tip_pct", order=ordine)
ax.set(title="Mancia media per giorno", xlabel="Giorno", ylabel="Mancia (% del conto)")
plt.show()
```

**Linee** — come varia una grandezza lungo una dimensione ordinata (tipicamente il tempo)?

```python
per_dimensione = tips.groupby("size")["total_bill"].mean().reset_index()
ax = sns.lineplot(data=per_dimensione, x="size", y="total_bill", marker="o")
ax.set(title="Conto medio per numero di persone", xlabel="Persone al tavolo", ylabel="Conto medio ($)")
plt.show()
```

### Quale grafico per quale domanda

| Domanda | Grafico |
|---|---|
| Come è distribuita una variabile numerica? | Istogramma |
| La distribuzione cambia tra gruppi? | Boxplot |
| Due variabili numeriche sono legate? | Scatter |
| Quanto vale una statistica in ogni categoria? | Barre |
| Come evolve una grandezza nel tempo? | Linee |

### Titoli, etichette, salvataggio

Un grafico deve potersi leggere da solo: titolo che dice che cosa mostra, etichette degli
assi con le unità di misura, legenda quando ci sono più serie.

```python
fig, ax = plt.subplots(figsize=(7, 4))
sns.barplot(data=tips, x="day", y="tip_pct", order=ordine, ax=ax)
ax.set(title="Mancia media per giorno", xlabel="Giorno", ylabel="Mancia (% del conto)")
ax.set_ylim(0, None)                       # l'asse delle barre parte da zero
fig.tight_layout()
fig.savefig("mancia_per_giorno.png", dpi=150)
plt.show()
```

!!! warning "Errore tipico: grafici senza etichette o con scala fuorviante"
    Un grafico a barre il cui asse non parte da zero ingrandisce differenze piccole fino a
    farle sembrare enormi. Controllate sempre da dove parte l'asse e che titolo ed
    etichette dicano che cosa si sta guardando.

## 4. Mini-progetto guidato (50 min)

Un'analisi completa segue sempre gli stessi passi:

1. **Domanda** — che cosa vogliamo sapere? Scriverla prima di toccare i dati.
2. **Caricamento** — leggere il file e verificare che sia stato letto bene.
3. **Pulizia** — sistemare tipi, testo, date, duplicati e valori mancanti, motivando le scelte.
4. **Analisi** — filtri, aggregazioni, eventuali join.
5. **Due grafici** — scelti in funzione delle domande.
6. **Conclusioni scritte** — che cosa dicono i dati, e che cosa *non* possono dire.

L'[esempio realistico](../esempi/turismo-milano.md) percorre tutti e sei i passi su dati
aperti del Comune di Milano. In aula si lavora poi, individualmente o a coppie, sul
[mini-progetto](../esercitazioni/04-mini-progetto.md), che è anche la verifica finale.

## 5. Chiusura: buone pratiche (15 min)

- **Notebook riproducibile**: *Riavvia ed esegui tutto* deve funzionare dall'inizio alla
  fine; i dati si leggono da un percorso o indirizzo dichiarato in cima.
- **Nomi chiari**: `presenze_per_mese` si capisce, `df2` no.
- **Celle Markdown**: una frase prima di ogni blocco per dire che cosa si fa e perché, una
  dopo ogni risultato per dire che cosa se ne ricava.
- **Dati originali intatti**: non si modifica mai il file di partenza; le correzioni si
  fanno nel codice, così restano documentate.

**Prossimi passi.** Le [risorse](../risorse.md) indicano dove proseguire: la guida di
pandas per i casi non visti a lezione, il tutorial di seaborn per gli altri tipi di grafico.

## Errori tipici da anticipare

| Errore | Come si manifesta | Rimedio |
|---|---|---|
| Aggregazioni con valori mancanti | Statistiche calcolate su pochi valori, senza avvisi | Affiancare `count` e `size` alla statistica |
| Join che moltiplicano le righe | Più righe dopo il `merge`, totali gonfiati | Confrontare `len` prima e dopo; `validate="many_to_one"` |
| Grafici senza etichette o con scala fuorviante | Grafico illeggibile o ingannevole | Titolo, etichette con unità, asse delle barre da zero |

## Risultato atteso e consegna

Un notebook di analisi completo, leggibile da una persona che non ha seguito il corso. Il
notebook del [mini-progetto](../esercitazioni/04-mini-progetto.md), completato entro una
settimana, è la verifica finale.

## Riferimenti

- [Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html) e
  [Merge, join, concatenate](https://pandas.pydata.org/docs/user_guide/merging.html) nella guida di pandas.
- [Tutorial di seaborn](https://seaborn.pydata.org/tutorial.html).
- [Python for Data Analysis, 3ª edizione](https://wesmckinney.com/book/), capitoli 8–10.

---

[← Lezione 2](02-numpy-pandas.md) · [Programma](../programma.md) · [Esercitazione 3 →](../esercitazioni/03-analisi-visualizzazione.md) · [Esempio realistico →](../esempi/turismo-milano.md)
