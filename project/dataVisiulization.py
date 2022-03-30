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

print(len(df))
filtered_df = df[df.Fax != 'None']
print(len(df), len(filtered_df))

it = 0
for index, row in df.iterrows():
    if it > 5:
        break
    if row['Max Salary'] > '1500000':
        print('***********************************************')
        print(row)
    it = it + 1
