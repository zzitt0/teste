# # Este programa fará a análise exploratória dos dados do arquivo 'dados_academicos_2.csv' e gerará gráficos para visualização dos dados.
# # O arquivo 'dados_academicos_2.csv' deve estar na mesma pasta que este script.
# # Será utilizado o framework Streamlit para criar uma interface web para visualização dos dados.

# # Importando as bibliotecas necessárias
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import streamlit as st

# # st.set_page_config(layout="wide")

# # Carregando o arquivo de dados
# df = pd.read_csv('dados_academicos_2.csv')

# # Criando uma lista com as colunas que possuem variáveis numericas
# colunas_numericas = ['N_REDACAO', 'N_MATEMATICA', 'N_FISICA', 'N_PORTUGUES', 'N_BIOLOGIA', 'IDADE', 'ALTURA']

# # Título do aplicativo
# st.title('Análise Exploratória de Dados Acadêmicos')

# # Gráficos de distribuição para variáveis numéricas
# st.subheader('Distribuição das Variáveis Numéricas')

# # Incluindo um slider para determinar o numero de bins

# num_bins = st.slider('Número de bins para o histograma', min_value=5, max_value=50, value=30)
# # Gráfico de distribuição para cada variável numérica
# for col in colunas_numericas:
# plt.figure(figsize=(10, 5))
# sns.histplot(df[col], bins=num_bins, kde=True, color='blue')
# plt.title(f'Distribuição de {col}', fontsize=16)
# plt.xlabel(col, fontsize=14)
# plt.ylabel('Frequência', fontsize=14)
# st.pyplot(plt) # Exibe o gráfico no Streamlit
# # plt.clf() # Limpa a figura para o próximo gráfico

#-----------------------------------------------------------------------------------------------------------------------------------------------------------#

# Este programa fará a análise exploratória dos dados do arquivo 'dados_academicos_2.csv' e gerará gráficos para visualização dos dados.
# O arquivo 'dados_academicos_2.csv' deve estar na mesma pasta que este script.
# Será utilizado o framework Streamlit para criar uma interface web para visualização dos dados.

# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# st.set_page_config(layout="wide")

# Carregando o arquivo de dados
df = pd.read_csv('dados_academicos_2.csv')

# Criando uma lista com as colunas que possuem variáveis numericas
colunas_numericas = ['N_REDACAO', 'N_MATEMATICA', 'N_FISICA', 'N_PORTUGUES', 'N_BIOLOGIA', 'IDADE', 'ALTURA']

# Título do aplicativo
st.title('Análise Exploratória de Dados Acadêmicos')

# Gráficos de distribuição para variáveis numéricas
st.subheader('Distribuição das Variáveis Numéricas')

# Gráfico de distribuição para cada variável numérica com um slider individual para o número de bins
for col in colunas_numericas:
    num_bins = st.slider(f'Número de bins para o histograma de {col}', min_value=5, max_value=50, value=30)
    plt.figure(figsize=(10, 5))
    sns.histplot(df[col], bins=num_bins, kde=True, color='blue')
    plt.title(f'Distribuição de {col}', fontsize=16)
    plt.xlabel(col, fontsize=14)
    plt.ylabel('Frequência', fontsize=14)
    st.pyplot(plt) # Exibe o gráfico no Streamlit
    # plt.clf() # Não é necessário limpar a figura aqui, pois cada gráfico é gerado em uma nova figura

col1, col2, col3 = st.columns([1, 2, 1,])

# Gráfico de barras para variáveis categóricas
with col1:
    st.subheader('Distribuição de SEXO')
    sexo_counts = df['SEXO'].value_counts()
    plt.figure(figsize=(6, 4))
    sns.barplot(x=sexo_counts.index, y=sexo_counts.values, hue=sexo_counts.index, palette='Set2', dodge=False)
    plt.title('Distribuição de SEXO', fontsize=16)
    plt.xlabel('SEXO', fontsize=14)
    plt.ylabel('Frequência', fontsize=14)
    st.pyplot(plt) # Exibe o gráfico no Streamlit
    plt.clf() # Limpa a figura para o próximo gráfico

with col2:
    st.subheader('Distribuição de ESPORTE_PREFERIDO')
    esporte_counts = df['ESPORTE_PREFERIDO'].value_counts()
    plt.figure(figsize=(6, 4))
    sns.barplot(x=esporte_counts.index, y=esporte_counts.values, hue=esporte_counts.index, palette='Paired', dodge=False)
    plt.title('Distribuição de ESPORTE_PREFERIDO', fontsize=16)
    plt.xlabel('ESPORTE_PREFERIDO', fontsize=14)
    plt.ylabel('Frequência', fontsize=14)
    plt.xticks(rotation=45)
    st.pyplot(plt) # Exibe o gráfico no Streamlit
    plt.clf() # Limpa a figura para o próximo gráfico
    
with col3:
    st.subheader('Distribuição de COR')
    cor_counts = df['COR'].value_counts()
    plt.figure(figsize=(6, 4))
    sns.barplot(x=cor_counts.index, y=cor_counts.values, hue=cor_counts.index, palette='Set2', dodge=False)
    plt.title('Distribuição de COR', fontsize=16)
    plt.xlabel('COR', fontsize=14)
    plt.ylabel('Frequência', fontsize=14)
    plt.xticks(rotation=45)
    st.pyplot(plt) # Exibe o gráfico no Streamlit
    plt.clf() # Limpa a figura para o próximo gráfico

