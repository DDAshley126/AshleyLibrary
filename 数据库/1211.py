import pandas as pd
from decimal import Decimal, ROUND_HALF_UP


def up_round(x):
    return Decimal(x).quantize(Decimal('.00'), rounding=ROUND_HALF_UP)


def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries['rating']/queries['position']
    df = queries.groupby(by='query_name').agg(
        quality=('quality', lambda x: up_round(x.mean())),
        poor_query_percentage=('rating', lambda x: up_round((x < 3).sum()/len(x)*100))
    ).reset_index()
    return df











