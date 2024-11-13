import pandas as pd


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = triangle.apply(lambda x: 'Yes' if max(x) < sum(x) - max(x) else 'No', axis=1)
    return triangle















