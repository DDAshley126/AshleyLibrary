import pandas as pd


def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    try:
        df = my_numbers.sort_values('num',ascending=False).drop_duplicates(subset='num',keep=False)
        return pd.DataFrame({'num': [df.iat[0,0]]})
    except:
        return pd.DataFrame({'num': [None]})















