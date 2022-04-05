from sentence_transformers import SentenceTransformer
from random import random
import pandas as pd
import numpy as np
import matplotlib

with open('/Users/zolboo/Desktop/bachelor/employementAnalysis/project/latestData.tsv', 'r', encoding='utf-8') as file:
    app_lines = file.read().split('\n')

df = pd.read_csv(
    '/Users/zolboo/Desktop/bachelor/employementAnalysis/project/latestData.tsv', sep='\t')

print(len(df))
filtered_df = df[df.Fax != 'None']

# def extractPrice(price):
#     print(type(price))
#     ans = float(price.replace(',', ''))
#     return ans


# def normalizeData(data_set):
#     ret = pd.DataFrame(columns=["Title", "Min Salary", "Max Salary", "isDealable", "City/Provice", "District"])
#     for index, row in data_set.iterrows():
#         t_price = extractPrice(row['Min Salary'])
#     return ret


# ret = normalizeData(df)
# print(len(ret))
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
