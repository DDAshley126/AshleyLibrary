import pandas as pd


def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    inValid = sales[(sales['sale_date'] < '2019-01-01') | (sales['sale_date'] > '2019-03-31')]['product_id']
    Valid = sales[~sales['product_id'].isin(inValid)]['product_id']
    return product[product['product_id'].isin(Valid)][['product_id', 'product_name']]












