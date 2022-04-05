from random import random
import requests
import pandas as pd
import numpy as np
import csv
import bs4 as BeautifulSoup
import random

with open('/Users/fate/Desktop/Bachelor/employementAnalysis/project/latestData.tsv', 'r', encoding='utf-8') as file:
    app_lines = file.read().split('\n')

df = pd.read_csv(
    '/Users/fate/Desktop/Bachelor/employementAnalysis/project/latestData.tsv', sep='\t')


def cleanSalary(salary) -> float:
    if(isinstance(salary, str)):
        return float(salary.replace(',', ''))
    return None


def cleanDealable(deal) -> bool:
    if(deal == 'Тохиролцоно'):
        return True
    return False


def normalizeDataSet(data_set):
    ret = pd.DataFrame(columns=['employee', 'jobTitle', 'level', 'minSalary',
                       'maxSalary', 'isDealable', 'city', 'district'])
    for index, row in df.iterrows():
        minSalary = cleanSalary(row['Min Salary'])
        maxSalary = cleanSalary(row['Max Salary'])
        if minSalary is None and maxSalary is None:
            continue
        dealable = cleanDealable(row['Is Dealable'])
        ret = ret.append({'branch': row['Category Name'],
                          'employee': row['Employee Company'],
                          'jobTitle': row['Title'],
                          'level': row['Level'],
                          'minSalary': minSalary,
                          'maxSalary': maxSalary,
                          'isDealable': dealable,
                          'city': row['City/Province'],
                          'district': row['District']
                          }, ignore_index=True)
    return ret


data_set = normalizeDataSet(df)
len(data_set)
