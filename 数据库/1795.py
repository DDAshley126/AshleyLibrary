import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df = pd.melt(products, id_vars='product_id', var_name='store')
    df.dropna(axis=0, inplace=True)
    return df.rename(columns={'value': 'price'})






