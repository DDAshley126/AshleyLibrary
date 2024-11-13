import pandas as pd


def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(users, rides, left_on='id', right_on='user_id', how='left', suffixes=('', '_y')).groupby(by=['id', 'name']).sum().reset_index().rename(columns={'distance':'travelled_distance'}).sort_values(by=['travelled_distance','name'],ascending=[False,True])
    df.fillna(0, inplace=True)
    return df[['name', 'travelled_distance']]








