# Soluzioni — Esercitazione 3

[![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/emanbuc/corso_intro_python_analisi_dati/blob/main/docs/soluzioni/03-analisi-visualizzazione/soluzione-03.ipynb) · [Scarica il notebook](03-analisi-visualizzazione/soluzione-03.ipynb)

!!! warning "Prima provate da soli"
    Questa pagina contiene le soluzioni complete dell'[esercitazione 3](../esercitazioni/03-analisi-visualizzazione.md).

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

URL_DATI = "https://raw.githubusercontent.com/emanbuc/corso_intro_python_analisi_dati/main/docs/dati/"
tips = pd.read_csv(URL_DATI + "tips.csv")
tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100
ordine = ["Thur", "Fri", "Sat", "Sun"]
```

## A. Aggregazioni

```python
# A1
print(tips["day"].value_counts())
print((tips["day"].value_counts(normalize=True) * 100).round(1))

# A2
per_giorno = tips.groupby("day").agg(
    conti=("total_bill", "count"),
    incasso=("total_bill", "sum"),
    mancia_media_pct=("tip_pct", "mean"),
).loc[ordine]
print(per_giorno.round(2))
```

```python
# A3
media = tips.pivot_table(values="tip_pct", index="day", columns="smoker", aggfunc="mean").loc[ordine]
numero = tips.pivot_table(values="tip_pct", index="day", columns="smoker", aggfunc="count").loc[ordine]
print(media.round(1))
print(numero)
```

Sabato e domenica raccolgono quasi due terzi dei conti (87 e 76 su 244); il venerdì ne ha
solo 19. La tabella dei conteggi è quella che dice quanto fidarsi delle medie: la cella
"venerdì, non fumatori" si basa su 4 conti soltanto, quindi la sua media va presa con
molta cautela. Le medie per cella vanno da circa 15% a circa 19%, differenze piccole
rispetto alla variabilità dei singoli conti.

## B. Combinare tabelle

```python
giorni = pd.read_csv(URL_DATI + "giorni.csv")

# B1
arricchito = tips.merge(giorni, on="day", how="left", validate="many_to_one")
print(len(tips), len(arricchito))
print(arricchito["giorno"].isna().sum())

# B2
confronto = arricchito.groupby("fine_settimana").agg(
    conti=("total_bill", "count"),
    conto_medio=("total_bill", "mean"),
    persone_medie=("size", "mean"),
)
print(confronto.round(2))
```

Le righe sono 244 prima e dopo, e nessun giorno è rimasto senza corrispondenza: il `merge`
ha solo aggiunto colonne. Nel fine settimana i conti sono di più (163 contro 81), più alti
in media (20,89 $ contro 17,56 $) e con tavoli un po' più numerosi.

## C. Quattro domande, quattro grafici

```python
# C1: distribuzione di una variabile numerica -> istogramma
ax = sns.histplot(data=tips, x="tip_pct", bins=30)
ax.set(title="Distribuzione della mancia", xlabel="Mancia (% del conto)", ylabel="Numero di conti")
plt.show()
```

La maggior parte delle mance sta tra il 10% e il 20% del conto, con pochi valori molto più
alti (fino al 71%) che allungano la coda a destra.

```python
# C2: confronto di una distribuzione tra gruppi -> boxplot
ax = sns.boxplot(data=tips, x="time", y="total_bill", order=["Lunch", "Dinner"])
ax.set(title="Importo dei conti per pasto", xlabel="Pasto", ylabel="Conto ($)")
plt.show()

print(tips.groupby("time")["total_bill"].median())
```

A cena i conti sono più alti e più dispersi: la mediana è circa 18,4 $ contro circa 16,0 $ a pranzo,
e 8 dei 10 conti sopra i 40 $ sono a cena.

```python
# C3: relazione tra due variabili numeriche -> scatter, con il colore per il gruppo
ax = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="smoker", alpha=0.7)
ax.set(title="Mancia e importo del conto", xlabel="Conto ($)", ylabel="Mancia ($)")
plt.show()

print(tips.groupby("smoker")[["total_bill", "tip"]].corr().round(2))
```

La mancia cresce con il conto. Per i tavoli senza fumatori i punti sono più allineati
(correlazione 0,82) che per quelli con fumatori (0,49), dove la mancia è meno prevedibile
a partire dal conto.

```python
# C4: una statistica per categoria -> barre, a partire da una tabella aggregata
incasso = tips.groupby("day")["total_bill"].sum().loc[ordine].reset_index()

fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(data=incasso, x="day", y="total_bill", color="steelblue", ax=ax)
ax.set(title="Incasso totale per giorno", xlabel="Giorno", ylabel="Incasso ($)")
ax.set_ylim(0, None)
fig.tight_layout()

# C5
fig.savefig("incasso_per_giorno.png", dpi=150)
plt.show()
print(incasso.round(2))
```

Il sabato è il giorno con l'incasso più alto (1.778,40 $), seguito dalla domenica
(1.627,16 $); il venerdì è di gran lunga il più basso (325,88 $), ma con soli 19 conti.
L'incasso totale dipende sia dal numero di conti sia dal loro importo: per confrontare i
giorni "a parità di conti" si guarda il conto medio.

---

[← Esercitazione 3](../esercitazioni/03-analisi-visualizzazione.md) · [Lezione 3](../lezioni/03-analisi-visualizzazione.md) · [Programma](../programma.md)
