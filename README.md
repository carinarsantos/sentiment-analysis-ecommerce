Análise de Sentimentos de Reviews de E-commerce com Streamlit

Descrição do Projeto
Este projeto realiza uma análise de sentimentos completa sobre reviews de produtos de um site de e-commerce (Mercado Livre). Os dados são coletados via web scraping, processados e limpos, e um modelo de Processamento de Linguagem Natural (PLN) é aplicado para classificar o sentimento de cada review. Os resultados são apresentados em um dashboard interativo construído com Streamlit, permitindo uma exploração visual e intuitiva dos dados.

Funcionalidades
Coleta de Dados: Script de web scraping para extrair reviews de páginas de produtos.

Processamento de Texto: Limpeza e pré-processamento de texto em português, incluindo remoção de stopwords e pontuação.

Análise de Sentimento: Classificação de cada review como Positivo, Negativo ou Neutro utilizando o modelo VADER após tradução.

Dashboard Interativo: Visualização dos dados com filtros por sentimento, métricas-chave e gráficos dinâmicos.

Exploração de Dados: Tabela interativa para ler e ordenar os reviews filtrados.

Acesso à Aplicação
Você pode acessar e interagir com o dashboard através deste link:
Link para o seu App Streamlit

Tecnologias Utilizadas
Este projeto foi construído utilizando as seguintes tecnologias e bibliotecas:

Coleta de Dados: requests, BeautifulSoup4

Processamento e Análise: Pandas, NLTK, googletrans, vaderSentiment

Visualização e Dashboard: Streamlit, Plotly Express, WordCloud, Seaborn, Matplotlib

Ambiente: Python 3.11, Jupyter Notebook, VS Code

Estrutura do Repositório

O projeto está organizado da seguinte forma:

├── data/
│   ├── ml_reviews_raw.csv
│   ├── ml_reviews_processed.csv
│   └── ml_reviews_final.csv
├── notebooks/
│   ├── 01-scraping.ipynb
│   ├── 02-text-preprocessing.ipynb
│   └── 03-EDA.ipynb
├── src/
│   └── (Opcional: scripts modulares se você os criou)
├── .venv/
├── .gitignore
├── app.py
├── README.md
└── requirements.txt

Como Executar o Projeto Localmente
Siga os passos abaixo para executar a aplicação na sua máquina.

Clone o repositório:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Crie e ative um ambiente virtual:

Bash

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt
Execute a aplicação Streamlit:

Bash

streamlit run app.py
A aplicação abrirá automaticamente no seu navegador.

Pipeline do Projeto
O projeto foi desenvolvido seguindo 4 fases principais:

Coleta de Dados: Extração de reviews utilizando requests e BeautifulSoup. O script foi projetado para ser robusto a falhas em campos individuais.

Limpeza e Pré-processamento: O texto dos reviews foi normalizado (minúsculas), limpo (remoção de pontuação) e otimizado para análise (remoção de stopwords) com NLTK.

Análise de Sentimento: Utilização do modelo VADER, aplicando-o ao texto traduzido para o inglês para obter scores de polaridade (positivo, negativo, neutro) e um score composto (compound).

Dashboard: Desenvolvimento de uma aplicação web com Streamlit para apresentar os resultados de forma visual e interativa, com KPIs, gráficos e filtros.

Desafios e Aprendizados
Um dos maiores desafios foi o diagnóstico de um LookupError persistente da biblioteca NLTK. Após múltiplas tentativas de depuração (verificação de ambientes, caminhos de instalação), foi descoberto que o arquivo de modelo pré-treinado (.pickle) para o tokenizador em português estava obsoleto e era incompatível com versões modernas do Python. A solução foi substituir o tokenizador por uma abordagem mais robusta (RegexpTokenizer), resolvendo o conflito e garantindo a execução do pipeline. Isso reforçou a importância de entender o funcionamento interno das bibliotecas e de não depender de pacotes de dados desatualizados.

Melhorias Futuras
Adicionar filtros por data no dashboard.

Implementar uma nuvem de palavras dinâmica que se atualiza com base nos filtros.

Substituir o modelo VADER por um modelo de Deep Learning (ex: BERTimbau) para obter uma classificação de sentimento mais precisa e contextual em português.

Autor
Ana Carina R. Santos

LinkedIn: https://www.linkedin.com/in/ana-carina-romualdo-dos-santos/

GitHub: https://github.com/carinarsantos

Streamlit: https://sentiment-analysis-ecommerce.streamlit.app/
Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
