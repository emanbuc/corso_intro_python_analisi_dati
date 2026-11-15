# Dataset del corso

Tutti i file sono nella cartella [`docs/dati`](https://github.com/emanbuc/corso_intro_python_analisi_dati/tree/main/docs/dati)
del repository. Nei notebook si leggono direttamente dall'indirizzo:

```text
https://raw.githubusercontent.com/emanbuc/corso_intro_python_analisi_dati/main/docs/dati/
```

## Dataset guida: `tips`

| File | Descrizione |
|---|---|
| [`tips.csv`](dati/tips.csv) | Dataset di esempio `tips` di seaborn (lo stesso di `sns.load_dataset("tips")`), copiato senza modifiche dal repository [seaborn-data](https://github.com/mwaskom/seaborn-data). 244 conti di un ristorante: importo, mancia, sesso di chi paga, fumatori, giorno, pasto, numero di persone. |
| [`tips.xlsx`](dati/tips.xlsx) | Lo stesso contenuto in formato Excel, per provare `read_excel`. |
| [`giorni.csv`](dati/giorni.csv) | Piccola tabella di anagrafica dei giorni (nome italiano, fine settimana), preparata per il corso per l'esercizio sul `merge`. |

## Versioni "sporche" (dati modificati a scopo didattico)

!!! warning "Dati alterati apposta"
    Questi file **non sono dati reali**: partono dai dataset di seaborn e contengono problemi
    di qualità aggiunti dallo script
    [`scripts/genera_dati_sporchi.py`](https://github.com/emanbuc/corso_intro_python_analisi_dati/blob/main/scripts/genera_dati_sporchi.py).
    Servono solo per esercitarsi nella pulizia.

| File | Problemi aggiunti |
|---|---|
| [`tips_sporco.csv`](dati/tips_sporco.csv) | Separatore `;` e virgola decimale, valori mancanti, righe duplicate, testo con maiuscole/minuscole e spazi incoerenti. Le colonne `id_conto` (numero progressivo) e `data` (data **fittizia**, coerente solo con il giorno della settimana) non esistono nell'originale. |
| [`penguins_sporco.csv`](dati/penguins_sporco.csv) | Dal dataset `penguins` di seaborn ([`penguins.csv`](dati/penguins.csv), copiato senza modifiche): specie scritte in modo incoerente, massa corporea come testo con unità di misura, righe duplicate. I valori mancanti erano già presenti nell'originale. |

## Dati reali: turismo a Milano

| File | Descrizione |
|---|---|
| [`ds370_presenze_mensili_regioni_2023.csv`](dati/ds370_presenze_mensili_regioni_2023.csv) | Presenze turistiche mensili per regione di provenienza, anno 2023. |
| [`ds370_presenze_mensili_regioni_2024.csv`](dati/ds370_presenze_mensili_regioni_2024.csv) | Come sopra, anno 2024. |
| [`regioni.csv`](dati/regioni.csv) | Tabella di anagrafica preparata per il corso: per ogni voce del dataset, nome esteso e ripartizione geografica (Nord-ovest, Nord-est, Centro, Sud, Isole). |

**Fonte:** Comune di Milano, dataset
[«Turismo: presenze mensili per regioni»](https://dati.comune.milano.it/dataset/ds370-turismotempolibero-presenze-regione-mese),
licenza [Creative Commons Attribuzione 4.0 Internazionale (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.it).
I due file CSV sono copie identiche byte per byte di quelli pubblicati sul portale (scaricati il 15 novembre 2026)
e **non sono stati ripuliti**: separatori, nomi di colonna e formato dei mesi sono quelli originali.
Per il significato esatto delle grandezze fate riferimento alla pagina del dataset sul portale.
