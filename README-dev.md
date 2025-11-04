👨‍💻 Guia do Desenvolvedor: Análise de Moedas

Este documento fornece um mapa para a estrutura de código, convenções e o fluxo de trabalho para todos os membros da equipe.

1. Estrutura do Projeto

O projeto segue uma estrutura modular para separar as responsabilidades de coleta, armazenamento, processamento e interface.

projeto-dashboard-moedas/
├── data/
│ ├── raw/ # Dados brutos, como vieram da API.
│ └── processed/ # Dados limpos e prontos para o Streamlit (Ex: exchange_data.json).
├── src/
│ ├── api/ # Módulo de Conexão com a API (currency_api.py).
│ ├── database/ # Módulo da camada de abstração DB (db.py).
│ ├── processing/ # Módulo de Limpeza e Transformação (data_cleaner.py).
│ └── app.py # Arquivo principal do Streamlit (UI/Layout).
├── .gitignore
├── README.md # Documentação Geral (Entrega).
└── requirements.txt # Dependências Python.

2. Setup e Ambiente de Desenvolvimento

Siga os passos do README.md para criar e ativar sua venv.

Convenção:

Sempre trabalhe com a venv ativada.

Novas dependências devem ser adicionadas ao requirements.txt.

3. Arquitetura Chave: Camada DB (Abstração)

Adotamos uma camada de abstração para o banco de dados. O objetivo é que nenhum outro módulo (exceto db.py) saiba que estamos usando JSON/CSV para armazenamento.

Módulo: src/database/db.py

Classe: DB

Uso: Use a classe DB para ler e escrever dados processados.

from database.db import DB

# Inicializa (carrega o JSON)

db_instance = DB(filepath='data/processed/exchange_data.json')

# Lê todos os dados

df = db_instance.get_all()

4. Fluxo de Coleta e Processamento

Coleta: O src/api/currency_api.py é responsável por fazer a requisição HTTP e obter os dados brutos da API.

Limpeza: O src/processing/data_cleaner.py recebe os dados brutos, aplica a limpeza (conversão de tipos, tratamento de nulos, criação de métricas) e os transforma em um formato uniforme (Ex: DataFrame Pandas).

Armazenamento: O módulo de limpeza/coleta deve chamar db.insert() e db.save() para persistir os dados processados em data/processed/exchange_data.json.

Dashboard: O src/app.py deve sempre iniciar lendo os dados processados da camada DB.

5. Análise Exploratória e Testes

Use o analysis_notebook.ipynb para:

Testar a conexão da API.

Desenvolver e validar a lógica de limpeza de dados.

Criar protótipos de gráficos antes de implementá-los no Streamlit.

6. Convenções de Código

Tipagem: Use tipagem de função (def minha_funcao(arg: str) -> bool:) sempre que possível.

Comentários: Comente funções complexas e seções não triviais.

Importações: Mantenha as importações limpas e organizadas no topo de cada arquivo.

Log: [PREENCHER: Defina uma convenção de logging simples, se aplicável.]
