import streamlit as st
import pandas as pd
import warnings
import io
import zipfile
import json

# Importações dos módulos locais
from components.sidebar import render_sidebar
from components.metrics import render_current_rates, render_metrics_cards, render_comparative_table
from components.charts import render_temporal_chart, render_correlation_heatmap
from components.analysis import render_advanced_analysis
from services.api_client import get_exchange_data
from utils.helpers import calculate_metrics

# Configuração da Página
st.set_page_config(
    page_title="Dashboard de Análise Cambial",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Suprimir avisos desnecessários do Pandas
warnings.filterwarnings('ignore')

# --- Função para Carregar CSS ---
def local_css(file_name):
    """Carrega o arquivo CSS local para estilizar o dashboard"""
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"Arquivo de estilo não encontrado: {file_name}. Verifique se 'styles.css' está na raiz.")

# --- Função para Exportação ---
def export_zip(df_data, metrics_data):
    """Cria um ZIP com histórico (CSV) e métricas (JSON) para download"""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zip_file:
        # Salva o CSV
        zip_file.writestr("historico_cotacoes.csv", df_data.to_csv(index=False))
        # Salva o JSON com caracteres especiais (UTF-8)
        zip_file.writestr("metricas_analise.json", json.dumps(metrics_data, indent=4, ensure_ascii=False))

    st.download_button(
        label="📦 Baixar Pacote de Dados (ZIP)",
        data=buffer.getvalue(),
        file_name="dashboard_cambial.zip",
        mime="application/zip",
        use_container_width=True
    )

# --- Função Principal ---
def main():
    # 1. Carregar Estilos
    local_css("styles.css")
    
    st.markdown('<h1 class="main-header">💹 Dashboard de Análise Cambial</h1>', unsafe_allow_html=True)

    try:
        # 2. Renderizar Sidebar e obter filtros
        selected_currencies, time_period = render_sidebar()
        
        if not selected_currencies:
            st.warning("⚠️ Selecione pelo menos uma moeda na barra lateral para iniciar a análise.")
            st.stop()

        # 3. Carregar Dados da API
        with st.spinner("🔄 Conectando à API e processando dados..."):
            df_data = get_exchange_data(selected_currencies, time_period)

        if df_data.empty:
            st.error("❌ Não foi possível carregar os dados. Verifique sua conexão com a internet ou a disponibilidade da AwesomeAPI.")
            st.stop()

        # 4. Exibir Cotações Atuais
        render_current_rates(selected_currencies)

        # 5. Calcular Métricas
        metrics_data = calculate_metrics(df_data, selected_currencies)
        if not metrics_data:
            st.error("❌ Erro ao calcular métricas financeiras.")
            st.stop()

        # 6. Renderizar Componentes Visuais
        st.markdown("---")
        render_metrics_cards(metrics_data, selected_currencies)
        
        render_temporal_chart(df_data, selected_currencies)
        
        # Seção de Análise Avançada
        render_advanced_analysis(metrics_data, df_data, selected_currencies)
        
        # Tabela Comparativa
        render_comparative_table(metrics_data, selected_currencies)

        # Heatmap (apenas se houver mais de 1 moeda)
        if len(selected_currencies) > 1:
            render_correlation_heatmap(df_data, selected_currencies)

        # 7. Área de Download
        st.markdown("---")
        st.subheader("💾 Exportar Dados")
        col_export, _ = st.columns([1, 2])
        with col_export:
            export_zip(df_data, metrics_data)
        
        st.caption("Nota: Os dados são fornecidos pela AwesomeAPI e podem apresentar atrasos em relação ao mercado oficial.")

    except Exception as e:
        st.error(f"❌ Ocorreu um erro inesperado: {str(e)}")
        # Em produção, você pode adicionar logs aqui

if __name__ == "__main__":
    main()