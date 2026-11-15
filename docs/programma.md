# Programma

Tre lezioni da 3 ore, ciascuna con una pausa di 10 minuti a metà. Un unico dataset
([`tips`](dati.md)) accompagna le tre lezioni, così si ritrovano gli stessi dati a ogni passaggio.

!!! note "Ipotesi da confermare"
    Durata di 3 ore a lezione e pubblico principiante sono assunzioni: se cambiano,
    vanno ricalibrati i tempi dei blocchi.

## Lezione 1 — Fondamenti di Python e ambiente di lavoro

[Pagina della lezione](lezioni/01-fondamenti-python.md) · [Esercitazione](esercitazioni/01-fondamenti-python.md) · [Soluzioni](soluzioni/01-fondamenti-python.md)

| Blocco | Durata | Contenuti | Attività |
|---|---|---|---|
| 1. Ambiente e notebook | 30 min | Perché Python per i dati; Colab e Jupyter; celle di codice e Markdown; kernel e ordine di esecuzione | Aprire il notebook del corso ed eseguire le prime celle |
| 2. Sintassi di base | 45 min | Variabili; tipi `int`, `float`, `str`, `bool`; operatori; stringhe e f-string; `print` e `type` | Calcoli su valori singoli: percentuali, variazioni, conversioni |
| 3. Strutture dati | 45 min | Liste, tuple, dizionari, set; indici e slicing; metodi principali; list comprehension | Rappresentare un piccolo dataset come lista di dizionari |
| 4. Controllo di flusso e funzioni | 40 min | `if`/`elif`/`else`; cicli `for` e `while`; `def`, parametri e `return`; `import` di moduli | Scrivere una funzione che calcola media e massimo di una lista |
| 5. Esercitazione ponte | 20 min | Lettura di un CSV con il modulo `csv`; limiti dell'approccio manuale | Calcolare una media per categoria "a mano", da rifare con pandas nella lezione 2 |

**Risultato atteso.** Ogni partecipante ha un notebook funzionante con esempi commentati di tipi, strutture dati e funzioni.

**Esercizi per casa.** Tre esercizi brevi su liste e dizionari e una funzione che conta le occorrenze di ogni valore in una lista.

## Lezione 2 — NumPy e pandas: caricare, selezionare e pulire i dati

[Pagina della lezione](lezioni/02-numpy-pandas.md) · [Esercitazione](esercitazioni/02-numpy-pandas.md) · [Soluzioni](soluzioni/02-numpy-pandas.md)

| Blocco | Durata | Contenuti | Attività |
|---|---|---|---|
| 1. NumPy essenziale | 30 min | `ndarray`; operazioni vettorizzate contro cicli; broadcasting; `mean`, `std`, `min`, `max` | Confrontare un calcolo con ciclo `for` e con array |
| 2. Series e DataFrame | 40 min | `read_csv` e `read_excel`; `head`, `shape`, `info`, `describe`, `dtypes`; indice e colonne | Caricare il dataset del corso e descriverne la struttura |
| 3. Selezione e filtri | 40 min | Selezione di colonne; `loc` e `iloc`; maschere booleane e condizioni multiple; `sort_values`; nuove colonne calcolate | Rispondere a cinque domande usando solo filtri e ordinamenti |
| 4. Pulizia dei dati | 45 min | Valori mancanti: `isna`, `dropna`, `fillna`; duplicati; `astype`; date con `to_datetime`; metodi `.str` | Ripulire una versione "sporca" del dataset e salvarla con `to_csv` |
| 5. Esercitazione | 25 min | Ripasso guidato dell'intero flusso carica → ispeziona → filtra → pulisci | Rifare con pandas la media per categoria della lezione 1 |

**Risultato atteso.** Un notebook che parte da un CSV grezzo e produce un DataFrame pulito, con ogni passaggio motivato in una cella Markdown.

**Esercizi per casa.** Pulizia di un secondo dataset con almeno tre problemi di qualità da individuare e correggere.

## Lezione 3 — Analisi esplorativa, visualizzazione e mini-progetto

[Pagina della lezione](lezioni/03-analisi-visualizzazione.md) · [Esercitazione](esercitazioni/03-analisi-visualizzazione.md) · [Soluzioni](soluzioni/03-analisi-visualizzazione.md) · [Esempio realistico](esempi/turismo-milano.md) · [Mini-progetto](esercitazioni/04-mini-progetto.md)

| Blocco | Durata | Contenuti | Attività |
|---|---|---|---|
| 1. Aggregazioni | 40 min | `value_counts`; `groupby` con `agg`; `pivot_table`; statistiche per gruppo | Costruire una tabella riassuntiva per due variabili categoriche |
| 2. Combinare tabelle | 25 min | `merge` e tipi di join; `concat`; controllo delle righe prima e dopo | Arricchire il dataset con una tabella di anagrafica |
| 3. Visualizzazione | 50 min | Matplotlib: figura e assi; grafici da pandas; seaborn: istogramma, boxplot, scatter, barre, linee; titoli, etichette, salvataggio | Scegliere e realizzare il grafico adatto a quattro domande diverse |
| 4. Mini-progetto guidato | 50 min | Dalla domanda al risultato: caricamento, pulizia, analisi, due grafici, conclusioni scritte | Lavoro individuale o a coppie su un dataset assegnato |
| 5. Chiusura | 15 min | Buone pratiche: notebook riproducibile, nomi chiari, celle Markdown; prossimi passi | Discussione dei risultati e domande |

**Risultato atteso.** Un notebook di analisi completo, leggibile da una persona che non ha seguito il corso.

**Consegna.** Il notebook del [mini-progetto](esercitazioni/04-mini-progetto.md), completato entro una settimana, è la verifica finale.

## Valutazione del mini-progetto

| Criterio | Peso |
|---|---|
| Correttezza del codice e dei risultati | 40% |
| Pulizia dei dati motivata | 20% |
| Qualità e leggibilità dei grafici | 20% |
| Chiarezza di commenti e conclusioni | 20% |
