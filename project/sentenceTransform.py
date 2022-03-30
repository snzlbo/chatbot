from sentence_transformers import SentenceTransformer
from random import random
import pandas as pd
import numpy as np
import matplotlib

with open('/Users/fate/Desktop/Bachelor/employementAnalysis/project/latestData.tsv', 'r', encoding='utf-8') as file:
    app_lines = file.read().split('\n')

df = pd.read_csv(
    '/Users/fate/Desktop/Bachelor/employementAnalysis/project/latestData.tsv', sep='\t')

print(len(df))
filtered_df = df[df.Fax != 'None']

# it = 0
# for index, row in df.iterrows():
#     if it > 5:
#         break
#     if row['Max Salary'] > '1500000':
#         print('***********************************************')
#         print(row)
#     it = it + 1


def extractPrice(price):
    ans = .0
    if 
    return ans


def normalizeData(data_set):
    ret = pd.DataFrame(columns=["Min Salary", "Max Salary"])
    for index, row in data_set.iterrows():
        ret = ret.append({'Min Salary': float(row['Min Salary']),
                          'Max Salary': float(row['Max Salary'])
                          }, ignore_index=True)
    return ret


ret = normalizeData(df)
print(len(ret))
# print('a: ', ret)

print(type(df['Max Salary'][1]))
# df.plot.scatter(x='Min Salary', y='Max Salary', s=1)

# sentences = ["This is an example sentence", "Each sentence is converted"]

# print(sentences)
# sen_model = SentenceTransformer(
#     'sentence-transformers/msmarco-distilbert-multilingual-en-de-v2-tmp-lng-aligned')
# embeddings = sen_model.encode(sentences)
# print(embeddings)

# sentences = []

# y = []
# z = []
# for index, row in a
