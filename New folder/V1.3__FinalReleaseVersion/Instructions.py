#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      4601465
#
# Created:     15/06/2018
# Copyright:   (c) 4601465 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import tkinter as tk

def instructions():

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()


    root.configure(background='black')

    instruction_label =tk.Label(frame,
    text = "Welcome to Deep Space w... shooter. Avoid bullets with the mouse while shooting down enemies."+"\n"+
            "You will remain safe as long as the green hitbox not touch enemy bullets"+"\n"+"\n"*3+"Enemy's health will go up exponentially with base 1.15, you will receive health recover and power upgrade at somepoints of the game."+"\n"*2+
            "the score multiplier will have an effect on your score, the higer you on the screen"+"\n"+"the higher your score will be"
            + "score:"+"\n"+"the closer the player gets to the top, the higher his multiplier will be, varies from 1 to 11 (100.0% to 1100.0%)"+"\n"+
            " then multiply by the log_base 1.12 of the wave modifier" + "\n"*5+
            "Mark and Xavier's record is more than five hundred thousand, up to 25th. wave and nearly 30 minutes, can you break the record?",
    fg = "white",
    bg = "black")


    quit_button = tk.Button(frame,
    text = "Quit",
    fg = "white",
    bg = "blue",
    command = root.destroy)

    instruction_label.pack()
    quit_button.pack()

    root.mainloop()

