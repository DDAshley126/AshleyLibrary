import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee.drop_duplicates(subset='salary')
    if df.shape[0] >= N:
        df = df.sort_values(by='salary', ascending=False).head(N).tail(1)
        return df[['salary']].rename(columns={'salary': 'getNthHighestSalary({})'.format(N)})
    else:
        return pd.DataFrame({'getNthHighestSalary({})'.format(N): [None]})


