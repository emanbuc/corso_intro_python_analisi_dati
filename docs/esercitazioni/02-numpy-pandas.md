# Esercitazione 2 — NumPy e pandas

[![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/emanbuc/corso_intro_python_analisi_dati/blob/main/docs/esercitazioni/02-numpy-pandas/esercitazione-02.ipynb) · [Scarica il notebook](02-numpy-pandas/esercitazione-02.ipynb)

**Lezione di riferimento:** [Lezione 2 — NumPy e pandas](../lezioni/02-numpy-pandas.md)

## Obiettivi di apprendimento

- Sostituire un ciclo `for` con un calcolo vettorizzato su array NumPy.
- Caricare un dataset in un DataFrame e descriverne la struttura.
- Rispondere a domande usando selezioni, maschere booleane e ordinamenti.
- Ripulire un file con duplicati, tipi errati, testo incoerente, date e valori mancanti, motivando le scelte.

## Consegna

Aprite il notebook in Colab e completate le celle che contengono `# TODO`. Dove è richiesta
una motivazione, scrivetela in una cella di testo: fa parte dell'esercizio.

| Parte | Attività | Quando |
|---|---|---|
| A | Spesa a testa con ciclo `for` e con array | In aula |
| B | Caricare `tips` e descriverne la struttura | In aula |
| C | Cinque domande con filtri e ordinamenti | In aula |
| D | Ripulire `tips_sporco.csv` e salvarlo con `to_csv` | In aula |
| E | Rifare con pandas la media per categoria della lezione 1 | In aula |
| Casa | Pulizia di `penguins_sporco.csv`: almeno tre problemi di qualità da individuare e correggere | Per casa |

## File di supporto

- [`tips.csv`](../dati/tips.csv) — dataset guida del corso.
- [`tips_sporco.csv`](../dati/tips_sporco.csv) — versione con problemi di qualità.
- [`penguins_sporco.csv`](../dati/penguins_sporco.csv) — secondo dataset, per casa.

!!! warning "Dati modificati a scopo didattico"
    I due file "sporchi" non sono dati reali: contengono difetti aggiunti apposta, e in
    `tips_sporco.csv` le colonne `id_conto` e `data` sono fittizie. Dettagli nella pagina
    [Dataset](../dati.md).

## Soluzioni

Dopo aver provato: [Soluzioni dell'esercitazione 2](../soluzioni/02-numpy-pandas.md).

---

[← Lezione 2](../lezioni/02-numpy-pandas.md) · [Programma](../programma.md) · [Lezione 3 →](../lezioni/03-analisi-visualizzazione.md)
