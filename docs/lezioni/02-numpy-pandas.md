# Lezione 2 — NumPy e pandas: caricare, selezionare e pulire i dati

La seconda lezione introduce il DataFrame come strumento di lavoro e copre il percorso
dal file grezzo a una tabella pulita.

!!! abstract "Obiettivi"
    - Usare gli array NumPy per calcoli vettorizzati.
    - Caricare un CSV o un file Excel in un DataFrame e descriverne struttura e qualità.
    - Selezionare colonne e righe con `loc`, `iloc` e maschere booleane; ordinare; creare colonne calcolate.
    - Pulire i dati: valori mancanti, duplicati, tipi errati, date e stringhe.

**Esercitazione collegata:** [Esercitazione 2](../esercitazioni/02-numpy-pandas.md)

## 1. NumPy essenziale (30 min)

### `ndarray`

NumPy introduce l'**array** (`ndarray`): una sequenza di valori tutti dello stesso tipo, su
cui le operazioni si applicano a tutti gli elementi in un colpo solo.

```python
import numpy as np

conti = np.array([16.99, 10.34, 21.01, 23.68, 24.59])
mance = np.array([1.01, 1.66, 3.50, 3.31, 3.61])

print(conti.dtype, conti.shape)      # tipo degli elementi e dimensioni
print(conti[0], conti[1:3])          # indici e slicing come nelle liste
```

### Operazioni vettorizzate contro cicli

Con le liste, per calcolare la percentuale di mancia di ogni conto serve un ciclo. Con gli
array si scrive la formula una volta sola: l'operazione è **vettorizzata**, cioè applicata
elemento per elemento.

```python
# Con liste e ciclo for
lista_conti = [16.99, 10.34, 21.01, 23.68, 24.59]
lista_mance = [1.01, 1.66, 3.50, 3.31, 3.61]
percentuali = []
for i in range(len(lista_conti)):
    percentuali.append(lista_mance[i] / lista_conti[i] * 100)
print(percentuali)

# Con array NumPy
percentuali = mance / conti * 100
print(percentuali.round(1))
```

Il codice vettorizzato è più corto, più leggibile e, su dati grandi, molto più veloce,
perché il ciclo viene eseguito all'interno di NumPy invece che in Python.

### Broadcasting

Quando un'operazione coinvolge un array e un singolo numero, il numero viene "esteso" a
tutti gli elementi: è il caso più semplice di **broadcasting**.

```python
print(conti * 1.10)            # ogni conto aumentato del 10%
print(conti - conti.mean())    # scarto di ogni conto dalla media
print(conti > 20)              # confronto: array di True/False
print(conti[conti > 20])       # un array booleano si può usare come filtro
```

### Statistiche

```python
print(conti.mean(), conti.std(), conti.min(), conti.max())
print(conti.sum(), np.median(conti))
```

pandas è costruito sopra NumPy: ogni colonna numerica di un DataFrame si comporta come un
array, e tutto ciò che avete appena visto vale anche lì.

## 2. Series e DataFrame (40 min)

Un **DataFrame** è una tabella: righe e colonne con un nome. Ogni colonna è una **Series**,
cioè una sequenza di valori dello stesso tipo accompagnata da un **indice** che etichetta
le righe.

### `read_csv` e `read_excel`

```python
import pandas as pd

URL_DATI = "https://raw.githubusercontent.com/emanbuc/corso_intro_python_analisi_dati/main/docs/dati/"

tips = pd.read_csv(URL_DATI + "tips.csv")
tips.head()
```

`read_csv` accetta un percorso locale o un indirizzo web. I parametri che servono più
spesso sono `sep` (separatore delle colonne, se non è la virgola), `decimal` (separatore
decimale) ed `encoding`.

Per un file Excel si usa `read_excel`, che legge il primo foglio oppure quello indicato
con `sheet_name`:

```python
tips_excel = pd.read_excel(URL_DATI + "tips.xlsx")
print(tips_excel.shape)
```

