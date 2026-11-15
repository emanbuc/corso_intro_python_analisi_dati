# Introduzione a Python per l'analisi dati

Materiale del corso: 3 lezioni da 3 ore su Python, NumPy, pandas, Matplotlib e seaborn.
Tutto il codice di lezioni, esempio e soluzioni gira senza errori con pandas 2.2.3 e 3.0.5.

**Sito del corso:** <https://emanbuc.github.io/corso_intro_python_analisi_dati/>

## Contenuto del repository

| Percorso | Contenuto |
|---|---|
| `docs/` | Pagine del sito (lezioni, esercitazioni, soluzioni, esempio realistico, risorse) |
| `docs/dati/` | Dataset usati nel corso (vedi `docs/dati.md` per fonti e licenze) |
| `docs/**/**.ipynb` | Notebook apribili in Google Colab |
| `scripts/genera_dati_sporchi.py` | Rigenera le versioni "sporche" dei dataset e `tips.xlsx` |
| `mkdocs.yml`, `requirements.txt` | Configurazione del sito (MkDocs Material) |
| `.github/workflows/pages.yml` | Build e pubblicazione su GitHub Pages |

## Anteprima in locale

```bash
pip install -r requirements.txt
mkdocs serve
```

## Pubblicazione

Il workflow pubblica il sito a ogni push su `main`. In *Settings → Pages* la sorgente
deve essere **GitHub Actions**.
