from pymongo import MongoClient
import pandas as pd


client = MongoClient(
    "mongodb+srv://sainaa:1234@chatbot.7uvjg.mongodb.net/chatbot?retryWrites=true&w=majority")
db = client.chatbot
print(db.list_collection_names())
adCollection = db.advertisement
print(db)
df = pd.read_csv(
    '/Users/fate/Desktop/Bachelor/employementAnalysis/project/dataConnection/data.csv', sep=',')
data = df.to_dict(orient='records')

adCollection.insert_one(data[0])
# adCollection.drop()
