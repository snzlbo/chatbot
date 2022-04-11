# from pymongo import MongoClient
import psycopg2
import pandas as pd
from dataScrapping.data import cleanData as useCleandata


df = pd.read_csv('/Users/fate/Desktop/Bachelor/employementAnalysis/project/dataConnection/advertisement.csv')
data = df.to_dict(orient='records')
print(df.dtypes)

# conn = psycopg2.connect(database="chatbot",
#                         user='chatbot', password='1234!@#$',
#                         host='3.228.127.116', port='5432'
#                         )

# conn.autocommit = True
# cursor = conn.cursor()

# client = MongoClient(
#     "mongodb+srv://sainaa:1234@chatbot.7uvjg.mongodb.net/chatbot?retryWrites=true&w=majority")
# db = client.chatbot
# print(db.list_collection_names())
# adCollection = db.advertisement
# print(db)
# df = pd.read_csv(
#     '/Users/fate/Desktop/Bachelor/employementAnalysis/project/dataConnection/data.csv', sep=',')
# data = df.to_dict(orient='records')

# adCollection.insert_one(data[0])
# adCollection.drop()
