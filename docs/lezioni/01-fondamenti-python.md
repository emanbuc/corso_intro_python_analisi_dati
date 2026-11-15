# Lezione 1 — Fondamenti di Python e ambiente di lavoro

La prima lezione dà il minimo di linguaggio necessario per leggere e scrivere codice di
analisi, e si chiude mostrando perché serve pandas.

!!! abstract "Obiettivi"
    - Aprire un notebook, eseguire celle di codice e scrivere celle Markdown.
    - Usare variabili, tipi di base, operatori e f-string per fare calcoli su valori singoli.
    - Rappresentare dati con liste, tuple, dizionari e set.
    - Scrivere condizioni, cicli e funzioni.
    - Leggere un file CSV con il modulo `csv` e riconoscere i limiti dell'approccio manuale.

**Esercitazione collegata:** [Esercitazione 1](../esercitazioni/01-fondamenti-python.md)

## 1. Ambiente e notebook (30 min)

### Perché Python per i dati

Chi lavora con i fogli di calcolo conosce già il problema: un'analisi fatta a colpi di
clic non lascia traccia dei passaggi e va rifatta da capo quando i dati cambiano. Con
Python l'analisi è un testo: si rilegge, si corregge, si riesegue su dati nuovi e si
condivide. Le librerie che useremo — NumPy, pandas, Matplotlib e seaborn — coprono
l'intero percorso dal file grezzo al grafico.

### Colab e Jupyter

Un **notebook** è un documento fatto di **celle**:

- le celle di **codice** contengono Python e, quando vengono eseguite, mostrano il risultato subito sotto;
- le celle **Markdown** contengono testo formattato: titoli, elenchi, spiegazioni.

