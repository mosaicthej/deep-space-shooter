#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      4601465
#
# Created:     24/05/2018
# Copyright:   (c) 4601465 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

def start():
    print("Welcome")

def instructions():
    print("Welcome to [our game].  Shoot down the enemies while avoiding enemy bullets.")

start_button = tk.Button(frame,
    text = "Start",
    fg = "white",
    bg = "blue",
    height = 2,
    width = 10,
    command = start)

instruction_button = tk.Button(frame,
    text = "Instructions",
    fg = "white",
    bg = "blue",
    height = 2,
    width = 10,
    command = instructions)

quit_button = tk.Button(frame,
    text = "Quit",
    fg = "white",
    bg = "blue",
    height = 2,
    width = 10,
    command = quit)


start_button.pack(side=tk.TOP)
instruction_button.pack(side=tk.TOP)
quit_button.pack(side=tk.TOP)

background_image=tk.PhotoImage("background_menu_image_test.png")
background_label = tk.Label(root, image=background_image)
background_label.photo=background_image
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()
