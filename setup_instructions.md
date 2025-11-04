🛠️ Instruções de Setup do Ambiente Virtual (VENV)

Para garantir que seu projeto funcione de forma idêntica para todos os membros do grupo, siga os passos abaixo para criar e ativar o ambiente virtual e instalar o Jupyter.

Pré-requisito: Certifique-se de que o Python e o pip estão instalados em seu sistema.

Passo 1: Criar e Ativar o Ambiente Virtual

Execute o seguinte comando no terminal (na pasta raiz do projeto projeto-dashboard-moedas/):

Criar a VENV:

python3 -m venv venv

Ativar a VENV:

Linux/macOS:

source venv/bin/activate

Windows (PowerShell):

.\venv\Scripts\Activate

Você saberá que a venv está ativa quando o nome (venv) aparecer no início da linha de comando.

Passo 2: Instalar as Dependências

Com a venv ativa, instale as bibliotecas necessárias usando o arquivo requirements.txt que geramos.

pip install -r requirements.txt

Passo 3: Instalar o Jupyter Notebook

Você precisará do Jupyter e do ipykernel para usar o notebook com este ambiente virtual.

Instalar Jupyter:

pip install jupyter

Registrar a VENV no Jupyter (ipykernel):

Isso garante que o kernel do notebook use as bibliotecas instaladas na sua venv.

python -m ipykernel install --user --name=moedas_venv --display-name "Análise de Moedas (VENV)"

Passo 4: Abrir o Notebook

Agora você pode iniciar o servidor Jupyter e abrir o arquivo analysis_notebook.ipynb.

jupyter notebook

Seu navegador abrirá automaticamente. Navegue até o arquivo analysis_notebook.ipynb e selecione o kernel "Análise de Moedas (VENV)".

Lembre-se de desativar o ambiente quando terminar de trabalhar:

deactivate
