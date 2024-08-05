import plotly.express as px
import numpy as np

#df_netflix_titles = pd.read_csv('data/df_netflix_titles.csv')

'''gráfico que lista os 20 países que mais lançaram filmes'''
def countries_graph(df_netflix_titles):
    df_exploded = df_netflix_titles.explode(column='country')
    df_exploded['country'] = df_exploded['country'].apply(lambda x: x.strip())
    df_filtered = df_exploded[df_exploded['country'] != '']
    df_grouped = df_filtered.groupby(['country']).size().sort_values(ascending=False)
    df_grouped

    df_netflix_country = df_grouped.rename_axis('country').reset_index(name='count').head(20)

    fig = px.bar(df_netflix_country, 
                x='count', 
                y='country', 
                labels={'country': '', 'count': ''},
                text_auto=True,
                height=600,
                width=800)
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    fig.update_xaxes(visible=False)
    fig.update_traces(marker_color='#E50914')
    return fig

'''widget com dropdown com lista dos gêneros contidos no dataframe'''
def genres_dropdown(df):
    df_netflix_genre = df.copy(deep=True)
    df_netflix_genre.dropna(subset='listed_in', inplace=True)
    df_netflix_genre['listed_in'] = df_netflix_genre['listed_in'].apply(lambda x: str(x))
    df_netflix_genre['listed_in'] = df_netflix_genre['listed_in'].apply(lambda x: x.split(','))
    df_netflix_genre_exploded = df_netflix_genre.explode(column='listed_in')
    df_netflix_genre_exploded['listed_in'] = df_netflix_genre_exploded['listed_in'].apply(lambda x: x.strip())
    df_netflix_genre_exploded['listed_in'] = df_netflix_genre_exploded['listed_in'].apply(lambda x: x.replace('[','').replace(']','').replace("' ","").replace("'","").replace('" ','').replace('"',''))
    list_genres = df_netflix_genre_exploded['listed_in'].unique()
    list_genres = np.append(list_genres, [''])
    list_genres.sort()
    return list_genres

'''filtro dos gêneros'''
def filter_genres(row, filter_values):
    # Check if any of the filter values are in the list of genres
    return filter_values in row

'''boxplot IMDB'''
def boxplot_graph(df, min_year, max_year):
    df_netflix_last_titles = df[(df["release_year"] >= min_year) & (df["release_year"] <= max_year)]

    fig = px.box(df_netflix_last_titles, 
                x='release_year', 
                y="rating_imdb", 
                color='type',
                width=700,
                title=None,
                color_discrete_sequence=['#E50914', 'darkblue'],
                labels={'release_year':'Ano de lançamento', 'rating_imdb':'Nota no IMDB', 'type':'Tipo'})
    return fig

'''histograma IMDB'''
def histogram(df, min_year, max_year):
    df_netflix_last_titles = df[(df["release_year"] >= min_year) & (df["release_year"] <= max_year)]

    fig = px.histogram(df_netflix_last_titles, 
                   x="rating_imdb", 
                   color='type',
                   labels={'rating_imdb':'Nota no IMDB', 'type':'Tipo'},
                   color_discrete_sequence=['#E50914', 'darkblue'],
                   width=700,
                   nbins=20, 
                   barmode='stack',
                   title=None)
    fig.data = fig.data[::-1]
    fig.layout.legend.traceorder = 'reversed'
    fig.update_yaxes(title='')
    fig.update_layout(bargap=0.1)
    return fig
