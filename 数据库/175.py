#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：myDevelop 
@File    ：175.py
@IDE     ：PyCharm 
@Author  ：Du Manting
@Date    ：2024/11/13 14:41 
'''
import pandas as pd


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(person,address,on='personId',how='left')[['firstName','lastName','city','state']]