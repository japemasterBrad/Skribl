from fileinput import filename
from tkinter import *

import os
import new_note
import window

class Main:
    os.system("clear")
    global app_name
    app_name = "Skribl"

    def __init__(self):
        
        file_struct = os.listdir("notes")

        root = Tk()
        root.title("Notes - Skribl")
        root.geometry("200x270")
        root.grid_columnconfigure(0, weight=1)
        root.resizable(0, 0)

        note_list = Frame(root, background="RED")
        note_list.pack(pady=25, side = "top")
        button_frame = Frame(root)
        button_frame.pack(side = "bottom")

        notes_list = Listbox(note_list, width=40, height=9)
        notes_list.pack()
        
        # listbox_selection = note_list.get()
        # print(listbox_selection)

        for notes in file_struct:
            notes_list.insert(END, notes)
            
       

        # notes_list.bind("<Button-1>", open_note) # OPEN FROM CLASS
        
        open_button = Button(button_frame, text="New Note", command=new_note.Note)
        open_button.pack(pady=10)

        root.mainloop()

            

Main()


'''
Program sticking points:
- cannot get string value for listbox selection

'''