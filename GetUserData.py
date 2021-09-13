from pymongo import MongoClient
from random import randint
from datetime import datetime
import json

class GetUserData:

    #Product Code is hard coded value that is machine specific
    global productCode 
    productCode = '890'

    # Make connection to DB and Cluser
    global client 
    client = MongoClient('mongodb+srv://Steven:XO9V<Bpf)bGCNfKEX.6P0h!Z@cluster0.tjzfa.mongodb.net/MedMaster?retryWrites=true&w=majority')

    global db 
    db = client.MedMaster

    def userdata():  
        
        # Get data from the Collection
        user = db.Users.find_one({'ProductCode': productCode})
        usercount = db.Users.find({'ProductCode': productCode}).count()

        if (usercount == 0):
            return 0

        return user
        
    def getMedications(userid):
         # Get the Users Medications
         usersMedication = db.Medications.find({'UserId': userid})
         meds = list(usersMedication)

         return meds

    def getSystemTime():
        # Get the current system time

        now = datetime.now()
        currentTime = now.strftime("%H:%M:%S %p")
        return currentTime

    def getSystemDate():
        # Get the current system date

        now = datetime.now()
        currentDate = now.strftime("%m %d, %Y")
        return currentDate