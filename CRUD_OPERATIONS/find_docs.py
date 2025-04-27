#%%
from pymongo import MongoClient
from bson import ObjectId
from config import*
import pprint
client=MongoClient(MONGODB_URI)

db=client["sample_mflix"]
collection=db["test"]

document_to_find={"_id":ObjectId("680ce453ada94d0188699c73")}

result=collection.find_one(document_to_find)
pprint.pprint(result)
client.close()
# %%

#EXAMPLE QUERY FOR COMPARISON NUMBERS
#immagina di avere un qualcosa tipo bank account 
#document_to_find={"balance": {"$gt":1000}}
#found_docs=bank_accounts.find(document_to_find)
#n_docs_found=0
#for i in found_docs:
#    n_docs_found+=1
#print(f"# docs found {n_docs_found}")
#client.close()