import pandas as pd


def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    data = activity.groupby(by='player_id')[['event_date']].min()
    data['second_login'] = data['event_date'] + pd.DateOffset(days=1)
    result = pd.merge(data.reset_index(),activity,left_on=['player_id', 'second_login'],right_on=['player_id','event_date'],how='right')
    fraction = round(len(result[~result['second_login'].isna()]['player_id'].unique())/len(activity['player_id'].unique()),2)
    return pd.DataFrame({'fraction': [fraction]})