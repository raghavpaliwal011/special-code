import tkinter as tk
import pyttsx3

# Initialize the pyttsx3 text-to-speech engine
engine = pyttsx3.init()

# Function to speak the text entered in the Entry widget
def speak_text():
    text = entry.get()  # Retrieve text from the Entry widget
    if text:  # Check if the text is not empty
        engine.say(text)
        engine.runAndWait()
    else:
        engine.say("Please enter some text.")
        engine.runAndWait()

# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Create an Entry widget for text input
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create a button that will call speak_text function when clicked
speak_button = tk.Button(root, text="Speak", command=speak_text)
speak_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()