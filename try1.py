# this is a try window in this i am going to try specific modules
import pyttsx3
import tkinter as tk
from tkinter import *
root = tk.Tk()
root.geometry("1000x800")
root.config(bg = "white")
root.title("friday")
label = tk.Label(root,text = "friday",font = ("arial",18))
label.pack()
textbox = tk.Text(root,height = 10,width = 100,font = ("arial",16),bg = "black",fg = "white")
textbox.pack()
button = tk.Button(root, text="start func",bg = "black",fg = "white")
button.pack(pady = 20,padx=20)
root.mainloop()
engine = pyttsx3.init() # this function is neccessary before using pyttsx3 
rate = engine.getProperty('rate')# this function will get this property named rate this means the speed of assistance
print(rate)
engine.setProperty('rate',150)
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume',1.0)
engine.say("")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
engine.runAndWait()