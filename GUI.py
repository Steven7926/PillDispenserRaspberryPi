import tkinter as tk
from tkinter import *  
import json
from time import strftime 
from PIL import ImageTk,Image  
from GetUserData import GetUserData

# Begin Initial Window
window = tk.Tk(className = 'Magic Meds')

def checkSignup():

	user = GetUserData.userdata()
	if (user == 0):
		window.destroy()
	else:
		getUserInfoScreen

def getUserInfoScreen():
	window.destroy()
	windowNext = tk.Tk(className = 'Magic Meds')
	user = GetUserData.userdata()


	windowNext.mainloop()
	

def makeInitWindow():

	user = GetUserData.userdata()
	date = GetUserData.getSystemDate()
	timel = GetUserData.getSystemTime()

	if (user == 0):
		greeting = tk.Label(text= "Hello! Welcome to Magic Meds!", background = "#1e3f66", foreground = "white", font = "Arial 20 bold")
		greetingnext = tk.Label(text= "Please sign up on the mobile app before preceeding.", background = "#1e3f66", foreground = "white", font = "Arial 20 bold")
		greetingafter = tk.Label(text= "Press the button below when you have signed up.", background = "#1e3f66", foreground = "white", font = "Arial 20 bold")
		A = tk.Button(window, text ="I have signed up!", command = checkSignup)

		greeting.place(relx = 0.5, rely = 0.3, anchor = 'center')
		greetingnext.place(relx = 0.5, rely = 0.4, anchor = 'center')
		greetingafter.place(relx = 0.5, rely = 0.5, anchor = 'center')

		A.place(relx = 0.5, rely = 0.6, anchor = 'center')

	else: 
		greeting = tk.Label(text= "Hello " + user['FirstName'] + "! Welcome to Magic Meds!", background = "#1e3f66", foreground = "white", font = "Arial 25 bold")
		greeting.place(relx = 0.5, rely = 0.5, anchor = 'center')

		canvas = Canvas(window, width = 90, height = 90, background = "#1e3f66", highlightthickness=0)  
		canvas.place(relx=0.45, rely=0.2)  
		img = ImageTk.PhotoImage(Image.open("icon.png"))
		canvas.create_image(50, 50, anchor = 'center', image = img)

		A = tk.Button(window, text ="Continue", command = getUserInfoScreen)
		A.place(relx = 0.5, rely = 0.6, anchor = 'center')

		datelabel = tk.Label(text = date, background = "#1e3f66", foreground = "white", font = "Arial 15 bold")
		datelabel.place(relx = 0.1, rely = 0.04, anchor = 'center')


		timelabel = tk.Label(text = timel, background = "#1e3f66", foreground = "white", font = "Arial 15 bold")
		timelabel.place(relx = 0.9, rely = 0.04, anchor = 'center')
		



	# This removes the window resize, minimize, and close. 
	# This will only be uncommented when we have an MVP
	window.overrideredirect(1)
	window.geometry('{}x{}'.format(800, 480))
	window.configure(bg = '#1e3f66')

	window.mainloop()

makeInitWindow()
