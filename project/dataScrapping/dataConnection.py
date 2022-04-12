# from pymongo import MongoClient
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

def get_engine(user, password, host, port, db):
  url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
  if not database_exists(url):
    create_database(url)
  engine = create_engine(url, pool_size=50, echo=False)
  print(type(engine))
  return engine

engine = get_engine('chatbot', '1234!@#$', '3.228.127.116', '5432', 'chatbot')
print(engine.url)
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
