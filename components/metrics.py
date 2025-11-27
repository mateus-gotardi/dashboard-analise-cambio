import streamlit as st
import pandas as pd
from utils.helpers import format_currency_value, format_percentage
from services.api_client import get_single_currency_rate


def render_current_rates(selected_currencies):
    """Exibe as cotações atuais no topo do dashboard"""

    st.subheader("💵 Cotações Atuais (BC)")

    cols = st.columns(len(selected_currencies))

    for idx, currency in enumerate(selected_currencies):
        with cols[idx]:

            if currency == "BRL":
                st.metric(
                    label="BRL (Real)",
                    value="R$ 1.0000"
                )
                continue

            rate = get_single_currency_rate(currency)

            if rate is not None:
                st.metric(
                    label=f"{currency}",
                    value=format_currency_value(rate)
                )
            else:
                st.metric(
                    label=f"{currency}",
                    value="R$ --.--"
                )


def render_metrics_cards(metrics_data, currencies):
    """Cards com métricas principais (valor atual + variação 7d)"""

    st.subheader("📈 Métricas Principais (Histórico AwesomeAPI)")

    cols = st.columns(len(currencies))

    currency_symbols = {
        "USD": "US$", "EUR": "€", "JPY": "¥",
        "GBP": "£", "BRL": "R$"
    }

    for idx, currency in enumerate(currencies):
        metric = metrics_data.get(currency, {})

        with cols[idx]:
            current_value = metric.get("current_value", 0)
            change_7d = metric.get("change_7d", 0)

            delta_color = "normal" if change_7d >= 0 else "inverse"

            st.metric(
                label=f"{currency} ({currency_symbols.get(currency, currency)})",
                value=format_currency_value(current_value),
                delta=format_percentage(change_7d),
                delta_color=delta_color
            )


def render_comparative_table(metrics_data, currencies):
    """Tabela comparativa completa das métricas de cada moeda"""

    st.subheader("📋 Tabela Comparativa (AwesomeAPI)")

    table_rows = []

    for currency in currencies:
        metric = metrics_data.get(currency, {})

        table_rows.append({
            "Moeda": currency,
            "Cotação": format_currency_value(metric.get("current_value", 0)),
            "Var. 7d": format_percentage(metric.get("change_7d", 0)),
            "Var. 30d": format_percentage(metric.get("change_30d", 0)),
            "Var. 90d": format_percentage(metric.get("change_90d", 0)),
            "Volatilidade": f"{metric.get('volatility', 0):.1f}%",
            "Dados": metric.get("data_points", 0)
        })

    df_table = pd.DataFrame(table_rows)
    st.dataframe(df_table, use_container_width=True, hide_index=True)
