# src/processing/data_cleaner.py

import pandas as pd
from typing import List, Dict, Any

class DataCleaner:
    """
    Classe responsável pela limpeza, transformação e agregação de dados.
    Esta classe aplica os requisitos de processamento de dados do projeto.
    """

    def __init__(self, raw_data: List[Dict[str, Any]]):
        """Inicializa com a lista de dados brutos para processamento."""
        self.raw_data = raw_data
        print(f"DataCleaner inicializado com {len(raw_data)} itens para processar.")
        self.df: pd.DataFrame = pd.DataFrame()

    def load_to_dataframe(self) -> pd.DataFrame:
        """Converte a lista de dicionários brutos em um DataFrame do Pandas."""
        if not self.raw_data:
            print("Nenhum dado bruto para carregar.")
            return pd.DataFrame()
            
        self.df = pd.DataFrame(self.raw_data)
        return self.df

    def clean_and_transform(self) -> pd.DataFrame:
        """
        Aplica as técnicas de limpeza (tratamento de nulos, tipos)
        e transformações (criação de colunas de métricas/KPIs).
        """
        df = self.load_to_dataframe()
        
        if df.empty:
            return df
            
        # Exemplo de limpeza e transformação (substituir pela lógica real)
        # 1. Filtragem de dados inválidos
        # 2. Conversão de tipo de dados (ex: 'data' para datetime)
        # 3. Criação de nova coluna (ex: Variação Diária)
        
        print(f"DataFrame processado com {len(df.columns)} colunas.")
        return df

    def get_kpis(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Calcula as métricas chave (KPIs) para exibição no dashboard."""
        # Esta função será implementada na fase de Análise
        return {"total_registros": len(df), "ultima_atualizacao": "N/A"}
