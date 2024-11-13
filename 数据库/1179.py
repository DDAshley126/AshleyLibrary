import pandas as pd


def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df = department.melt(id_vars=['id', 'month']).pivot(values='value', columns='month', index='id').reindex(columns=months)
    month = ['{}_Revenue'.format(x) for x in months]
    df.columns = month
    return df.reset_index()











