import schedule
import datetime
from GetUserData import GetUserData
import spidev
import time
from array import array
import ctypes
import pathlib

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
			print("Do they match: no")

def sendData():
	print("Do they match: yes")
	## Send Data to Atmega using SPI to turn the motor
	bus = 0
	device = 0
	spi = spidev.SpiDev()
	print(spi)
	spi.open(bus, device)
	print(spi)

	spi.max_speed_hz = 1000000

	send_byte = 0x80
	print(send_byte)
	rcv_byte = spi.xfer2([send_byte])
	print(rcv_byte)
	# rcv_byte = spi.xfer2([send_byte])
	print(rcv_byte)
	data_recv = rcv_byte[0]
	print(data_recv)

	spi.close()

# def runjob():
# 	schedule.every(1).seconds.do(job)

# 	while True:
# 		schedule.run_pending()

schedule.every(1).seconds.do(job)

while True:
	schedule.run_pending()