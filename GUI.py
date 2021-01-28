import tkinter as tk
import json
from GetUserData import GetUserData

# Begin Window 
window = tk.Tk(className = 'Magic Meds')
user = GetUserData.userdata()

def checkSignup():

	user = GetUserData.userdata()
	if (user == 0):
		window.destroy()
	else:
		window.destroy()
		print("success")



def makeWindow():


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
		A = tk.Button(window, text ="Continue", command = window.destroy)

		greeting.place(relx = 0.5, rely = 0.5, anchor = 'center')
		A.place(relx = 0.5, rely = 0.6, anchor = 'center')



	# This removes the window resize, minimize, and close. 
	# This will only be uncommented when we have an MVP
	window.overrideredirect(1)
	window.geometry('{}x{}'.format(800, 480))
	window.configure(bg = '#1e3f66')

	window.mainloop()

makeWindow()
