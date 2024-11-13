import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)
    df = weather[((weather['recordDate'] - weather['recordDate'].shift(1)) == "1days") & (weather['temperature'] > weather['temperature'].shift(1))]
    return df[['id']]