### Ispezionare la struttura

Le prime cose da fare con una tabella appena caricata:

```python
print(tips.shape)        # (numero di righe, numero di colonne)
print(tips.columns)      # nomi delle colonne
print(tips.dtypes)       # tipo di ogni colonna
tips.info()              # riepilogo: colonne, valori non nulli, tipi, memoria
```

```python
print(tips.head(3))      # prime righe (tail per le ultime)
print(tips.describe())   # statistiche delle colonne numeriche
print(tips.index)        # l'indice: qui un semplice contatore da 0
```

Il dataset `tips` contiene 244 conti di un ristorante:

| Colonna | Significato |
|---|---|
| `total_bill` | importo del conto in dollari |
| `tip` | mancia in dollari |
| `sex` | sesso di chi paga |
| `smoker` | presenza di fumatori al tavolo |
| `day` | giorno della settimana (`Thur`, `Fri`, `Sat`, `Sun`) |
| `time` | pasto (`Lunch` o `Dinner`) |
| `size` | numero di persone al tavolo |

!!! note "Una colonna è una Series"
    `tips["tip"]` è una Series: ha i suoi metodi (`mean`, `max`, `value_counts`…) e si
    comporta come un array NumPy con un'etichetta per ogni valore.

## 3. Selezione e filtri (40 min)

### Selezionare colonne

```python
mance = tips["tip"]                       # una colonna -> Series
parte = tips[["total_bill", "tip"]]       # più colonne -> DataFrame (notare le doppie parentesi)
print(mance.mean())
print(parte.head(3))
```

### `loc` e `iloc`

- `loc` seleziona per **etichetta**: nomi delle colonne e valori dell'indice.
- `iloc` seleziona per **posizione**: numeri interi che partono da 0, come nelle liste.

```python
print(tips.loc[0, "tip"])                       # riga con etichetta 0, colonna "tip"
print(tips.loc[0:2, ["total_bill", "tip"]])     # etichette da 0 a 2 COMPRESO
print(tips.iloc[0, 1])                          # prima riga, seconda colonna
print(tips.iloc[0:2, 0:2])                      # posizioni 0 e 1: il 2 è ESCLUSO
```

!!! warning "Errore tipico: `loc` e `iloc`"
    Finché l'indice è il contatore 0, 1, 2… i due sembrano equivalenti, ma non lo sono:
    con `loc` l'estremo finale dell'intervallo è **compreso**, con `iloc` è **escluso**.
    Dopo un filtro o un ordinamento, inoltre, le etichette non coincidono più con le posizioni.

### Maschere booleane

Un confronto su una colonna produce una Series di `True`/`False` (una **maschera**), che
usata tra parentesi quadre tiene solo le righe `True`.

```python
maschera = tips["total_bill"] > 40
print(maschera.sum())                 # quante righe soddisfano la condizione
print(tips[maschera])

# Condizioni multiple: & (e), | (oppure), ~ (non), ogni condizione tra parentesi
cene_sabato = tips[(tips["day"] == "Sat") & (tips["time"] == "Dinner")]
print(len(cene_sabato))

weekend = tips[tips["day"].isin(["Sat", "Sun"])]      # isin: appartenenza a un elenco
print(len(weekend))
```

!!! warning "Errore tipico: parentesi nelle condizioni multiple"
    `tips[tips["day"] == "Sat" & tips["size"] > 2]` dà errore: `&` e `|` hanno precedenza
    sui confronti, quindi **ogni condizione va racchiusa tra parentesi**. Con le Series
    non si usano `and` e `or`.

### Ordinare

```python
print(tips.sort_values("tip", ascending=False).head(5))          # le 5 mance più alte
print(tips.sort_values(["day", "total_bill"]).head(3))           # per più colonne
```

`sort_values` restituisce una nuova tabella: l'originale non cambia finché non si
riassegna il risultato (`tips = tips.sort_values(...)`).

