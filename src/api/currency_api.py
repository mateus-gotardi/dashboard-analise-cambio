import requests
import pandas as pd
import json
from typing import List, Dict, Any

class CurrencyAPI:
    """
    Classe responsável por interagir com a API de dados de moedas.
    API ESCOLHIDA: API oficial do Banco Central do Brasil (BCB)
    documentação: 
     - https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/swagger-ui3#/ <-- O Swagger tem algumas rotas que ele cria a URL errada, mais util pra ter um overview do que como documentação
     - https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/recursos <-- aqui é mais fácil pq ele ja forma a URL certa
    
    base URL: https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata
    
    ** importante: A API do BCB recebe todas as datas no formato MM-DD-AAAA **
    endpoints principais para uso:
      /Moedas - retorna a lista de moedas suportadas
      /CotacaoMoedaPeriodo - retorna as cotações de uma moeda em um período específico
    https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda='EUR'&@dataInicial='10-01-2025'&@dataFinalCotacao='11-18-2025'&$top=100&$format=json&$select=paridadeCompra,paridadeVenda,cotacaoCompra,cotacaoVenda,dataHoraCotacao,tipoBoletim
    """
    
    def __init__(self, api_url: str = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata"):
        """Inicializa a classe com a URL base da API (placeholder)."""
        self.api_url = api_url
        print(f"CurrencyAPI inicializada para URL: {self.api_url}")

    def fetch_data(self, currency: str, start_date: str, end_date: str, page: int = 1, limit: int = 100) -> Dict[str, Any]:
        # verifica se o currency é suportado
        if(currency not in [c["simbolo"] for c in self.get_available_currencies()]):
            raise ValueError(f"Currency {currency} não suportada.")
        #verifica o formato das datas
        if(not self.validate_date_format(start_date) or not self.validate_date_format(end_date)):
            raise ValueError("Formato de data inválido. Use MM-DD-AAAA.")
        """
        chamada da rota /CotacaoMoedaPeriodo da API do BCB com os parametros recebidos.
        """
        print(f"Buscando dados para {currency} de {start_date} a {end_date}...")
        # Simulação de retorno de dados vazios
        url_path = f"{self.api_url}/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)"
        params = {
                    '@moeda': f"'{currency}'", 
                    '@dataInicial': f"'{start_date}'",
                    '@dataFinalCotacao': f"'{end_date}'",
                    '$top': limit,
                    '$skip': (page - 1) * limit,
                    '$format': 'json',
                    '$select': 'paridadeCompra,paridadeVenda,cotacaoCompra,cotacaoVenda,dataHoraCotacao,tipoBoletim'
                }
        try:
            response = requests.get(url_path, params=params, timeout=10)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            # Captura erros 4xx/5xx (erros na API)
            # Garante que response existe antes de acessar atributos
            status = getattr(http_err.response, 'status_code', 'N/A')
            url = getattr(http_err.response, 'url', url_path)
            text = getattr(http_err.response, 'text', '')
            print(f"Erro HTTP {status}: Falha na requisição. URL: {url}")
            print(f"Resposta do Servidor (parcial): {text[:400]}...")
            raise
        except requests.RequestException as e:
            print(f"Erro de Conexão Geral: {e}")
            raise
        response.encoding = 'utf-8'
        try:
            return response.json()
        except (ValueError, json.JSONDecodeError) as json_err:
            # Ocorre se o BCB retornou texto/HTML, JSON vazio, ou outro formato inesperado.
            print(f"Erro de Decodificação JSON: Conteúdo recebido não é JSON válido. URL: {response.url}")
            print(f"Status Code: {response.status_code}")
            print(f"Conteúdo Recebido (primeiros 1000 chars):\n{response.text[:1000]}\n---")
            # Re-raise com contexto para facilitar debug
            raise RuntimeError(f"Falha ao decodificar JSON (status {response.status_code}). Conteúdo foi impresso no stdout.") from json_err

    def get_available_currencies(self) -> List[Dict[str, str]]:
        """Essa Rota é fixa na API e não muda com frequencia,
        pra esse trabalho vamos deixar hardcoded.
        """
        return [
            {
                "simbolo": "AUD",
                "nomeFormatado": "Dólar australiano",
                "tipoMoeda": "B"
            },
            {
                "simbolo": "CAD",
                "nomeFormatado": "Dólar canadense",
                "tipoMoeda": "A"
            },
            {
                "simbolo": "CHF",
                "nomeFormatado": "Franco suíço",
                "tipoMoeda": "A"
            },
            {
                "simbolo": "DKK",
                "nomeFormatado": "Coroa dinamarquesa",
                "tipoMoeda": "A"
            },
            {
                "simbolo": "EUR",
                "nomeFormatado": "Euro",
                "tipoMoeda": "B"
            },
            {
                "simbolo": "GBP",
                "nomeFormatado": "Libra Esterlina",
                "tipoMoeda": "B"
            },
            {
                "simbolo": "JPY",
                "nomeFormatado": "Iene",
                "tipoMoeda": "A"
            },
            {
                "simbolo": "NOK",
                "nomeFormatado": "Coroa norueguesa",
                "tipoMoeda": "A"
            },
            {
                "simbolo": "SEK",
                "nomeFormatado": "Coroa sueca",
                "tipoMoeda": "A"
            },
            {
                "simbolo": "USD",
                "nomeFormatado": "Dólar dos Estados Unidos",
                "tipoMoeda": "A"
            }
        ]

    def validate_date_format(self, date_str: str) -> bool:
        """Valida se a data está no formato MM-DD-AAAA."""
        try:
            pd.to_datetime(date_str, format='%m-%d-%Y')
            return True
        except ValueError:
            return False
# Exemplo de como esta classe seria usada (executa apenas quando chamado como script):
if __name__ == "__main__":
    api = CurrencyAPI()
    try:
        dolar = api.fetch_data(currency="USD", start_date="01-01-2023", end_date="01-31-2023", page=1, limit=5)
        print(dolar)
    except Exception as e:
        print(f"Erro ao buscar dados no modo script: {e}")