[Google Colab](https://colab.research.google.com/) esegue i notebook nel browser senza
installare nulla; JupyterLab fa la stessa cosa sul proprio computer. In entrambi una cella
si esegue con ++shift+enter++.

### Kernel e ordine di esecuzione

Dietro il notebook lavora un **kernel**: il programma che esegue il codice e tiene in
memoria le variabili. Due conseguenze pratiche:

- il kernel ricorda ciò che è stato **eseguito**, non ciò che è scritto: conta l'ordine in
  cui avete eseguito le celle, non l'ordine in cui compaiono nella pagina;
- se il kernel viene riavviato, tutte le variabili spariscono e le celle vanno rieseguite dall'inizio.

!!! warning "Errore tipico: celle eseguite fuori ordine"
    Se una cella usa una variabile definita più in basso, o modificata da una cella eseguita
    due volte, il risultato dipende dalla storia della sessione. Il controllo da fare prima
    di consegnare un notebook è *Riavvia ed esegui tutto*: se funziona così, funziona per tutti.

## 2. Sintassi di base (45 min)

### Variabili e tipi

Una variabile è un nome a cui si assegna un valore con `=`. Il tipo non si dichiara: lo
decide il valore.

```python
prezzo = 16.99          # float: numero con la virgola
persone = 2             # int: numero intero
giorno = "Sun"          # str: testo
fumatore = False        # bool: True oppure False

print(prezzo, persone, giorno, fumatore)
print(type(prezzo), type(persone), type(giorno), type(fumatore))
```

`print` mostra uno o più valori; `type` dice di che tipo è un valore. In un notebook
l'ultima espressione di una cella viene mostrata anche senza `print`.

### Operatori

```python
conto = 16.99
mancia = 1.01

totale = conto + mancia
quota = totale / 2            # divisione: il risultato è sempre float
print(totale, quota)

print(7 // 2, 7 % 2)          # divisione intera e resto: 3 1
print(2 ** 10)                # potenza: 1024

print(conto > 10)             # confronto: True
print(conto > 10 and mancia > 2)   # and, or, not combinano valori booleani: False
```

!!! warning "Errore tipico: `=` e `==`"
    `=` **assegna** un valore a un nome; `==` **confronta** due valori e restituisce
    `True` o `False`. Scrivere `if giorno = "Sun":` è un errore di sintassi.

### Calcoli tipici: percentuali, variazioni, conversioni

```python
conto = 16.99
mancia = 1.01

percentuale_mancia = mancia / conto * 100
print(round(percentuale_mancia, 1))        # 5.9

vendite_ieri = 1200
vendite_oggi = 1380
variazione = (vendite_oggi - vendite_ieri) / vendite_ieri * 100
print(variazione)                          # 15.0

# Conversioni di tipo
print(int("42") + 1)        # da testo a intero: 43
print(float("3.5") * 2)     # da testo a decimale: 7.0
print(str(42) + " persone") # da numero a testo
```

### Stringhe e f-string

```python
nome = "  Mario Rossi "
print(nome.strip())             # toglie gli spazi ai bordi
print(nome.strip().upper())     # MARIO ROSSI
print(len(nome.strip()))        # numero di caratteri: 11
print("Rossi" in nome)          # True

conto = 16.99
mancia = 1.01
print(f"Conto: {conto} $, mancia: {mancia / conto:.1%}")
print(f"Totale: {conto + mancia:.2f} $")
```

Una **f-string** è una stringa preceduta da `f`: le espressioni tra parentesi graffe
vengono calcolate e inserite nel testo. Dopo i due punti si indica il formato: `.2f` per
due decimali, `.1%` per una percentuale con un decimale.

## 3. Strutture dati (45 min)

### Liste

Una lista è una sequenza ordinata e modificabile di valori.

```python
conti = [16.99, 10.34, 21.01, 23.68, 24.59]

print(conti[0])       # primo elemento: gli indici partono da 0
print(conti[-1])      # ultimo elemento
print(conti[1:3])     # slicing: dall'indice 1 incluso al 3 escluso -> [10.34, 21.01]
print(conti[:2])      # i primi due
print(len(conti), sum(conti), min(conti), max(conti))

conti.append(25.29)   # aggiunge in fondo
conti.sort()          # ordina la lista stessa
print(conti)
```

!!! warning "Errore tipico: gli indici partono da 0"
    In una lista di 5 elementi gli indici validi vanno da 0 a 4: `conti[5]` produce
    `IndexError: list index out of range`.

### Tuple

Una tupla è come una lista ma non si può modificare. Si usa per raggruppare pochi valori
che vanno insieme.

```python
punto = (45.46, 9.19)       # latitudine, longitudine
lat, lon = punto            # "spacchettamento" in due variabili
print(lat, lon)
```

### Dizionari

Un dizionario associa **chiavi** a **valori**: è il modo naturale di descrivere una riga
di una tabella.

```python
conto = {"total_bill": 16.99, "tip": 1.01, "day": "Sun", "size": 2}

print(conto["day"])                 # accesso per chiave
conto["time"] = "Dinner"            # aggiunge (o sostituisce) una chiave
print(conto.get("smoker", "n.d."))  # get: valore di riserva se la chiave manca
print(list(conto.keys()))
print(list(conto.values()))

for chiave, valore in conto.items():
    print(chiave, "->", valore)
```

### Set

Un set è un insieme di valori **senza duplicati** e senza ordine: utile per sapere quali
valori distinti compaiono.

```python
giorni = ["Sun", "Sat", "Sun", "Thur", "Sat", "Sun"]
print(set(giorni))          # i valori distinti
print(len(set(giorni)))     # 3
```

### List comprehension

Una list comprehension costruisce una lista a partire da un'altra, in una riga.

```python
conti = [16.99, 10.34, 21.01, 23.68, 24.59]

con_servizio = [c * 1.10 for c in conti]          # trasforma ogni elemento
grandi = [c for c in conti if c > 20]             # tiene solo alcuni elementi
print(grandi)                                     # [21.01, 23.68, 24.59]
```

### Un piccolo dataset come lista di dizionari

Una tabella si può rappresentare come lista di righe, dove ogni riga è un dizionario con
le stesse chiavi.

```python
dataset = [
    {"total_bill": 16.99, "tip": 1.01, "day": "Sun", "size": 2},
    {"total_bill": 10.34, "tip": 1.66, "day": "Sun", "size": 3},
    {"total_bill": 20.65, "tip": 3.35, "day": "Sat", "size": 3},
    {"total_bill": 27.20, "tip": 4.00, "day": "Thur", "size": 4},
]

print(len(dataset))                  # numero di righe
print(dataset[0]["tip"])             # un valore: riga 0, colonna "tip"
mance = [riga["tip"] for riga in dataset]     # una "colonna"
print(mance)
```

## 4. Controllo di flusso e funzioni (40 min)

### `if` / `elif` / `else`

```python
percentuale = 12.5

if percentuale >= 20:
    giudizio = "generosa"
elif percentuale >= 10:
    giudizio = "nella norma"
else:
    giudizio = "bassa"

print(giudizio)
```

!!! warning "Errore tipico: indentazione"
    In Python i blocchi si delimitano con il **rientro** (4 spazi), non con parentesi. Le
    righe dello stesso blocco devono avere lo stesso rientro, e la riga che apre il blocco
    termina con i due punti. Un rientro sbagliato produce `IndentationError` oppure, peggio,
    un programma che fa una cosa diversa da quella voluta.

### Cicli `for` e `while`

```python
mance = [1.01, 1.66, 3.35, 4.00]

totale = 0
for m in mance:              # ripete il blocco per ogni elemento
    totale = totale + m
print(totale)

for i in range(3):           # range(3) produce 0, 1, 2
    print("giro", i)

# while ripete finché la condizione è vera
capitale = 1000
anni = 0
while capitale < 1200:
    capitale = capitale * 1.05
    anni = anni + 1
print(anni)                  # 4
```

Nell'analisi dati `for` è di gran lunga il più usato; con `while` bisogna assicurarsi che
la condizione prima o poi diventi falsa, altrimenti il ciclo non termina.

### Funzioni

Una funzione dà un nome a un blocco di codice riutilizzabile: riceve **parametri** e
restituisce un risultato con `return`.

```python
def percentuale_mancia(conto, mancia):
    """Restituisce la mancia come percentuale del conto."""
    return mancia / conto * 100

print(percentuale_mancia(16.99, 1.01))
print(round(percentuale_mancia(conto=20.65, mancia=3.35), 1))    # 16.2


def media_e_massimo(valori):
    """Restituisce media e massimo di una lista di numeri."""
    media = sum(valori) / len(valori)
    massimo = max(valori)
    return media, massimo          # due risultati, restituiti come tupla

m, mx = media_e_massimo([1.01, 1.66, 3.35, 4.00])
print(m, mx)
```

Senza `return` una funzione restituisce `None`: stampare un valore con `print` dentro la
funzione non equivale a restituirlo.

### `import` di moduli

Un **modulo** è una raccolta di funzioni pronte. La libreria standard di Python ne contiene
molti; altri (pandas, NumPy…) si installano a parte e in Colab sono già disponibili.

```python
import math
import statistics as st            # "as" assegna un nome più corto
from datetime import date

print(math.sqrt(16))
print(st.mean([1.01, 1.66, 3.35, 4.00]), st.median([1.01, 1.66, 3.35, 4.00]))
print(date(2026, 11, 15).year)
```

## 5. Esercitazione ponte: un CSV letto "a mano" (20 min)

Un file CSV è un file di testo in cui ogni riga è una riga della tabella e i valori sono
separati da virgole. La prima riga contiene di solito i nomi delle colonne. Il modulo
`csv` della libreria standard lo legge riga per riga.

```python
import csv
import urllib.request

URL_DATI = "https://raw.githubusercontent.com/emanbuc/corso_intro_python_analisi_dati/main/docs/dati/"
urllib.request.urlretrieve(URL_DATI + "tips.csv", "tips.csv")    # scarica il file accanto al notebook

with open("tips.csv", newline="") as f:
    righe = list(csv.DictReader(f))      # ogni riga diventa un dizionario

print(len(righe))
print(righe[0])
```

Guardate bene la prima riga: **tutti i valori sono stringhe**, anche i numeri. Prima di
fare calcoli vanno convertiti.

### Media per categoria, a mano

Domanda: qual è la mancia media per ciascun giorno della settimana?

```python
somme = {}
conteggi = {}

for riga in righe:
    giorno = riga["day"]
    mancia = float(riga["tip"])              # conversione esplicita da testo a numero
    if giorno not in somme:
        somme[giorno] = 0
        conteggi[giorno] = 0
    somme[giorno] = somme[giorno] + mancia
    conteggi[giorno] = conteggi[giorno] + 1

for giorno in somme:
    media = somme[giorno] / conteggi[giorno]
    print(f"{giorno}: {media:.2f}")
```

### I limiti dell'approccio manuale

Funziona, ma per una sola domanda abbiamo scritto una dozzina di righe, e abbiamo dovuto:

- convertire a mano ogni numero (e se una cella fosse vuota, `float("")` darebbe errore);
- gestire a mano l'inizializzazione di somme e conteggi;
- riscrivere quasi tutto per cambiare domanda (mediana invece di media, due categorie invece di una).

Nella [lezione 2](02-numpy-pandas.md) la stessa risposta si otterrà con pandas in una riga:
è il motivo per cui esiste.

## Errori tipici da anticipare

| Errore | Come si manifesta | Rimedio |
|---|---|---|
| Indentazione | `IndentationError`, o codice che finisce fuori dal blocco | 4 spazi per livello, mai mescolare tabulazioni e spazi |
| Indici che partono da 0 | `IndexError`, o l'elemento sbagliato | Il primo elemento è `[0]`, l'ultimo `[-1]` |
| Celle eseguite fuori ordine | `NameError`, o risultati che cambiano a ogni esecuzione | *Riavvia ed esegui tutto* prima di fidarsi del risultato |
| Confusione tra `=` e `==` | `SyntaxError` nelle condizioni | `=` assegna, `==` confronta |

## Risultato atteso ed esercizi per casa

Al termine ogni partecipante ha un notebook funzionante con esempi commentati di tipi,
strutture dati e funzioni. Gli esercizi per casa (tre esercizi brevi su liste e dizionari
e una funzione che conta le occorrenze di ogni valore in una lista) sono in fondo
all'[esercitazione 1](../esercitazioni/01-fondamenti-python.md).

## Riferimenti

- [Tutorial ufficiale di Python](https://docs.python.org/3/tutorial/), capitoli 3–5.
- [Modulo `csv`](https://docs.python.org/3/library/csv.html) nella documentazione di Python.

---

[Programma](../programma.md) · [Esercitazione 1 →](../esercitazioni/01-fondamenti-python.md) · [Lezione 2 →](02-numpy-pandas.md)
