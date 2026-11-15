# Mini-progetto finale — Il turismo a Milano, 2023 e 2024

[![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/emanbuc/corso_intro_python_analisi_dati/blob/main/docs/esercitazioni/04-mini-progetto/mini-progetto.ipynb) · [Scarica il notebook](04-mini-progetto/mini-progetto.ipynb)

Il mini-progetto è la **verifica finale** del corso: un notebook di analisi completo su un
dataset aperto reale, da iniziare in aula (lezione 3, blocco 4) e completare entro una settimana.

## Obiettivi di apprendimento

Svolgere in autonomia un'analisi dall'inizio alla fine: caricamento, pulizia motivata,
aggregazioni e join, due grafici, conclusioni scritte.

## I dati

Presenze turistiche mensili a Milano per regione italiana di provenienza, anni 2023 e 2024,
pubblicate dal Comune di Milano con licenza CC BY 4.0 (fonte e dettagli nella pagina
[Dataset](../dati.md)). I file sono quelli originali, non ripuliti.

| File | Contenuto |
|---|---|
| [`ds370_presenze_mensili_regioni_2023.csv`](../dati/ds370_presenze_mensili_regioni_2023.csv) | Presenze mensili per regione, 2023 |
| [`ds370_presenze_mensili_regioni_2024.csv`](../dati/ds370_presenze_mensili_regioni_2024.csv) | Presenze mensili per regione, 2024 |
| [`regioni.csv`](../dati/regioni.csv) | Anagrafica: nome esteso e ripartizione geografica di ogni regione |

## Le domande

1. Le presenze complessive sono cresciute o diminuite tra il 2023 e il 2024? Di quanto, e in quali mesi?
2. Quali regioni di provenienza sono cresciute di più e quali di meno, in percentuale?
3. Quanto pesa ciascuna ripartizione geografica (Nord-ovest, Nord-est, Centro, Sud, Isole) sul totale delle presenze, e come è cambiata tra i due anni?

## Consegna

Un notebook, costruito a partire dal modello, che contenga:

1. **Caricamento** dei due file annuali, con la verifica che siano stati letti correttamente, e la loro unione in un'unica tabella.
2. **Pulizia** motivata: nomi delle colonne, testo, mesi, controlli su duplicati, valori mancanti e completezza.
3. **Analisi** che risponde alle tre domande, compreso il `merge` con l'anagrafica delle regioni e il controllo delle righe prima e dopo.
4. **Due grafici** con titolo, etichette e scala non fuorviante, ciascuno commentato.
5. **Conclusioni scritte** (5–10 righe): che cosa dicono i dati e che cosa non possono dire.

Il notebook deve funzionare con *Riavvia ed esegui tutto* ed essere leggibile da una persona
che non ha seguito il corso. Si lavora individualmente o a coppie.

!!! tip "Da dove partire"
    L'[esempio realistico](../esempi/turismo-milano.md) svolge un'analisi completa sul solo
    2023 con domande diverse: usatelo come guida per il metodo. Attenzione: i due file annuali
    non sono formattati allo stesso modo.

## Valutazione

| Criterio | Peso |
|---|---|
| Correttezza del codice e dei risultati | 40% |
| Pulizia dei dati motivata | 20% |
| Qualità e leggibilità dei grafici | 20% |
| Chiarezza di commenti e conclusioni | 20% |

Trattandosi della verifica finale, per il mini-progetto non è pubblicata una soluzione.

---

[← Esempio realistico](../esempi/turismo-milano.md) · [Lezione 3](../lezioni/03-analisi-visualizzazione.md) · [Programma](../programma.md)
