from cgitb import text
from textwrap import fill
from tkinter import *
import os
from new_note import *

class Window:
    def open_note(self):
        pass
    
    def __init__(self) -> None:
        file_struct = os.listdir("/media/japemasterbrad/ZEUS/DEV/PYTHON/note-app/notes")
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
        listbox.pack(pady=25)
        
        button_frame = Frame(window, background="BLUE")
        
        # Listbox --------------ADD VERTICAL SCROLLBAR----------------
        notes_list = Listbox(listbox, width=40, height=8)
        notes_list.pack()
        notes_list.bind("<Button-1>", Note.new_note)
        
        for notes in file_struct:
            print(notes)
            notes_list.insert(END, notes)
            
        # Buttons ----------------------------------------------------
        open_button = Button(button_frame, text="Open", command=self.open_note)


        window.mainloop()


Window()