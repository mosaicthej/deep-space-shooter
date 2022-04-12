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
import Main_vM3
import Instructions

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.configure(background='black')

start_button = tk.Button(frame,
    text = "Start",
    fg = "white",
    bg = "blue",
    height = 2,
    width = 10,
    command = Main_vM3.main)


instruction_button = tk.Button(frame,
    text = "Instructions",
    fg = "white",
    bg = "blue",
    height = 2,
    width = 10,
    command = Instructions.instructions)



quit_button = tk.Button(frame,
    text = "Quit",
    fg = "white",
    bg = "blue",
    height = 2,
    width = 10,
    command = root.destroy)


start_button.pack()
instruction_button.pack()
quit_button.pack()

root.mainloop()
