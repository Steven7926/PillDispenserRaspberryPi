from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image  
from GetUserData import GetUserData

import datetime
import json


# Begin Initial Window
window = Tk(className = 'Magic Meds')
datelabel = Label(background = "#1e3f66", foreground = "white", font = "Arial 15 bold")
timelabel = Label(background = "#1e3f66", foreground = "white", font = "Arial 15 bold")

def clock():
    dateTime = datetime.datetime.now().strftime("%b %d, %Y  %H:%M:%S/%p")
    date,time1 = dateTime.split("  ")
    time2,time3 = time1.split('/')
    hour,minutes,seconds =  time2.split(':')
    if int(hour) > 12 and int(hour) < 24:
            time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
    else:
            time = time2 + ' ' + time3
    timelabel.config(text = time)
    datelabel.config(text = date)
    timelabel.after(1000, clock)

def checkSignup():

	user = GetUserData.userdata()
	if (user == 0):
		window.destroy()
	else:
		getUserInfoScreen

def getUserInfoScreen():
	window.destroy()
	windowNext = Tk(className = 'Magic Meds')
	user = GetUserData.userdata()


	windowNext.mainloop()
	

def makeInitWindow():

	user = GetUserData.userdata()
	date = GetUserData.getSystemDate()
	timel = GetUserData.getSystemTime()

	if (user == 0):
		greeting = Label(text= "Hello! Welcome to Magic Meds!", background = "#1e3f66", foreground = "white", font = "Arial 20 bold")
		greeting.place(relx = 0.5, rely = 0.3, anchor = 'center')

		greetingnext = Label(text= "Please sign up on the mobile app before preceeding.", background = "#1e3f66", foreground = "white", font = "Arial 20 bold")
		greetingnext.place(relx = 0.5, rely = 0.4, anchor = 'center')

		greetingafter = Label(text= "Press the button below when you have signed up.", background = "#1e3f66", foreground = "white", font = "Arial 20 bold")
		greetingafter.place(relx = 0.5, rely = 0.5, anchor = 'center')

		A = tk.Button(window, text ="I have signed up!", command = checkSignup)
		A.place(relx = 0.5, rely = 0.6, anchor = 'center')

		datelabel.place(relx = 0.1, rely = 0.04, anchor = 'center')
		timelabel.place(relx = 0.9, rely = 0.04, anchor = 'center')

		clock()

	else: 
		greeting = Label(text= "Hello " + user['FirstName'] + "! Welcome to Magic Meds!", background = "#1e3f66", foreground = "white", font = "Arial 25 bold")
		greeting.place(relx = 0.5, rely = 0.5, anchor = 'center')

		canvas = Canvas(window, width = 90, height = 90, background = "#1e3f66", highlightthickness=0)  
		canvas.place(relx=0.45, rely=0.2)  
		img = ImageTk.PhotoImage(Image.open("icon.png"))
		canvas.create_image(50, 50, anchor = 'center', image = img)

		A = Button(window, text ="Continue", command = getUserInfoScreen)
		A.place(relx = 0.5, rely = 0.6, anchor = 'center')

		
		datelabel.place(relx = 0.1, rely = 0.04, anchor = 'center')
		timelabel.place(relx = 0.9, rely = 0.04, anchor = 'center')

		clock()
		

	# This removes the window resize, minimize, and close. 
	# This will only be uncommented when we have an MVP
	window.overrideredirect(1)
	window.geometry('{}x{}'.format(800, 480))
	window.configure(bg = '#1e3f66')

	window.mainloop()

makeInitWindow()
