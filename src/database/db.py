# src/database/db.py

import json
import os
from typing import Dict, Any, List

class DB:
    """
    Classe de abstração de banco de dados (Repository Pattern).
    Inicialmente, usa arquivos JSON para persistência local,
    facilitando a migração futura para um DB real (SQLite, NoSQL, etc.).
    """

    def __init__(self, filepath: str = 'data/processed/exchange_data.json'):
        """
        Inicializa a classe e define o caminho do arquivo de armazenamento.
        """
        self.filepath = filepath
        self.data: List[Dict[str, Any]] = self._load_data()
        print(f"DB inicializado. Carregou {len(self.data)} registros de {self.filepath}")

    def _load_data(self) -> List[Dict[str, Any]]:
        """Carrega os dados do arquivo JSON."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r', encoding='utf-8') as f:
                    # Garantindo que o arquivo não está vazio ou corrompido
                    content = f.read()
                    return json.loads(content) if content else []
            except json.JSONDecodeError:
                print(f"Aviso: Arquivo {self.filepath} corrompido ou JSON inválido. Reiniciando com dados vazios.")
                return []
        return []

    def _save_data(self) -> None:
        """Salva os dados atuais em memória para o arquivo JSON."""
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4)
        print(f"Dados salvos em {self.filepath}.")

    def insert(self, record: Dict[str, Any]) -> None:
        """Insere um novo registro de dados de conversão."""
        self.data.append(record)
        self._save_data()

    def get_all(self) -> List[Dict[str, Any]]:
        """Retorna todos os registros armazenados."""
        return self.data

    # Outras funções CRUD (update, delete) podem ser adicionadas futuramente.