### Nuove colonne calcolate

```python
tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100        # operazione vettorizzata
tips["a_testa"] = tips["total_bill"] / tips["size"]
print(tips[["total_bill", "tip", "tip_pct", "a_testa"]].head(3).round(2))
```

Per modificare solo alcune righe si usa `loc` con una maschera e il nome della colonna:

```python
tips["tavolo"] = "piccolo"
tips.loc[tips["size"] >= 4, "tavolo"] = "grande"
print(tips["tavolo"].value_counts())
```

!!! warning "Errore tipico: `SettingWithCopyWarning`"
    Scrivere in due passaggi, `tips[tips["size"] >= 4]["tavolo"] = "grande"`, non modifica
    `tips`: il primo passaggio crea una tabella temporanea ed è quella a essere modificata.
    Le versioni di pandas precedenti alla 3 lo segnalano con l'avviso
    `SettingWithCopyWarning`; in ogni versione la forma corretta è quella con `loc` in un
    solo passaggio, `tips.loc[maschera, "colonna"] = valore`. Quando serve davvero una
    tabella separata su cui lavorare, createla esplicitamente con `.copy()`.

## 4. Pulizia dei dati (45 min)

I dati reali arrivano quasi sempre con qualche problema. Lavoriamo su `tips_sporco.csv`,
una versione del dataset a cui sono stati aggiunti apposta difetti tipici
(vedi [Dataset](../dati.md)).

```python
sporco = pd.read_csv(URL_DATI + "tips_sporco.csv", sep=";")     # qui il separatore è il punto e virgola
print(sporco.shape)
print(sporco.head())
sporco.info()
```

`info` rivela già due sintomi: `total_bill` e `tip` non sono colonne numeriche, e alcune
colonne hanno meno valori non nulli del numero di righe.

### Duplicati

```python
print(sporco.duplicated().sum())          # righe identiche a una riga precedente
sporco = sporco.drop_duplicates()
print(sporco.shape)
```

### Tipi errati: `astype`

I numeri sono stati letti come testo perché usano la virgola come separatore decimale
(`"16,99"`). Si sostituisce la virgola con il punto e si converte.

```python
sporco["total_bill"] = sporco["total_bill"].str.replace(",", ".").astype(float)
sporco["tip"] = sporco["tip"].str.replace(",", ".").astype(float)
print(sporco[["total_bill", "tip"]].dtypes)
```

!!! tip "La scorciatoia in lettura"
    Quando si sa in anticipo che il file usa la virgola decimale, basta dirlo a
    `read_csv`: `pd.read_csv(percorso, sep=";", decimal=",")`.

### Stringhe: i metodi `.str`

I metodi di testo visti nella lezione 1 si applicano a un'intera colonna tramite `.str`.

```python
print(sporco["day"].unique())             # stessi giorni scritti in modi diversi

sporco["day"] = sporco["day"].str.strip().str.capitalize()
sporco["sex"] = sporco["sex"].str.strip().str.capitalize()
print(sporco["day"].unique())
print(sporco["sex"].unique())
```

`strip` toglie gli spazi ai bordi, `capitalize` mette maiuscola solo la prima lettera.
Altri metodi utili: `lower`, `upper`, `replace`, `contains`, `split`.

### Date: `to_datetime`

La colonna `data` è testo nel formato giorno/mese/anno. `to_datetime` la converte in un
vero tipo data, da cui si estraggono anno, mese, giorno della settimana.

```python
sporco["data"] = pd.to_datetime(sporco["data"], format="%d/%m/%Y")
print(sporco["data"].dtype)
print(sporco["data"].min(), sporco["data"].max())
print(sporco["data"].dt.month.value_counts().sort_index())      # conti per mese
print(sporco["data"].dt.day_name().head(3))
```

Indicare sempre il formato (`%d` giorno, `%m` mese, `%Y` anno a quattro cifre): una data
come `03/04/2024` è ambigua, e senza formato pandas la interpreta come mese/giorno.

