#%%
#ogni volta che compili li carica tutti senza controlli se ci sono gia o meno
#cambia l id unico 

from pymongo import MongoClient 
from config import *
client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)


db=client["sample_mflix"]
collection = db["test"]

doc={
    "field1":"tac",
    "field2":"ciao"
}



result= collection.insert_one(doc)
doc_id=result.inserted_id
print(f"Unique id added by PYMongo : {doc_id}")

#SAME BUT USING INSERT_MANY
docs=[{
    "field0":"tac",
    "field0":"ciao"
},
{
    "000":"tac",
    "000":"ciao"
}]
results= collection.insert_many(docs)
docs_ids=results.inserted_ids
print(f"# Documents added : {len(docs_ids)}")
client.close()
# %%
