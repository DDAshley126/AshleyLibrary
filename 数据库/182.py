import pandas as pd


def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person[['email']][person.duplicated(subset=['email'])].drop_duplicates()