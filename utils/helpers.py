import pandas as pd
import numpy as np

def calculate_metrics(df, currencies):
    metrics = {}

    for currency in currencies:
        if currency not in df.columns:
            continue

        values = pd.to_numeric(df[currency], errors='coerce').dropna()

        if len(values) == 0:
            continue

        current_value = values.iloc[-1]

        metrics[currency] = {
            "current_value": float(current_value),
            "change_7d": calculate_percentage_change(values, 7),
            "change_30d": calculate_percentage_change(values, 30),
            "change_90d": calculate_percentage_change(values, 90),
            "volatility": calculate_volatility(values),
            "data_points": len(values)
        }

    return metrics


def calculate_percentage_change(values, days):
    if len(values) <= days:
        return 0.0
    try:
        past = values.iloc[-(days+1)]
        current = values.iloc[-1]
        return float(((current - past) / past) * 100)
    except:
        return 0.0


def calculate_volatility(values):
    try:
        returns = values.pct_change().dropna()
        return float(returns.std() * np.sqrt(252) * 100)
    except:
        return 0.0


def format_currency_value(value, currency="BRL"):
    if value is None or pd.isna(value):
        return "R$ --.--"
    return f"R$ {value:.4f}"


def format_percentage(value):
    if value is None or pd.isna(value):
        return "--.--%"
    return f"{value:+.2f}%"


def calculate_correlation_matrix(df, currencies):
    cols = [c for c in currencies if c in df.columns]
    if len(cols) < 2:
        return None
    clean = df[cols].apply(pd.to_numeric, errors="coerce").dropna()
    if len(clean) < 10:
        return None
    return clean.corr()
