import requests
import pandas as pd
from typing import List, Dict, Any

class CurrencyAPI:
    """
    Classe responsável por interagir com a API de dados de moedas.
    Nesta fase, apenas define a estrutura para a coleta de dados.
    """
    
    def __init__(self, api_url: str = "https://api.exchangerate.com/..."):
        """Inicializa a classe com a URL base da API (placeholder)."""
        self.api_url = api_url
        print(f"CurrencyAPI inicializada para URL: {self.api_url}")

    def fetch_data(self, base_currency: str, target_currencies: List[str], start_date: str, end_date: str) -> Dict[str, Any]:
        """
        Método placeholder para buscar dados históricos da API.
        Ainda não implementa a lógica real de chamada HTTP.
        """
        print(f"Buscando dados para {base_currency} de {start_date} a {end_date}...")
        # Simulação de retorno de dados vazios
        return {"status": "success", "data": []}

    def get_available_currencies(self) -> List[str]:
        """Método placeholder para obter a lista de moedas suportadas."""
        return ["USD", "EUR", "BRL", "JPY"]

# Exemplo de como esta classe seria usada:
# api = CurrencyAPI()
# data = api.fetch_data("USD", ["BRL"], "2024-01-01", "2024-12-31")
# print(data)
