# Soluzioni — Esercitazione 2

[![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/emanbuc/corso_intro_python_analisi_dati/blob/main/docs/soluzioni/02-numpy-pandas/soluzione-02.ipynb) · [Scarica il notebook](02-numpy-pandas/soluzione-02.ipynb)

!!! warning "Prima provate da soli"
    Questa pagina contiene le soluzioni complete dell'[esercitazione 2](../esercitazioni/02-numpy-pandas.md).

```python
import numpy as np
import pandas as pd

URL_DATI = "https://raw.githubusercontent.com/emanbuc/corso_intro_python_analisi_dati/main/docs/dati/"
tips = pd.read_csv(URL_DATI + "tips.csv")
```

## A. Ciclo `for` contro array

```python
lista_conti = tips["total_bill"].head(8).tolist()
lista_persone = tips["size"].head(8).tolist()

# A1
a_testa = []
for i in range(len(lista_conti)):
    a_testa.append(lista_conti[i] / lista_persone[i])
print(a_testa)

# A2
conti = np.array(lista_conti)
persone = np.array(lista_persone)
a_testa = conti / persone
print(a_testa.round(2))
print(a_testa.mean().round(2), a_testa.min().round(2), a_testa.max().round(2))
```

## B. Descrivere la struttura del dataset

```python
print(tips.shape)
print(tips.dtypes)
tips.info()
print(tips.describe().round(2))
```

`tips` ha 244 righe e 7 colonne. Le colonne numeriche sono `total_bill`, `tip` e `size`; le
altre quattro (`sex`, `smoker`, `day`, `time`) sono testo. Il conto medio è 19,79 $ e il
tavolo più numeroso ha 6 persone. Non ci sono valori mancanti.

## C. Cinque domande con filtri e ordinamenti

```python
# C1
print((tips["total_bill"] > 30).sum())

# C2
print(len(tips[(tips["time"] == "Lunch") & (tips["day"] == "Fri")]))

# C3
print(tips.sort_values("total_bill", ascending=False).head(1))

# C4
tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100
print(tips.sort_values("tip_pct", ascending=False)[["total_bill", "tip", "tip_pct"]].head(5).round(2))

# C5
grandi = tips[tips["size"] >= 5]
print(len(grandi), len(grandi[grandi["day"].isin(["Sat", "Sun"])]))
```

- **C1.** 32 conti superano i 30 $.
- **C2.** 7 conti a pranzo di venerdì.
- **C3.** Il conto più alto è 50,81 $, pagato a cena di sabato.
- **C4.** La percentuale più alta è il 71,0% (mancia di 5,15 $ su un conto di 7,25 $).
- **C5.** I tavoli da 5 o più persone sono 9, di cui 5 nel fine settimana.

In C1 la somma di una maschera booleana conta i `True`. In C4 la percentuale più alta
nasce da un conto molto piccolo: prima di trarre conclusioni conviene sempre guardare le
righe estreme.

## D. Ripulire la versione "sporca"

```python
# D1
sporco = pd.read_csv(URL_DATI + "tips_sporco.csv", sep=";")
print(sporco.shape)
sporco.info()
print(sporco.head())
```

Problemi visibili: 250 righe invece di 244 (possibili duplicati); `total_bill` e `tip` letti
come testo perché usano la virgola decimale; `data` è testo; `tip`, `sex` e `time` hanno
valori mancanti. Guardando i valori distinti si scopre anche che `day` e `sex` sono scritti
in modi diversi.

```python
# D2
print(sporco.duplicated().sum())
sporco = sporco.drop_duplicates()

# D3
sporco["total_bill"] = sporco["total_bill"].str.replace(",", ".").astype(float)
sporco["tip"] = sporco["tip"].str.replace(",", ".").astype(float)

# D4
print(sporco["day"].unique())
sporco["day"] = sporco["day"].str.strip().str.capitalize()
sporco["sex"] = sporco["sex"].str.strip().str.capitalize()
print(sporco["day"].unique(), sporco["sex"].unique())

# D5
sporco["data"] = pd.to_datetime(sporco["data"], format="%d/%m/%Y")
print(sporco["data"].min(), sporco["data"].max())
```

```python
# D6
print(sporco.isna().sum())

pulito = sporco.dropna(subset=["tip"])
pulito = pulito.fillna({"sex": "Non indicato", "time": "Non indicato"})
print(pulito.isna().sum().sum(), pulito.shape)
```

**Scelta proposta per D6.** Mancano 10 mance, 6 valori di `sex` e 5 di `time`. La mancia è
la grandezza che vogliamo analizzare: inventarla (con zero o con la media) altererebbe i
risultati, quindi le 10 righe senza mancia si eliminano. `sex` e `time` sono categorie:
si conserva la riga e si dichiara l'assenza con il valore `Non indicato`. Altre scelte sono
accettabili, purché motivate: ad esempio tenere anche le righe senza mancia se l'analisi
riguarda solo l'importo dei conti.

```python
# D7
pulito.to_csv("tips_pulito.csv", index=False)
riletto = pd.read_csv("tips_pulito.csv", parse_dates=["data"])
print(riletto.shape)
print(riletto.dtypes)
```

Il CSV non conserva i tipi: senza `parse_dates` la colonna `data` tornerebbe a essere testo.

## E. La media per categoria, con pandas

```python
print(tips.groupby("time")["total_bill"].agg(["mean", "count"]).round(2))
```

Gli stessi numeri ottenuti a mano nella lezione 1 (20,80 $ a cena su 176 conti, 17,17 $ a
pranzo su 68), in una riga e senza conversioni manuali.

## Esercizi per casa — Pulizia di un secondo dataset

```python
penguins = pd.read_csv(URL_DATI + "penguins_sporco.csv")
print(penguins.shape)
penguins.info()
print(penguins.head())
print(penguins["species"].unique())
```

Problemi individuati:

1. **Righe duplicate**: alcune righe compaiono due volte.
2. **Testo incoerente** in `species`: maiuscole, minuscole e spazi ai bordi producono 14
   valori distinti al posto di 3.
3. **Tipo errato** in `body_mass_g`: è testo perché contiene l'unità di misura (`3750 g`).
4. **Valori mancanti** nelle misure e in `sex`.

```python
# 1. Duplicati
print(penguins.duplicated().sum())
penguins = penguins.drop_duplicates()

# 2. Testo
penguins["species"] = penguins["species"].str.strip().str.capitalize()
print(penguins["species"].value_counts())

# 3. Tipo: si toglie l'unità e si converte in numero
penguins["body_mass_g"] = penguins["body_mass_g"].str.replace(" g", "").astype(float)

# 4. Valori mancanti
print(penguins.isna().sum())
penguins = penguins.dropna(subset=["bill_length_mm"])
print(penguins.isna().sum())

penguins.to_csv("penguins_pulito.csv", index=False)
print(penguins.shape)
```

**Motivazioni.** I duplicati si eliminano perché lo stesso animale conterebbe due volte.
Le due righe prive di tutte le misure non contengono informazione utile e si eliminano.
Le righe in cui manca solo `sex` si conservano con il valore mancante: le misure sono
valide, e `groupby("sex")` le escluderà automaticamente quando servirà.

---

[← Esercitazione 2](../esercitazioni/02-numpy-pandas.md) · [Lezione 2](../lezioni/02-numpy-pandas.md) · [Programma](../programma.md)
