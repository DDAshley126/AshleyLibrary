import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    d = pd.to_datetime(['2019-07-27']*activity.shape[0]) - activity['activity_date']
    df = activity[(d < '30days') & (d >= '0days')]
    df = df.groupby(by='activity_date')[['user_id']].nunique().reset_index().rename(columns={'activity_date':'day','user_id':'active_users'})
    return df











