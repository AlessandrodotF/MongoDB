#%%
#NON RUNNATO PERCHE NON AVEVO I DATI o voglia di crearli
from pymongo import MongoClient
from bson import ObjectId
from config import*
import pprint
client=MongoClient(MONGODB_URI)

conversion_rate_usd_to_gbp=1.3
#pipeline = [stage1,stage2,etc.]
#db.collection.aggragate(pipeline)
db=client.bank
accounts_collections=db.accounts

#select checking accounts with balance of more 1500$
select_by_balance = {"$match":{"account_type": "checking","balance": {"$gt":1500}}}
#organize the docs from  the highest to the lowest
organize_by_original_balance = {"$sort":{"balance":-1}}
#return only the account type & balance fileds, plus a new field containing balance in GBP
return_specified_field = {
    "$project":{
        "account_type":1,
        "balance":1,
        "gbp_balance":{"$divide":["$balance",conversion_rate_usd_to_gbp]},#create a new field
        "_id":0#supress id field
    }
}

pipeline = [select_by_balance,organize_by_original_balance,return_specified_field]
results = accounts_collections.aggregate(pipeline)#return a cursor ! 

for item in results:
    pprint.pprint(item)

client.close()
