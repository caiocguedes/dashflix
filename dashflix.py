import streamlit as st
import pandas as pd
from graph_functions import *
from streamlit_navigation_bar import st_navbar

df = pd.read_csv('data/df_netflix_titles.csv')

navbar = ["Github", "Streamlit Docs"]
urls = {"Github": "https://github.com/caiocguedes/dashflix", "Streamlit Docs": "https://streamlit.io/"}

st.set_page_config(
    page_title="Dashflix",
    page_icon="images/dashflix.png"
)

page = st_navbar(
        navbar,
        logo_path='images/dashflix.svg',
        urls=urls
)

st.image('images/dashflix.png')


with st.container():
         st.markdown("<h1 style='text-align: center;'>O dashboard da sua Netflix!</h1>", unsafe_allow_html=True)
         st.markdown("<h4>Lista dos 20 países que mais lançaram filmes - por gênero</h4>", unsafe_allow_html=True)
         sel_genero = st.selectbox(
            label="Selecione o gênero",
            options=genres_dropdown(df),
            index=0
            )
         
         filtered_df = df[df['listed_in'].apply(lambda x: filter_genres(x, sel_genero))]
         
         st.plotly_chart(countries_graph(filtered_df), use_container_width=True)

st.divider()

col1, col2 = st.columns(2)
col1.markdown("![Alt Text](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXliZGUwMmwxejdxcjdsd3UweXRmODR6Z2RxbXlncThiNGY4cG9hNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1vRCeaHbgATwA/giphy.gif)")
col2.markdown("![Alt Text](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTFhZHpmdzB1NmpuYjh4NmdlZG04ZDVhc3dzNGd3NTVwcnU3ZzFvMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CU8abIBThDh09NUg2a/giphy-downsized-large.gif)")
st.caption("<p align='center'>(Sim, sabemos que Game of Thrones é da HBO)</p>", unsafe_allow_html=True)
st.divider()

with st.container():
    choice = st.radio("Qual tipo de análise de notas do IMDB você deseja visualizar?", ["Boxplot com distribuição das notas por ano de lançamento", "Histograma das notas"])
    with st.container():
        years_list = set(df['release_year'].to_list())
        min_year, max_year = st.select_slider('Selecione o intervalo (anos) desejado:', options=years_list, value=[1990, 2000])
        if "Boxplot" in choice:
            st.markdown('<h4>Distribuição das Notas dos Filmes com Boxplot</h4>', unsafe_allow_html=True)
            st.plotly_chart(boxplot_graph(df, min_year, max_year), use_container_width=True)
        else:
            st.markdown('<h4>Histograma das notas</h4>', unsafe_allow_html=True)
            st.plotly_chart(histogram(df, min_year, max_year), use_container_width=True)