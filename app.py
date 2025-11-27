import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

from components.sidebar import render_sidebar
from components.metrics import render_current_rates, render_metrics_cards, render_comparative_table
from components.charts import render_temporal_chart, render_correlation_heatmap
from components.analysis import render_advanced_analysis
from services.api_client import get_exchange_data
from utils.helpers import calculate_metrics

# Bibliotecas para download
import io
import zipfile
import json

st.set_page_config(
    page_title="Dashboard de Análise Cambial",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Funções para download ---
def export_zip(df_data, metrics_data):
    """Cria um ZIP com histórico e métricas"""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zip_file:
        zip_file.writestr("historico.csv", df_data.to_csv(index=False))
        zip_file.writestr("metricas.json", json.dumps(metrics_data, indent=4, ensure_ascii=False))

    st.download_button(
        label="📦 Baixar Pacote de Dados (ZIP)",
        data=buffer.getvalue(),
        file_name="dashboard.zip",
        mime="application/zip"
    )

# --- Main ---
def main():
    st.title("💹 Dashboard de Análise Cambial")

    try:
        # Sidebar
        selected_currencies, time_period = render_sidebar()
        if not selected_currencies:
            st.warning("⚠️ Selecione pelo menos uma moeda para análise")
            st.stop()

        # Carregar dados
        with st.spinner("🔄 Carregando dados..."):
            df_data = get_exchange_data(selected_currencies, time_period)

        if df_data.empty:
            st.error("❌ Não foi possível carregar dados")
            st.stop()

        # ✅ Cotações atuais (BC / PTAX)
        render_current_rates(selected_currencies)

        # Calcular métricas
        metrics_data = calculate_metrics(df_data, selected_currencies)
        if not metrics_data:
            st.error("❌ Não foi possível calcular métricas")
            st.stop()

        # Exibir componentes
        render_metrics_cards(metrics_data, selected_currencies)
        render_temporal_chart(df_data, selected_currencies)
        render_advanced_analysis(metrics_data, df_data, selected_currencies)
        render_comparative_table(metrics_data, selected_currencies)

        if len(selected_currencies) > 1:
            render_correlation_heatmap(df_data, selected_currencies)

        # --- Botões de download ---
        st.markdown("---")
        st.subheader("💾 Exportar Dashboard")
        export_zip(df_data, metrics_data)
        st.info("📌 Screenshot do dashboard só pode ser feita manualmente ou usando ferramentas externas.")

    except Exception as e:
        st.error(f"❌ Erro no dashboard: {str(e)}")

if __name__ == "__main__":
    main()