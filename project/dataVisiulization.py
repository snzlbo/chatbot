from random import random
import requests
import pandas as pd
import numpy as np
import csv
import bs4 as BeautifulSoup
import random

with open('/Users/zolboo/Desktop/Bachelor/employementAnalysis/project/latestData.tsv', 'r', encoding='utf-8') as file:
    app_lines = file.read().split('\n')

df = pd.read_csv(
    '/Users/zolboo/Desktop/Bachelor/employementAnalysis/project/latestData.tsv', sep='\t')


def cleanSalary(salary) -> float:
    if(isinstance(salary, str)):
        return float(salary.replace(',', ''))
    return None


def cleanDealable(deal) -> bool:
    if(deal == 'Тохиролцоно'):
        return True
    return False

def cleanLocation(location) -> str:
    if isinstance(location, str) and location != 'None':
        return location
    return None

it = 0
def normalizeDataSet(data_set):
    ret = pd.DataFrame(columns=['branch', 'employee', 'jobTitle', 'level', 'type','minSalary', 'maxSalary', 'isDealable', 'city', 'district'])
    for index, row in data_set.iterrows():
        minSalary = cleanSalary(row['Min Salary'])
        maxSalary = cleanSalary(row['Max Salary'])
        location = cleanLocation(row['City/Provice'])
        print(type(row['District']), row['District'])
        if minSalary is None and maxSalary is None and location is None:
            continue
        dealable = cleanDealable(row['Is Dealable'])
        ret = ret.append({'branch': row['Category Name'],
                          'employee': row['Employee Company'],
                          'jobTitle': row['Title'],
                          'level': row['Level'],
                          'level': row['Type'],
                          'minSalary': minSalary,
                          'maxSalary': maxSalary,
                          'isDealable': dealable,
                          'city': location,
                          'district': row['District']
                          }, ignore_index=True)
    return ret


data_set = normalizeDataSet(df)
len(data_set)
