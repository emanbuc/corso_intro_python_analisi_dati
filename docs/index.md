# Introduzione a Python per l'analisi dati

Il corso porta chi non ha mai programmato in Python a **caricare, pulire, analizzare e
visualizzare un dataset tabellare in autonomia**, in 3 lezioni da 3 ore (9 ore totali).

| Voce | Descrizione |
|---|---|
| Destinatari | Studenti o professionisti senza esperienza di Python, con familiarità con fogli di calcolo |
| Prerequisiti | Uso base del computer; nozioni elementari di statistica descrittiva (media, mediana, percentuali) |
| Durata | 3 lezioni × 3 ore, con una pausa di 10 minuti a metà lezione |
| Modalità | Live coding su notebook: il docente scrive, i partecipanti replicano ed estendono |
| Ambiente | Google Colab (nessuna installazione) oppure JupyterLab locale |
| Verifica finale | [Mini-progetto](esercitazioni/04-mini-progetto.md): notebook di analisi su un dataset assegnato |

## Obiettivi formativi

Al termine i partecipanti sanno:

1. Scrivere ed eseguire codice Python in un notebook, usando tipi, strutture dati, cicli e funzioni.
2. Caricare dati da CSV ed Excel in un DataFrame pandas e ispezionarne struttura e qualità.
3. Pulire i dati: valori mancanti, duplicati, tipi errati, date e stringhe.
4. Filtrare, ordinare, aggregare e combinare tabelle per rispondere a una domanda di analisi.
5. Produrre grafici leggibili con Matplotlib e seaborn e commentarne il risultato.

## Percorso

| Lezione | Argomento | Esercitazione | Soluzioni |
|---|---|---|---|
| [Lezione 1](lezioni/01-fondamenti-python.md) | Fondamenti di Python e ambiente di lavoro | [Esercitazione 1](esercitazioni/01-fondamenti-python.md) | [Soluzioni 1](soluzioni/01-fondamenti-python.md) |
| [Lezione 2](lezioni/02-numpy-pandas.md) | NumPy e pandas: caricare, selezionare e pulire i dati | [Esercitazione 2](esercitazioni/02-numpy-pandas.md) | [Soluzioni 2](soluzioni/02-numpy-pandas.md) |
| [Lezione 3](lezioni/03-analisi-visualizzazione.md) | Analisi esplorativa, visualizzazione e mini-progetto | [Esercitazione 3](esercitazioni/03-analisi-visualizzazione.md) | [Soluzioni 3](soluzioni/03-analisi-visualizzazione.md) |
| [Esempio realistico](esempi/turismo-milano.md) | Un'analisi completa su dati aperti del Comune di Milano | [Mini-progetto finale](esercitazioni/04-mini-progetto.md) | — |

Il dettaglio dei blocchi e dei tempi è nel [programma](programma.md); dati e fonti sono
descritti nella pagina [Dataset](dati.md); letture e strumenti in [Risorse](risorse.md).

## Come si lavora

Ogni lezione ha una pagina di teoria con esempi da eseguire e un notebook di esercitazione
da aprire in Colab con il pulsante **Apri in Colab**. Le soluzioni sono in pagine e notebook
separati: provate prima da soli, il confronto con la soluzione serve dopo.

!!! tip "Strumenti"
    Python 3.11 o successivo, pandas, NumPy, Matplotlib, seaborn. Con Google Colab è
    tutto già installato: basta un account Google.
