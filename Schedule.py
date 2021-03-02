import schedule
import datetime
from GetUserData import GetUserData

def job():
	user = GetUserData.userdata()
	medicationSchedule = GetUserData.getMedications(str(user["_id"]))
	currentDate = datetime.datetime.now().strftime("%A %H:%M:%S")

	for i in medicationSchedule:
		timeTaken = i['TimeTaken'] + ":01"
		dayTaken = i['DayTaken']
		medTime = dayTaken + " " + timeTaken
		print("MedicationTime: " + medTime)
		print("Current Date: " + currentDate)
		if (currentDate == medTime):
			sendData()
		else:
			print("Do they match: no");

def sendData():
	print("Do they match: yes")
	## Send Data to Atmega using SPI to turn the motor

schedule.every(1).seconds.do(job)

while True:
	schedule.run_pending()