import tkinter as tk
from tkinter import *

# filedialog helps import the tasks
from tkinter import filedialog, Text
import os


root = tk.Tk()

# creating the outter canvas
canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

# creatiing the inner frame
frame = tk.Frame(root, bg="white")
# Placing the frame onto the canvas relative to the canvas
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)


# adding buttons to the root, we can add the btns to the frame as well
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42")
# adding the btn to our root
openFile.pack()


runApps = tk.Button(root, text="Set App", padx=15, pady=5, bg="black", fg="white")
runApps.pack()


root.mainloop()

