import pandas as pd


def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left', suffixes=('', '_y')).sort_values(by=['departmentId', 'salary'], ascending=[True, False]).rename(columns={'name_y': 'Department', 'name': 'Employee', 'salary': 'Salary'})
    df['rank'] = df.groupby(by='departmentId').rank(ascending=False, method='dense')['Salary']
    return df[df['rank'] <= 3][['Department', 'Employee', 'Salary']]