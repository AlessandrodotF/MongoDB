#%%
#NON RUNNATO PERCHE NON AVEVO I DATI o voglia di crearli
from pymongo import MongoClient
from bson import ObjectId
from config import*
import pprint
client=MongoClient(MONGODB_URI)

#pipeline = [stage1,stage2,etc.]
#db.collection.aggragate(pipeline)
db=client.bank
accounts_collections=db.accounts

#select account where the balance is less then:
select_by_balance = {"$match":{"balance":{"$lt":2000}}}
#separete documents by account type and calculate the avg balance for each type
separate_by_account_calculate_avg_balance={"$group":{"_id":"$account_type","avg_balance":{"$avg": "$balance"}}}


#aggregation pipeline using "stage_match_balance" and "stage_group_account_type"

pipeline = [select_by_balance,separate_by_account_calculate_avg_balance]

results = accounts_collections.aggregate(pipeline)#return a cursor ! 

for item in results:
    pprint.pprint(item)

client.close()