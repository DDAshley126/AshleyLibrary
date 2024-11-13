import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby(by='customer_number').count().reset_index()
    return df[df['order_number'] == df['order_number'].max()][['customer_number']]
















