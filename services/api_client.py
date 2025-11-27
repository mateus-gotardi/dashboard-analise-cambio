import pandas as pd
import requests
import streamlit as st
from datetime import datetime, timedelta

# Moedas suportadas
SUPPORTED_CURRENCIES = ["USD", "EUR", "GBP", "JPY", "BRL"]


@st.cache_data(ttl=1800)
def fetch_from_awesome(currency: str, days: int):
    """
    Busca dados históricos da AwesomeAPI:
    https://economia.awesomeapi.com.br/json/daily/USD-BRL/90
    """

    if currency == "BRL":
        # BRL é sempre 1:1
        dates = pd.date_range(datetime.now()-timedelta(days=days), datetime.now())
        return pd.DataFrame({"date": dates, "BRL": 1.0})

    url = f"https://economia.awesomeapi.com.br/json/daily/{currency}-BRL/{days}"

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()

        df = pd.DataFrame(data)
        df["date"] = pd.to_datetime(df["timestamp"].astype(int), unit="s")
        df[currency] = pd.to_numeric(df["bid"], errors="coerce")

        return df[["date", currency]].sort_values("date")

    except:
        return pd.DataFrame()


def get_exchange_data(currencies, period="90 dias"):
    """Retorna dataframe unificado para todas as moedas."""

    period_map = {
        "7 dias": 7,
        "30 dias": 30,
        "90 dias": 90,
        "6 meses": 180
    }

    days = period_map.get(period, 90)

    series_dict = {}

    for c in currencies:
        if c not in SUPPORTED_CURRENCIES:
            continue
        df = fetch_from_awesome(c, days)
        if not df.empty:
            series_dict[c] = df

    return combine_series(series_dict)


def combine_series(data_dict):
    """ combina todas as séries mantendo consistência """

    # juntar todas as datas que aparecem em qualquer série
    all_dates = None
    for df in data_dict.values():
        if all_dates is None:
            all_dates = df["date"]
        else:
            all_dates = pd.concat([all_dates, df["date"]])

    all_dates = pd.DataFrame({"date": pd.to_datetime(all_dates.unique())})
    all_dates = all_dates.sort_values("date")

    df_final = all_dates.copy()

    # merge de cada moeda no dataframe principal
    for currency, df in data_dict.items():
        df_final = df_final.merge(df, on="date", how="left")

    # preencher buracos em feriados e finais de semana
    df_final = df_final.ffill().bfill()

    return df_final


@st.cache_data(ttl=300)
def get_single_currency_rate(currency):
    """Cotação atual (AwesomeAPI)"""

    if currency == "BRL":
        return 1.0

    url = f"https://economia.awesomeapi.com.br/json/last/{currency}-BRL"

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        key = f"{currency}BRL"
        return float(data[key]["bid"])
    except:
        return None