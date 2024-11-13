import pandas as pd


def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(visits, transactions, on='visit_id', how='outer')
    df.fillna(0, inplace=True)
    df = df.groupby(by='customer_id')[['amount']].value_counts().to_frame(name='count_no_trans').reset_index()
    return df[df['amount'] == 0][['customer_id', 'count_no_trans']]








