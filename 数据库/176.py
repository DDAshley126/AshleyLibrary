import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.drop_duplicates(subset='salary')
    if df.shape[0] >= 2:
        df = df.sort_values(by='salary', ascending=False).head(2).tail(1)
        return df[['salary']].rename(columns={'salary': 'SecondHighestSalary'})
    else:
        return pd.DataFrame({'SecondHighestSalary': [None]})


