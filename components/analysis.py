import streamlit as st
from utils.helpers import format_percentage


def render_advanced_analysis(metrics_data, df_data, currencies):
    """Seção de análises avançadas: variações percentuais e volatilidade"""

    st.subheader("🔍 Análises Avançadas (Histórico AwesomeAPI)")

    render_percentage_changes(metrics_data, currencies)
    render_volatility_analysis(metrics_data, currencies)


def render_percentage_changes(metrics_data, currencies):
    """Exibe variações percentuais"""

    st.markdown("#### 📈 Variações Percentuais")

    cols = st.columns(len(currencies))

    for idx, currency in enumerate(currencies):
        metric = metrics_data.get(currency, {})

        change_90d = metric.get("change_90d", 0)
        delta_color = "normal" if change_90d >= 0 else "inverse"

        with cols[idx]:
            st.metric(
                label=f"{currency} período escolhido",
                value=format_percentage(change_90d),
                delta_color=delta_color
            )


def render_volatility_analysis(metrics_data, currencies):
    """Mostra ranking de volatilidade"""

    st.markdown("#### 📉 Volatilidade")

    vol_list = []

    for c in currencies:
        if c == "BRL":
            continue
        metric = metrics_data.get(c, {})
        vol_list.append((c, metric.get("volatility", 0)))

    # Ordena por maior volatilidade
    vol_list.sort(key=lambda x: x[1], reverse=True)

    if not vol_list:
        st.info("Nenhuma moeda com dados suficientes.")
        return

    cols = st.columns(len(vol_list))

    for idx, (currency, volatility) in enumerate(vol_list):
        with cols[idx]:
            st.metric(
                label=f"{currency} Vol.",
                value=f"{volatility:.1f}%"
            )
