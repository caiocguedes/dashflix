import plotly.express as px
import pandas as pd

#df_netflix_titles = pd.read_csv('data/df_netflix_titles.csv')

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
    fig.update_traces(marker_color='#A7C7E7')
    return fig

def genres_dropdown(df):
    df_netflix_genre = df.copy(deep=True)
    df_netflix_genre.dropna(subset='listed_in', inplace=True)
    df_netflix_genre['listed_in'] = df_netflix_genre['listed_in'].apply(lambda x: str(x))
    df_netflix_genre['listed_in'] = df_netflix_genre['listed_in'].apply(lambda x: x.split(','))
    df_netflix_genre_exploded = df_netflix_genre.explode(column='listed_in')
    df_netflix_genre_exploded['listed_in'] = df_netflix_genre_exploded['listed_in'].apply(lambda x: x.strip())
    df_netflix_genre_exploded['listed_in'] = df_netflix_genre_exploded['listed_in'].apply(lambda x: x.replace('[','').replace(']','').replace("' ","").replace("'","").replace('" ','').replace('"',''))
    
    return df_netflix_genre_exploded['listed_in'].unique()

def filter_genres(row, filter_values):
    # Check if any of the filter values are in the list of genres
    return filter_values in row

