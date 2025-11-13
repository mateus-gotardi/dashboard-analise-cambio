💰 Dashboard Interativo: Análise e Conversão de Moedas

1. Título e Tema do Projeto

Título: Dashboard de Análise e Tendências de Câmbio Global
Tema: Análise de Moedas Estrangeiras e Impacto Econômico.

Justificativa da Escolha do Tema

A flutuação das moedas tem um impacto direto em investimentos, planejamento de viagens e decisões de negócios internacionais. Este dashboard se propõe a fornecer dados atualizados e análises históricas para informar o público ou decisores sobre as principais tendências cambiais.

(Esta seção precisa ser refinada com o grupo para refletir o foco exato, como moedas Latam vs. Moedas G7, etc.)

2. Fonte da API de Dados

Utilizaremos uma API pública de cotação para garantir dados em tempo real e históricos.

API de Dados Utilizada: Awesome API
Descrição dos Dados: Coletaremos cotações diárias/horárias de [PREENCHER: Ex: Dólar Americano (USD), Euro (EUR), Iene Japonês (JPY)] contra o Real Brasileiro (BRL) e armazenaremos dados históricos para análise de tendências.

3. Perguntas-Chave a Serem Respondidas

O Dashboard se propõe a responder as seguintes questões relevantes:

[PREENCHER: Pergunta Chave 1 (Ex: Qual foi a variação percentual das moedas X e Y nos últimos 90 dias?)]

[PREENCHER: Pergunta Chave 2 (Ex: Quais são os pontos de resistência e suporte para a moeda X?)]

[PREENCHER: Pergunta Chave 3 (Ex: Como o preço da moeda X se compara à média histórica de 6 meses?)]

4. Tecnologias e Requisitos

Interface: Streamlit

Linguagem: Python

Pacotes Principais: Streamlit, Pandas, Requests, etc. (detalhados em requirements.txt)

5. Instruções de Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto em sua máquina:

5.1. Criar e Ativar o Ambiente Virtual (VENV)

Criação: Na pasta raiz do projeto:

python3 -m venv venv

Ativação:

Linux/macOS: source venv/bin/activate

Windows (PowerShell): .\venv\Scripts\Activate.ps1

5.2. Instalar Dependências

Com a VENV ativa:

pip install -r requirements.txt

5.3. Executar o Dashboard

Execute o Streamlit a partir da pasta raiz do projeto:

streamlit run src/app.py

O dashboard será aberto automaticamente no seu navegador em http://localhost:8501.

6. Capturas de Tela do Dashboard

[PREENCHER: Inserir capturas de tela aqui, explicando o contexto de cada visualização.]
