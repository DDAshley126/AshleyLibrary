import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='left', suffixes=('', '_y'))
    max_salary = df.groupby(by=['name_y'])['salary'].transform('max')
    df = df[df['salary'] == max_salary]
    df.rename(columns={'name_y': 'Department', 'name': 'Employee', 'salary': 'Salary'}, inplace=True)
    return df[['Department', 'Employee', 'Salary']]