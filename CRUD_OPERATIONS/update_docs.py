#%%
from pymongo import MongoClient
from bson import ObjectId
import pprint
from config import *

client=MongoClient(MONGODB_URI)
db=client["sample_mflix"]
collections=db["test"]

id_to_find = {"_id":ObjectId("680ce453ada94d0188699c73")}
#find e basta avrebbe trovata tipo un qualcosa di iterabile (cursor)
doc_to_find = collections.find_one(id_to_find)
pprint.pprint(doc_to_find)
#result = collection.update_one(<filter>,<update>)
doc_updated = collections.update_one(
    id_to_find,
    {"$set": {"field44": "pippo"}}
)
print("\n")
# reload the updated document
updated_doc = collections.find_one(id_to_find)
print(f"Document updated : {str(doc_updated.modified_count)}")
#print("\nDocumento aggiornato:")
#pprint.pprint(updated_doc)

client.close()
# esiste anche la varinet update_many. dicamo che uscirebbe meglio con qualcosa tipo bankaccounts
#si potrebbe fare qualcosa tipo 
#select_accounts={"account_type":"savings"}
#set_fileds={"$set":{"minimum_balance":100"}}
#results = collections.update_many(select_accounts,set_field)

# %%
#altro esempio:
#The companies collection is missing data on the initial public offerings (IPO) 
#for Linkedin and Facebook. Given the python file below, 
#select the expression that sets the ipo field to True for the two companies. (Select one).
# Get reference to 'sample_training' database
#db = client.sample_training
# Get reference to 'accounts' collection
#companies_collection = db.companies
# Filter
#select_companies = {"name": { "$in" : ["Facebook", "LinkedIn"]}}
# Update
#set_ipo = {"$set": {"ipo": True}}
# Select an expression that sets the value of "ipo" to True for Facebook and Linkedin
#result = companies_collection.update_many(select_companies, set_ipo)