import schedule
from GetUserData import GetUserData

def job():
	user = GetUserData.userdata()
	medicationSchedule = GetUserData.getMedications(str(user["_id"]))
	print(medicationSchedule)

schedule.every(1).seconds.do(job)

while True:
	schedule.run_pending()