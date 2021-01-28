from pymongo import MongoClient
from random import randint
import json

class GetUserData:
    def userdata():
        
        #Product Code is hard coded value that is machine specific
        productCode = '8902'

        # Make connection to DB and Cluser
        client = MongoClient('mongodb+srv://Steven:XO9V<Bpf)bGCNfKEX.6P0h!Z@cluster0.tjzfa.mongodb.net/MedMaster?retryWrites=true&w=majority')
        db = client.MedMaster

        # Get data from the Collection
        user = db.Users.find_one({'ProductCode': productCode})
        usercount = db.Users.find({'ProductCode': productCode}).count()

        if (usercount == 0):
            return 0

        userid = str(user["_id"])

        # Get the Users Caregivers and Medications
        usersCaregivers = db.Caregivers.find({'UserId': userid})
        usersMedication = db.Medications.find ({'UserId': userid})

        print(usercount)

        return user
