#%%
from pymongo import MongoClient
from bson import ObjectId
from config import *

client = MongoClient(MONGODB_URI)
db=client["sample_mflix"]
collection = db["test"]

#.delete_one(<filter>)
#.delete_many()
doc_to_del = {"_id":ObjectId("680ce453ada94d0188699c73")}
result = collection.delete_one(doc_to_del)

print(f"Number of deleted doc : {str(result.deleted_count)}")
client.close()
# %%
# esiste anche la varinet delete_many. dicamo che uscirebbe meglio con qualcosa tipo bankaccounts
#si potrebbe fare qualcosa tipo 
#docs_to_delete={"balance":{"$lt":1000}}

#results = collections.delete_mant(docs_to_delete)
