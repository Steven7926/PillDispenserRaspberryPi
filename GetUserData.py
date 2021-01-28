from pymongo import MongoClient
from random import randint
import json

class GetUserData:
    def userdata():
        # Make connection to DB and Cluser
        client = MongoClient('mongodb+srv://Steven:XO9V<Bpf)bGCNfKEX.6P0h!Z@cluster0.tjzfa.mongodb.net/MedMaster?retryWrites=true&w=majority')
        db = client.MedMaster

        # Get data from the Collection
        user = db.Users.find_one({'ProductCode': '1234'})

        return user
