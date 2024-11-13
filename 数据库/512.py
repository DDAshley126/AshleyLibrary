import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    data = activity.groupby('player_id')[['event_date']].min().reset_index()
    return pd.merge(activity, data, on=['player_id', 'event_date'], how='inner')[['player_id', 'device_id']]
