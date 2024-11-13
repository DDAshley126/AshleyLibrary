import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users.apply(lambda x: x['name'][0].upper() + x['name'][1:].lower(),axis=1)
    users = users.sort_values('user_id')
    return users








