import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    df = logs[(logs['num'] == logs['num'].shift(1)) & (logs['num'] == logs['num'].shift(2))].rename(columns={'num':'ConsecutiveNums'})
    return df.drop_duplicates(subset='ConsecutiveNums')[['ConsecutiveNums']]
