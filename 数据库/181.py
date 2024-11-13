import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    data = pd.merge(employee, employee, left_on='id', right_on='managerId', how='right',suffixes=('','_y')).drop(['id','name','id_y','managerId','managerId_y'],axis=1)
    data = data[data['salary_y'] > data['salary']][['name_y']]
    data.columns = ['Employee']
    return data