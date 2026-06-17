# Importações necessárias
import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
# Define o título da página, o ícone e o layout. 'wide' aproveita melhor o espaço da tela.
st.set_page_config(
    page_title="Análise de Sentimentos de Reviews",
    page_icon="📊",
    layout="wide"
)

# --- Carregamento dos Dados ---
# @st.cache_data é um "decorador" que otimiza a performance.
# Ele diz ao Streamlit para carregar os dados apenas uma vez e mantê-los em cache,
# em vez de recarregá-los toda vez que o usuário interage com um filtro.
@st.cache_data
def load_data():
    """
    Função para carregar o DataFrame final com a análise de sentimento.
    """
    filepath = 'data/ml_reviews_final.csv'
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        st.error(f"ERRO: O arquivo '{filepath}' não foi encontrado.")
        st.info("Por favor, execute os notebooks das fases anteriores para gerar o arquivo final.")
        return None

# Carrega os dados usando a função cacheada
df = load_data()

# --- Título e Descrição ---
st.title("📊 Dashboard de Análise de Sentimentos")
st.markdown("Este dashboard interativo apresenta a análise de sentimentos dos reviews de produtos coletados do Mercado Livre.")

# --- Se os dados não foram carregados, para a execução aqui ---
if df is None:
    st.stop()

# --- Barra Lateral (Sidebar) com Filtros ---
st.sidebar.header("Filtros")

# Filtro multi-seleção para o sentimento
sentiments_to_filter = st.sidebar.multiselect(
    "Selecione o Sentimento:",
    options=df['sentiment'].unique(),
    default=df['sentiment'].unique() # Por padrão, todos os sentimentos são selecionados
)

# Filtra o DataFrame com base na seleção do usuário
filtered_df = df[df['sentiment'].isin(sentiments_to_filter)]

# --- Corpo Principal do Dashboard ---

# 1. Métricas Principais (KPIs)
st.header("Visão Geral")

# Divide o espaço em 3 colunas
col1, col2, col3 = st.columns(3)

# KPI 1: Total de Reviews
total_reviews = len(filtered_df)
col1.metric("Total de Reviews", total_reviews)

# KPI 2: Sentimento Médio (Compound)
avg_sentiment = filtered_df['compound'].mean()
col2.metric("Sentimento Médio (Compound)", f"{avg_sentiment:.2f}")

# KPI 3: Distribuição de Sentimentos (exibindo o mais comum)
most_common_sentiment = filtered_df['sentiment'].mode()[0]
col3.metric("Sentimento Predominante", most_common_sentiment)


st.markdown("---") # Linha divisória

# 2. Visualizações de Dados
st.header("Distribuição dos Sentimentos")

# Divide o espaço em 2 colunas para os gráficos
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    # Gráfico de Pizza com a contagem de cada sentimento
    sentiment_counts = filtered_df['sentiment'].value_counts()
    fig_pie = px.pie(
        sentiment_counts,
        values=sentiment_counts.values,
        names=sentiment_counts.index,
        title="Distribuição Percentual de Sentimentos",
        color=sentiment_counts.index,
        color_discrete_map={'Positivo':'lightgreen', 'Negativo':'#ff6961', 'Neutro':'lightgrey'}
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col_chart2:
    # Gráfico de Barras com a contagem de cada sentimento
    fig_bar = px.bar(
        sentiment_counts,
        x=sentiment_counts.index,
        y=sentiment_counts.values,
        title="Contagem Absoluta de Sentimentos",
        labels={'x': 'Sentimento', 'y': 'Número de Reviews'},
        color=sentiment_counts.index,
        color_discrete_map={'Positivo':'lightgreen', 'Negativo':'#ff6961', 'Neutro':'lightgrey'}
    )
    st.plotly_chart(fig_bar, use_container_width=True)


# 3. Tabela de Dados Detalhada
st.header("Explore os Reviews")
st.info("Veja abaixo os reviews filtrados. Você pode ordenar as colunas clicando no cabeçalho.")
st.dataframe(filtered_df[['title', 'text', 'sentiment', 'compound']], height=400, use_container_width=True)