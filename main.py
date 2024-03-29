from tkinter import *

import os
import new_note
import window

class Main:
    global app_name
    app_name = "Skribl"

    
    def __init__(self) -> None:
        file_struct = os.listdir("notes")
        button_height = 1
        
        def save_file():
            print("saving file now")
            
        def load_file():
            print("loading file now")
        # Tkinter init ----------------------------------------------------
        
        window = Tk()
        window.title("Notes - Skribl")
        window.geometry("200x270")
        window.grid_columnconfigure(0, weight=1)
        window.resizable(0, 0)

        # Frames ----------------------------------------------------
        
        listbox = Frame(window, background="RED")
        listbox.pack(pady=25, side = "top")
        
        button_frame = Frame(window)
        button_frame.pack(side = "bottom")
        
        # Listbox --------------ADD VERTICAL SCROLLBAR----------------
        notes_list = Listbox(listbox, width=40, height=10)
        notes_list.pack()
        notes_list.bind("<Button-1>", self.new_note)
        
        # Buttons ----------------------------------------------------
        open_button = Button(button_frame, text="New Note", command=self.new_note)
        open_button.pack(pady=10)

        for notes in file_struct:
            print(notes)
            notes_list.insert(END, notes)
            

        window.mainloop()

    def new_note(self):
        new_note.Note()



Main()