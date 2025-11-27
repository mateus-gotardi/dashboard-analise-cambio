import streamlit as st
from services.api_client import get_single_currency_rate
from utils.helpers import format_currency_value

def render_sidebar():
    """Renderiza a sidebar e retorna moedas e período selecionados"""
    
    with st.sidebar:
        st.header("🎛️ Controles")
        
        available_currencies = {
            "USD": "Dólar Americano",
            "EUR": "Euro", 
            "GBP": "Libra Esterlina", 
            "JPY": "Iene Japonês",
            "BRL": "Real Brasileiro"
        }
        
        selected_currencies = st.multiselect(
            "Selecione as moedas:",
            options=list(available_currencies.keys()),
            default=["USD", "EUR", "BRL"],
            format_func=lambda x: f"{x} - {available_currencies[x]}"
        )
        
        st.subheader("📅 Período")
        time_period = st.selectbox(
            "Período de análise:",
            options=["7 dias", "30 dias", "90 dias", "6 meses"],
            index=2
        )
        
        # Calculadora Rápida
        st.markdown("---")
        st.markdown("**💱 Calculadora Rápida**")
        
        col1, col2 = st.columns(2)
        with col1:
            amount = st.number_input("Valor", min_value=0.0, value=100.0, step=10.0)
        with col2:
            from_currency = st.selectbox(
                "De:", 
                options=["USD", "EUR", "GBP", "JPY"],
                index=0
            )
        
        if st.button("🔄 Calcular", use_container_width=True, type="primary"):
            rate = get_single_currency_rate(from_currency)
            if rate:
                converted_amount = amount * rate
                st.success(f"**{amount:.0f} {from_currency} = {format_currency_value(converted_amount, 'BRL')}**")
        
        st.markdown("---")
        if st.button("🔄 Atualizar Dashboard", use_container_width=True):
            st.cache_data.clear()           # limpa cache das funções cacheadas
            st.experimental_rerun()         # força recarregar a página

        return selected_currencies, time_period