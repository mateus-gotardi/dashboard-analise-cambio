import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from utils.helpers import calculate_correlation_matrix


def render_temporal_chart(df, currencies):

    st.subheader("📊 Evolução Temporal (Histórico AwesomeAPI)")

    fig = go.Figure()

    for c in currencies:
        if c in df.columns and c != "BRL":
            fig.add_trace(go.Scatter(
                x=df["date"], y=df[c], mode="lines", name=c
            ))

    fig.update_layout(
        height=500,
        xaxis_title="Data",
        yaxis_title="Valor (BRL)",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)


def render_correlation_heatmap(df, currencies):

    st.subheader("🔥 Heatmap de Correlação (AwesomeAPI)")

    corr = calculate_correlation_matrix(df, currencies)
    if corr is None:
        st.info("Selecione moedas com dados suficientes.")
        return

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
    )

    st.plotly_chart(fig, use_container_width=True)
