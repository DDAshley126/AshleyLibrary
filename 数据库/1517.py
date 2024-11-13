import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    r = '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    valid_users = users[users['mail'].str.match(r)]
    return valid_users








