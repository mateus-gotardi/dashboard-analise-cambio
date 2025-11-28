# 💹 Dashboard de Análise Cambial

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)

## 📝 Sobre o Projeto

Este é um dashboard interativo desenvolvido em Python para monitoramento e análise de tendências de moedas estrangeiras em relação ao Real Brasileiro (BRL).

O sistema consome dados da **AwesomeAPI** para fornecer cotações em tempo real, visualização histórica interativa, cálculo de volatilidade e matrizes de correlação, auxiliando na tomada de decisão rápida sobre câmbio.

🔗 **Repositório:** [https://github.com/mateus-gotardi/dashboard-analise-cambio](https://github.com/mateus-gotardi/dashboard-analise-cambio)

---

## 🚀 Funcionalidades Principais

- **Monitoramento em Tempo Real:** Cotações atualizadas de USD, EUR, GBP e JPY.
- **Gráficos Interativos:**
  - Evolução temporal (linhas) com janelas de 7 a 180 dias.
  - Heatmap de correlação para identificar movimentos conjuntos de moedas.
- **Métricas Financeiras:** Cálculo automático de volatilidade anualizada e variações percentuais.
- **Calculadora de Câmbio:** Ferramenta integrada para conversão rápida de valores.
- **Exportação de Dados:** Download de histórico tratado em CSV e métricas em JSON.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Streamlit** (Frontend e Interface)
- **Pandas** (Processamento de Dados)
- **Plotly** (Visualização de Dados)
- **Requests** (Integração com API REST)

---

## 📂 Estrutura do Projeto

```text
dashboard-analise-cambio/
│
├── app.py                  # Aplicação Principal (Entry point)
├── styles.css              # Estilização visual personalizada
├── requirements.txt        # Lista de dependências do projeto
├── README.md               # Documentação
│
├── components/             # Módulos de Interface (UI)
│   ├── analysis.py         # Seção de análises avançadas
│   ├── charts.py           # Renderização de gráficos
│   ├── metrics.py          # Cards de KPIs e tabelas
│   └── sidebar.py          # Barra lateral e filtros
│
├── services/               # Camada de Dados
│   └── api_client.py       # Conexão com a AwesomeAPI
│
└── utils/                  # Funções Auxiliares
    └── helpers.py          # Cálculos matemáticos e formatação

---

## ⚙️ Como Executar Localmente
Siga os passos abaixo para configurar e rodar o projeto na sua máquina:

1. Clonar o repositório
bash
git clone https://github.com/mateus-gotardi/dashboard-analise-cambio.git
cd dashboard-analise-cambio
2. Criar um ambiente virtual (Recomendado)
Isso isola as dependências do projeto do seu sistema principal.

No Windows:

bash
python -m venv venv
.\venv\Scripts\activate
No Linux ou Mac:

bash
python3 -m venv venv
source venv/bin/activate
3. Instalar as dependências
bash
pip install -r requirements.txt
4. Executar o Dashboard
bash
streamlit run app.py
O dashboard abrirá automaticamente no seu navegador padrão no endereço: http://localhost:8501.

Desenvolvido por Mateus Gotardi, Giovanna Durbano, Helena Koller, Marcele Caroline e Mateus Dani