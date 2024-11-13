import pandas as pd


def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(users, transactions, on='account', how='right').groupby(by='name')[['amount']].sum().reset_index().rename(columns={'amount': 'balance'})
    return df[df['balance'] > 10000]








