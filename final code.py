import pyttsx3
import tkinter as tk
from tkinter import *
import webbrowser
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def speak_text():
    text = entry1.get()
    if text:
        engine.say(text)
        engine.runAndWait()

    else:
        engine.say("please enter some text")
        engine.runAndWait()

def star_func():
    info = entry2.get()
    if info == "open youtube":
        webbrowser.open("https://www.youtube.com")
    else:
        engine.say("sorry but i cannot proceed")

def star_func():
    info = entry2.get()
    if info == "open prime":
        webbrowser.open("https://www.primevideo.com/")
    else:
        engine.say("sorry i cannot proceed")

def star_func():
    info = entry2.get()
    if info == "open extramarks":
        webbrowser.open("https://www.extramarks.com/")
    else:
        engine.say("sorry but i cannot proceed")
        
root = tk.Tk()
root.title("friday")

root.geometry("500x800")

root.config(bg="black")

label1 = tk.Label(root,text = "friday",height = 2,width=10,font=50,bg="black",fg="white")
label1.pack(pady=20)

entry1 = tk.Entry(root, width=50)
entry1.pack(pady=10)

entry2 = tk.Entry(root, width=50)
entry2.pack(pady=110)

button= tk.Button(root,text="start function",command=speak_text,height=5,width=10)
button.pack(pady=40)

button2 = tk.Button(root,text = "go func",command = star_func,height = 5, width = 10)
button2.pack(pady=60)

root.mainloop()

