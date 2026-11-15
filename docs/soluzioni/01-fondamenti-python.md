# Soluzioni — Esercitazione 1

[![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/emanbuc/corso_intro_python_analisi_dati/blob/main/docs/soluzioni/01-fondamenti-python/soluzione-01.ipynb) · [Scarica il notebook](01-fondamenti-python/soluzione-01.ipynb)

!!! warning "Prima provate da soli"
    Questa pagina contiene le soluzioni complete dell'[esercitazione 1](../esercitazioni/01-fondamenti-python.md).

Le soluzioni proposte non sono le uniche corrette: conta che il risultato sia giusto e che
il codice si legga bene.

## B. Calcoli su valori singoli

```python
# B1
conto = 48.27
mancia = 6.73
percentuale = round(mancia / conto * 100, 1)
print(percentuale)

# B2
vendite_prima = 1250
vendite_dopo = 1410
variazione = (vendite_dopo - vendite_prima) / vendite_prima * 100
print(variazione)

# B3
prezzo_testo = "19.90"
quantita_testo = "3"
totale = float(prezzo_testo) * int(quantita_testo)
print(f"Totale: {totale:.2f} euro")
```

In B2 la variazione si calcola sempre rispetto al valore di partenza. In B3 il prezzo va
convertito con `float` e la quantità con `int`: moltiplicare la stringa `"19.90"` per 3
ripeterebbe il testo tre volte.

## C. Un piccolo dataset come lista di dizionari

```python
dataset = [
    {"total_bill": 16.99, "tip": 1.01, "day": "Sun", "size": 2},
    {"total_bill": 10.34, "tip": 1.66, "day": "Sun", "size": 3},
    {"total_bill": 21.01, "tip": 3.50, "day": "Sun", "size": 3},
    {"total_bill": 23.68, "tip": 3.31, "day": "Sun", "size": 2},
    {"total_bill": 24.59, "tip": 3.61, "day": "Sun", "size": 4},
    {"total_bill": 25.29, "tip": 4.71, "day": "Sun", "size": 4},
]

# C1: la terza riga ha indice 2
print(len(dataset), dataset[2]["tip"])

# C2
conti = [riga["total_bill"] for riga in dataset]
print(conti, round(sum(conti), 2))

# C3
tavoli_grandi = [riga for riga in dataset if riga["size"] >= 3]
print(len(tavoli_grandi))

# C4
for riga in dataset:
    riga["tip_pct"] = round(riga["tip"] / riga["total_bill"] * 100, 1)
print(dataset[0])
```

## D. Una funzione

```python
def media_e_massimo(valori):
    """Restituisce media e massimo di una lista di numeri."""
    media = sum(valori) / len(valori)
    return media, max(valori)

print(media_e_massimo([1.01, 1.66, 3.35, 4.00]))
print(media_e_massimo([10]))
```

## E. Media per categoria "a mano"

```python
import csv
import urllib.request

URL_DATI = "https://raw.githubusercontent.com/emanbuc/corso_intro_python_analisi_dati/main/docs/dati/"
urllib.request.urlretrieve(URL_DATI + "tips.csv", "tips.csv")

with open("tips.csv", newline="") as f:
    righe = list(csv.DictReader(f))

somme = {}
conteggi = {}

for riga in righe:
    pasto = riga["time"]
    importo = float(riga["total_bill"])
    if pasto not in somme:
        somme[pasto] = 0
        conteggi[pasto] = 0
    somme[pasto] = somme[pasto] + importo
    conteggi[pasto] = conteggi[pasto] + 1

for pasto in somme:
    print(f"{pasto}: {somme[pasto] / conteggi[pasto]:.2f} (su {conteggi[pasto]} conti)")
```

Il conto medio è di circa 20,80 $ a cena (176 conti) e 17,17 $ a pranzo (68 conti).

## Esercizi per casa

```python
# H1
temperature = [18.5, 21.0, 19.2, 24.8, 26.1, 22.3, 17.9]
media = sum(temperature) / len(temperature)
sopra_media = [t for t in temperature if t > media]
print(round(media, 2), sopra_media, len(sopra_media))

# H2
magazzino = {"penne": 40, "quaderni": 25, "matite": 60}
magazzino["penne"] = magazzino["penne"] + 5
magazzino["evidenziatori"] = 12
print(magazzino, sum(magazzino.values()))

# H3
ordini = [
    {"prodotto": "caffè", "prezzo": 1.20, "quantita": 85},
    {"prodotto": "cornetto", "prezzo": 1.50, "quantita": 60},
    {"prodotto": "spremuta", "prezzo": 3.50, "quantita": 22},
]
incasso_totale = 0
migliore = None
incasso_migliore = 0
for ordine in ordini:
    incasso = ordine["prezzo"] * ordine["quantita"]
    incasso_totale = incasso_totale + incasso
    if incasso > incasso_migliore:
        incasso_migliore = incasso
        migliore = ordine["prodotto"]
print(round(incasso_totale, 2), migliore)
```

```python
# H4
def conta_occorrenze(valori):
    """Restituisce un dizionario valore -> numero di occorrenze."""
    conteggi = {}
    for valore in valori:
        conteggi[valore] = conteggi.get(valore, 0) + 1
    return conteggi

print(conta_occorrenze(["Sun", "Sat", "Sun", "Thur", "Sat", "Sun"]))
```

In H4 `conteggi.get(valore, 0)` restituisce 0 la prima volta che si incontra un valore:
evita l'`if` usato nell'esercizio E. È esattamente ciò che in pandas fa `value_counts`.

---

[← Esercitazione 1](../esercitazioni/01-fondamenti-python.md) · [Lezione 1](../lezioni/01-fondamenti-python.md) · [Programma](../programma.md)
