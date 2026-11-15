"""Genera i file derivati usati nel corso a partire dai dataset originali.

Uso (dalla radice del repository):

    python scripts/genera_dati_sporchi.py

Legge docs/dati/tips.csv e docs/dati/penguins.csv (dataset di esempio di seaborn,
non modificati) e scrive nella stessa cartella:

- tips.xlsx            : tips.csv salvato in formato Excel, senza altre modifiche
- tips_sporco.csv      : tips con problemi di qualità aggiunti a scopo didattico
- penguins_sporco.csv  : penguins con problemi di qualità aggiunti a scopo didattico

I problemi sono introdotti con un generatore casuale a seme fisso, quindi il
risultato è identico a ogni esecuzione. Le colonne `id_conto` e `data` di
tips_sporco.csv NON esistono nel dataset originale: sono aggiunte dallo script
(numero progressivo e data fittizia coerente con il giorno della settimana).
"""
from pathlib import Path

import numpy as np
import pandas as pd

DATI = Path(__file__).resolve().parent.parent / "docs" / "dati"
SEME = 2026


def genera_tips_sporco() -> pd.DataFrame:
    rng = np.random.default_rng(SEME)
    df = pd.read_csv(DATI / "tips.csv")
    n = len(df)

    # Colonne aggiunte (non presenti nell'originale)
    df.insert(0, "id_conto", range(1, n + 1))
    scarto = df["day"].map({"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3})
    settimana = rng.integers(0, 12, size=n)
    inizio = pd.Timestamp("2024-02-01")  # un giovedì
    data = inizio + pd.to_timedelta(settimana * 7 + scarto, unit="D")
    df.insert(1, "data", data.dt.strftime("%d/%m/%Y"))

    # 1. Valori mancanti
    for colonna, quanti in [("tip", 10), ("sex", 6), ("time", 5)]:
        righe = rng.choice(n, size=quanti, replace=False)
        df[colonna] = df[colonna].astype(object)
        df.loc[righe, colonna] = np.nan

    # 2. Testo incoerente: maiuscole/minuscole e spazi
    df["day"] = df["day"].astype(object)
    righe = rng.choice(n, size=30, replace=False)
    varianti = [str.upper, str.lower, lambda s: " " + s, lambda s: s + " "]
    for i, riga in enumerate(righe):
        df.loc[riga, "day"] = varianti[i % 4](df.loc[riga, "day"])
    righe = rng.choice(df.index[df["sex"].notna()], size=12, replace=False)
    df.loc[righe, "sex"] = df.loc[righe, "sex"].str.lower()

    # 3. Righe duplicate
    doppie = df.loc[rng.choice(n, size=6, replace=False)]
    df = pd.concat([df, doppie], ignore_index=True)
    df = df.sample(frac=1, random_state=SEME).reset_index(drop=True)

    # 4. Numeri con la virgola decimale (verranno letti come testo)
    for colonna in ["total_bill", "tip"]:
        df[colonna] = df[colonna].map(
            lambda x: "" if pd.isna(x) else f"{x:.2f}".replace(".", ",")
        )
    return df


def genera_penguins_sporco() -> pd.DataFrame:
    rng = np.random.default_rng(SEME + 1)
    df = pd.read_csv(DATI / "penguins.csv")
    n = len(df)

    # 1. Testo incoerente nella specie
    df["species"] = df["species"].astype(object)
    righe = rng.choice(n, size=40, replace=False)
    varianti = [str.upper, str.lower, lambda s: s + " ", lambda s: " " + s]
    for i, riga in enumerate(righe):
        df.loc[riga, "species"] = varianti[i % 4](df.loc[riga, "species"])

    # 2. Massa corporea come testo con unità di misura
    df["body_mass_g"] = df["body_mass_g"].map(
        lambda x: "" if pd.isna(x) else f"{int(x)} g"
    )

    # 3. Righe duplicate
    doppie = df.loc[rng.choice(n, size=8, replace=False)]
    df = pd.concat([df, doppie], ignore_index=True)
    return df.sample(frac=1, random_state=SEME).reset_index(drop=True)


if __name__ == "__main__":
    pd.read_csv(DATI / "tips.csv").to_excel(DATI / "tips.xlsx", index=False)
    genera_tips_sporco().to_csv(DATI / "tips_sporco.csv", sep=";", index=False)
    genera_penguins_sporco().to_csv(DATI / "penguins_sporco.csv", index=False)
    print("File generati in", DATI)
