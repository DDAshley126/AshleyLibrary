import pandas as pd


def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(movie_rating, users, on='user_id', how='left')
    result1 = df.groupby('name')[['created_at']].apply(lambda x: x.count()).idxmax()[0]
    df1 = pd.merge(movie_rating, movies, on='movie_id', how='left')
    result2 = df1[(df1['created_at'] >= '2020-02-01') & (df['created_at'] < '2020-03-01')].groupby('title')[['rating']].mean().idxmax()[0]
    return pd.DataFrame({'results': [result1, result2]})