import pandas as pd


def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders[orders['order_date'].dt.strftime('%Y-%m') == '2020-02']
    df = pd.merge(products,orders, on='product_id', how='left')
    data = df.groupby(by='product_name')[['unit']].sum().reset_index()
    return data[data['unit'] >= 100][['product_name', 'unit']]








