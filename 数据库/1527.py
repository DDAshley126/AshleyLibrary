import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].apply(judge)]


def judge(conditions):
    for i in conditions.split():
        if i.startswith('DIAB1'):
            return True
    return False