# Seção para os gráficos de IDADE e ALTURA em duas colunas (sem sliders)
st.subheader('Distribuição de IDADE e ALTURA')
col_idade, col_altura = st.columns(2)

with col_idade:
    st.subheader('Distribuição de IDADE')
    plt.figure(figsize=(8, 4))
    sns.histplot(df['IDADE'], bins=30, kde=True, color='purple') # Defina um número fixo de bins
    plt.title('Distribuição de IDADE', fontsize=14)
    plt.xlabel('IDADE', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    st.pyplot(plt)
    plt.clf()

with col_altura:
    st.subheader('Distribuição de ALTURA')
    plt.figure(figsize=(8, 4))
    sns.histplot(df['ALTURA'], bins=30, kde=True, color='orange') # Defina um número fixo de bins
    plt.title('Distribuição de ALTURA', fontsize=14)
    plt.xlabel('ALTURA', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    st.pyplot(plt)
    plt.clf()
    
# # Plotando em um histograma a nota de matemática por sexo escolhida pelo usuário em um selectbox
st.subheader('Distribuição da Nota de Matemática por Sexo')
sexo_selecionado = st.selectbox('Selecione o sexo:', df['SEXO'].unique())

# # Plotando o histograma para o sexo selecionado
df_sexo = df[df['SEXO'] == sexo_selecionado]
plt.figure(figsize=(10, 5))
sns.histplot(df_sexo['N_MATEMATICA'], bins=num_bins, kde=True, color='blue')
plt.title(f'Distribuição de N_MATEMATICA para {sexo_selecionado}', fontsize=16)
plt.xlabel('N_MATEMATICA', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
st.pyplot(plt) # Exibe o gráfico no Streamlit
plt.clf() # Limpa a figura para o próximo gráfico

# Nova seção para a distribuição da nota de matemática por esporte favorito
st.subheader('Distribuição da Nota de Matemática por Esporte Favorito')
esporte_selecionado = st.selectbox('Selecione o esporte:', df['ESPORTE_PREFERIDO'].unique(), key='esporte_matematica')

# Plotando o histograma para o esporte selecionado
df_esporte = df[df['ESPORTE_PREFERIDO'] == esporte_selecionado]
plt.figure(figsize=(10, 5))
sns.histplot(df_esporte['N_MATEMATICA'], bins=30, kde=True, color='coral') # Use um número fixo de bins ou adicione um slider
plt.title(f'N_MATEMATICA para {esporte_selecionado}', fontsize=16)
plt.xlabel('N_MATEMATICA', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
st.pyplot(plt) # Exibe o gráfico no Streamlit
plt.clf() # Limpa a figura para o próximo gráfico

# # Criando dois seletores: um para a cor e outro para a disciplina
cor_selecionada = st.selectbox('Selecione a cor:', df['COR'].unique())
disciplina_selecionada = st.selectbox('Selecione a disciplina:', colunas_numericas[1:5], key='disciplina1')

# # Colocando um botao para gerar o gráfico
if st.button('Gerar Gráfico', type='primary'):
# Verifica se a disciplina selecionada é válida
    if disciplina_selecionada not in colunas_numericas[1:]:
        st.error('Selecione uma disciplina válida!')
    else:
# Plotando o histograma para a cor e disciplina selecionadas
        df_cor = df[df['COR'] == cor_selecionada]
        plt.figure(figsize=(10, 5))
        sns.histplot(df_cor[disciplina_selecionada], bins=num_bins, kde=True, color='blue')
        plt.title(f'Distribuição de {disciplina_selecionada} para {cor_selecionada}', fontsize=16)
        plt.xlabel(disciplina_selecionada, fontsize=14)
        plt.ylabel('Frequência', fontsize=14)
        st.pyplot(plt) # Exibe o gráfico no Streamlit

# Vendo as notas por esporte escolhido pelo usuário em um segmented_control
st.subheader('Notas por Esporte Preferido')
esporte_selecionado = st.segmented_control('Selecione o esporte:', df['ESPORTE_PREFERIDO'].unique(), selection_mode='single', default=df['ESPORTE_PREFERIDO'].unique()[0])
# Selecionando o sexo e a disciplina
disciplina_selecionada2 = st.selectbox('Selecione a disciplina:', colunas_numericas[1:5], key='disciplina2')

# Incluindo um radiobox para escolher o número de bins
numero_bins = st.radio('Número de bins para o histograma', (5, 10, 20, 30, 50), index=2)

# Plotando o gráfico de barras de notas dos alunos que praticam o esporte e a a disciplina selecionada
# Plotando o gráfico de barras para o esporte e disciplina selecionados
df_esporte = df[df['ESPORTE_PREFERIDO'] == esporte_selecionado]
plt.figure(figsize=(10, 5))
sns.histplot(df_esporte[disciplina_selecionada2], bins=numero_bins, kde=True, color='blue')
plt.title(f'Distribuição de {disciplina_selecionada2} para praticantes de {esporte_selecionado}', fontsize=16)
plt.xlabel(disciplina_selecionada2, fontsize=14)
plt.ylabel('Frequência', fontsize=14)
st.pyplot(plt)
plt.clf() # Limpa a figura para o próximo gráfico