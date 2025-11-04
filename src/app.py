# src/app.py

import streamlit as st
import pandas as pd
from typing import List, Dict, Any

# =========================================================================
# 1. IMPORTAÇÃO DOS MÓDULOS DO PROJETO
# Os imports são feitos desta forma para garantir a modularidade
# e simular o funcionamento de um pacote Python.
# Nota: O ponto inicial ('.') indica um import relativo dentro do pacote 'src'.
# Se houver problemas, tente rodar no terminal: streamlit run src/app.py
# =========================================================================

# Importando classes shell criadas
from api.currency_api import CurrencyAPI
from database.db import DB
from processing.data_cleaner import DataCleaner

# =========================================================================
# 2. CONFIGURAÇÃO DA PÁGINA STREAMLIT
# =========================================================================
st.set_page_config(
    page_title="Dashboard de Análise de Moedas",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================================
# 3. SETUP INICIAL DO PROJETO (Instanciação dos Módulos)
# =========================================================================

@st.cache_resource
def initialize_project_modules():
    """
    Função para inicializar as classes do projeto uma única vez.
    O decorador st.cache_resource garante que este setup não é reexecutado
    a cada interação do Streamlit.
    """
    try:
        # 3.1. Inicializa a abstração de Banco de Dados (DB com JSON)
        db_instance = DB()
        st.success("✔ Módulo DB (JSON) inicializado com sucesso.")

        # 3.2. Inicializa a API de Moedas
        api_instance = CurrencyAPI(api_url="Placeholder API URL")
        st.success("✔ Módulo CurrencyAPI inicializado com sucesso.")
        
        # 3.3. Inicializa o DataCleaner (passando dados vazios/placeholder)
        # Na fase real, os dados seriam lidos do DB e passados aqui.
        cleaner_instance = DataCleaner(raw_data=[]) 
        st.success("✔ Módulo DataCleaner inicializado com sucesso.")

        return db_instance, api_instance, cleaner_instance

    except Exception as e:
        st.error(f"❌ Erro ao inicializar módulos: {e}")
        return None, None, None

db, currency_api, data_cleaner = initialize_project_modules()


# =========================================================================
# 4. LAYOUT E CONTEÚDO DO DASHBOARD
# =========================================================================

def main_dashboard():
    """Função principal que renderiza a interface do dashboard."""
    
    # Título principal
    st.title("💰 Dashboard Interativo de Análise de Moedas")
    st.caption("Protótipo Inicial | Estrutura de Módulos (API, DB, Processamento) Carregada.")

    if db is None:
        st.error("Não foi possível carregar os módulos. Verifique o console para detalhes.")
        return

    st.markdown("---")
    
    # 4.1. SIDEBAR (Requisito de Interatividade)
    with st.sidebar:
        st.header("⚙️ Configurações do Dashboard")
        
        # Exemplo de Elemento Interativo 1 (Slider)
        days_to_analyze = st.slider(
            "Período de Análise (Dias)",
            min_value=15, 
            max_value=365, 
            value=90,
            step=15
        )
        st.info(f"Análise configurada para os últimos **{days_to_analyze}** dias.")

        # Exemplo de Elemento Interativo 2 (Dropdown/Selectbox)
        available_currencies = currency_api.get_available_currencies()
        base_currency = st.selectbox(
            "Moeda Base para Conversão",
            options=available_currencies,
            index=available_currencies.index("USD") if "USD" in available_currencies else 0
        )
        st.info(f"Moeda Base selecionada: **{base_currency}**")

        st.markdown("---")
        st.subheader("Status do Setup")
        st.write(f"DB Records: {len(db.get_all())}")
        st.write(f"API URL: {currency_api.api_url}")
        
    # 4.2. CORPO PRINCIPAL DO DASHBOARD

    st.header("Hello World 👋")
    st.subheader("Bem-vindo ao Planejamento do Projeto de Ciência de Dados.")
    
    st.markdown("""
        Esta é a fase de **setup**. A estrutura de pastas e a modularização foram implementadas com sucesso!
        Os módulos `CurrencyAPI`, `DB` e `DataCleaner` estão carregados e prontos para receber a lógica de desenvolvimento.

        **Próximos Passos:**
        1.  Definir a API e as 3 Perguntas-Chave (Insights).
        2.  A equipe de Engenheiros de API pode começar a implementar o método `fetch_data` no módulo `currency_api.py`.
        3.  A equipe de Engenheiros de Dados pode começar a definir a lógica de `clean_and_transform` no módulo `data_cleaner.py`.
        4.  A equipe de Visualização pode começar a estruturar o layout do Streamlit com base nas perguntas-chave.
    """)
    
    st.markdown("---")
    st.subheader("Área para Visualizações (Em Desenvolvimento)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="KPI 1: Variação Média", value="N/A", delta="Em breve...")
        st.write("Gráfico de Tendência Histórica irá aqui.")
        
    with col2:
        st.metric(label="KPI 2: Moeda mais Volátil", value="N/A", delta="Em breve...")
        st.write("Gráfico de Dispersão/Comparação de Pares irá aqui.")

    with col3:
        st.metric(label="Registros no DB", value=str(len(db.get_all())) if db else "0")
        st.write("Elementos Interativos de Filtro estão na Barra Lateral.")
        
# Execução da função principal
if __name__ == '__main__':
    main_dashboard()
