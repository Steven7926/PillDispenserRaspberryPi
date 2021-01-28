import tkinter as tk
import json
from GetUserData import GetUserData


# Begin Window 
window = tk.Tk(className = 'Magic Meds')
user = GetUserData.userdata()

greeting = tk.Label(text= "Hello " + user['FirstName'] + "! Welcome to Magic Meds!", background = "#1e3f66", foreground = "white", font = "Arial 25 bold")

greeting.place(relx = 0.5, rely = 0.5, anchor = 'center')

# This removes the window resiz, minimize, and close. 
# This will only be uncommented when we have an MVP
window.overrideredirect(1)
window.geometry('{}x{}'.format(800, 480))
window.configure(bg = '#1e3f66')

A = tk.Button(window, text ="Continue", command = window.destroy)
A.place(relx = 0.5, rely = 0.6, anchor = 'center')
window.mainloop()