!!! note "Attenzione"
    In questo file la colonna `data` è **fittizia**: è stata aggiunta per esercitarsi con
    le date e non descrive quando i conti sono stati realmente pagati.

### Valori mancanti: `isna`, `dropna`, `fillna`

pandas rappresenta il dato mancante con `NaN`. Prima si contano, poi si decide.

```python
print(sporco.isna().sum())                 # valori mancanti per colonna
print(sporco[sporco["tip"].isna()].head(3))
```

Le scelte possibili sono tre, e vanno motivate caso per caso:

```python
# 1. Eliminare le righe in cui manca un dato indispensabile per l'analisi
pulito = sporco.dropna(subset=["tip"])

# 2. Sostituire con un valore esplicito che dichiara l'assenza
pulito = pulito.fillna({"sex": "Non indicato"})

# 3. Lasciare il valore mancante: molte funzioni (mean, sum, groupby) lo ignorano
print(pulito.isna().sum())
print(pulito.shape)
```

Sostituire un numero mancante con la media o con zero è una scelta forte, che cambia i
risultati: va fatta solo se si sa spiegare perché è ragionevole, e va scritta nel notebook.

### Salvare il risultato: `to_csv`

```python
pulito.to_csv("tips_pulito.csv", index=False)      # index=False: non salvare l'indice come colonna
print(pd.read_csv("tips_pulito.csv").head(3))
```

## 5. Ripasso: carica → ispeziona → filtra → pulisci (25 min)

Il flusso di lavoro visto oggi, in ordine:

1. **Carica** con `read_csv` / `read_excel`, controllando separatore e decimali.
2. **Ispeziona** con `shape`, `head`, `info`, `describe`: quante righe, che tipi, quanti valori mancanti.
3. **Pulisci**: duplicati, tipi, testo, date, valori mancanti — motivando ogni scelta.
4. **Filtra e ordina** per rispondere alle domande.

E la domanda con cui si è chiusa la lezione 1 — la mancia media per giorno — adesso si
scrive in una riga:

```python
print(tips.groupby("day")["tip"].mean().round(2))
```

`groupby` è l'argomento con cui si apre la [lezione 3](03-analisi-visualizzazione.md).

## Errori tipici da anticipare

| Errore | Come si manifesta | Rimedio |
|---|---|---|
| `loc` contro `iloc` | Righe in più o in meno, `KeyError` | `loc` = etichette (estremo compreso), `iloc` = posizioni (estremo escluso) |
| Parentesi con `&` e `\|` | `TypeError` o `ValueError` nelle condizioni multiple | Ogni condizione tra parentesi; mai `and`/`or` tra Series |
| `SettingWithCopyWarning` | Avviso, e la modifica non ha effetto | `df.loc[maschera, "colonna"] = valore` in un solo passaggio |
| Numeri letti come testo | La colonna non è numerica, `mean` fallisce | `decimal=","` in lettura, oppure `.str.replace(",", ".").astype(float)` |

## Risultato atteso ed esercizi per casa

Un notebook che parte da un CSV grezzo e produce un DataFrame pulito, con ogni passaggio
motivato in una cella Markdown. Per casa: la pulizia di un secondo dataset con almeno tre
problemi di qualità da individuare e correggere, in fondo
all'[esercitazione 2](../esercitazioni/02-numpy-pandas.md).

## Riferimenti

- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html).
- [Python for Data Analysis, 3ª edizione](https://wesmckinney.com/book/), capitoli 4 (NumPy), 5 (pandas) e 7 (pulizia).
- [Indexing and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html) nella guida di pandas.

---

[← Lezione 1](01-fondamenti-python.md) · [Programma](../programma.md) · [Esercitazione 2 →](../esercitazioni/02-numpy-pandas.md) · [Lezione 3 →](03-analisi-visualizzazione.md)
