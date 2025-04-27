#%%

from config import *
#TRANSACTION:
#GROUP OF database operations that arecomplited togheter as unit or not at all
#related to operation that must be or all completed or all failed togheter = this is called atomicity
#STEPS
#1) define a callback function that specifies teh sequence of operation to perform inside the transaction
#2)start a client session
#3)start the tarnsaction by calling the with_transaction() method

#NOTA
#MONGODB will cancel any multi-document transaction that runs for more than 60 secs

from pymongo import MongoClient
from bson import ObjectId
from bson.decimal128 import Decimal128
from config import *

client = MongoClient(MONGODB_URI)
#transazione
#Un gruppo di operazioni (aggiornamenti e inserimenti) che devono riuscire tutte insieme o fallire tutte insieme.
#Se qualcosa va storto a metà, MongoDB annulla tutto
def transfer_callback(session, transfer_id=None, account_id_receiver=None, account_id_sender=None, transfer_amount=None):
    """
    account_id_sender : id da cui tolgo i soldi
    account_id_receiver : id a cui acconto


    """
    #se non esiste il database lo crea in automatico.
    #stessa cosa per le collection dentro banks, infatti ha creato "transfers"
    accounts_collection = session.client.bank.accounts
    transfer_collection = session.client.bank.transfers

    transfer = {
        "transfer_id": transfer_id,
        "to_account": account_id_receiver,
        "from_account": account_id_sender,
        "amount": Decimal128(str(transfer_amount))
    }

    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfer_complete": transfer_id}
        },
        session=session,
    )
    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {
            "$inc": {"balance": transfer_amount},
            "$push": {"transfer_complete": transfer_id}
        },
        session=session,
    )
    transfer_collection.insert_one(transfer, session=session)

def callback_wrapper(s):
    transfer_callback(
        s,
        transfer_id="xxx",
        account_id_receiver="111",
        account_id_sender="222",
        transfer_amount=100
    )

#qui inizia la transazione intesa come insieme di operazioni
with client.start_session() as session:
    session.with_transaction(callback_wrapper)

client.close()

# %%
