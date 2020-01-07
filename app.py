import tkinter as tk
from tkinter import *

# filedialog helps import the tasks
from tkinter import filedialog, Text
import os

# making tkinter to our root/head of the program
root = tk.Tk()

# Creating a list to store the added programs by the user
programList = []


# Creating the required functions


def addProgram():

    # we must first remove all existing widgets,before we can add our own
    for widgets in frame.winfo_children():
        widgets.destroy()

    fileName = filedialog.askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("executables", "*.exe"), ("all files", "*.*")),
    )
    programList.append(fileName)
    print("The desired program is: ", fileName)

    # going through each program selected
    programNumber = 0
    for selectedProgram in programList:
        # creating a label widget to display the text of the location for the desired prorgam to be added
        programNumber += 1
        appLocation_label = tk.Label(
            frame,
            text=f"{programNumber}.\t{selectedProgram[::]}",
            bg="white",
            fg="black",
        )
        appLocation_label.pack()


def runProgram():
    for desiredProgram in programList:
        os.startfile(desiredProgram)


# creating the outter canvas
canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

# creatiing the inner frame
frame = tk.Frame(root, bg="white")
# Placing the frame onto the canvas relative to the canvas
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)


# adding buttons to the root, we can add the btns to the frame as well
openFile = tk.Button(
    root,
    text="Open File",
    padx=10,
    pady=5,
    fg="white",
    bg="#263D42",
    command=addProgram,
)
# adding the btn to our root
openFile.pack()


runApps = tk.Button(
    root, text="Set App", padx=15, pady=5, bg="black", fg="white", command=runProgram
)
runApps.pack()

# running the root onto the screen display
root.mainloop()

