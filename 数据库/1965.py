import pandas as pd


def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employees, salaries, on='employee_id', how='outer')
    interset = list(set(employees['employee_id']).intersection(set(salaries['employee_id'])))
    df['judge'] = df['employee_id'].apply(lambda x: 1 if x in interset else 0)
    return df[df['judge'] == 0][['employee_id']].sort_values(by='employee_id')






