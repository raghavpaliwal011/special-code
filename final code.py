import pyttsx3
import tkinter as tk
from tkinter import *

# Initialize the pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set to female voice

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to handle button click
def on_button_click():
    user_input = entry.get()
    if user_input.strip() == "raghav paliwal the god of gta 5":
        return
    textbox.insert(END, "You: " + user_input + "\n")
    
    # Simple echo bot response
    response = "" + user_input
    textbox.insert(END, response + "\n")
    
    # Speak the response
    speak(response)
    
    # Clear the entry box
    entry.delete(0, END)

# Create the main window
root = tk.Tk()
root.geometry("1000x1000")
root.config(bg="white")
root.title("Friday")

# Create and pack widgets
label = tk.Label(root, text="Friday", font=("Arial", 18))
label.pack(pady=10)

textbox = tk.Text(root, height=20, width=100, font=("Arial", 16), bg="black", fg="white")
textbox.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)

button = tk.Button(root, text="Start Func", bg="black", fg="white", command=on_button_click)
button.pack(pady=20)

# Start the main event loop
root.mainloop()