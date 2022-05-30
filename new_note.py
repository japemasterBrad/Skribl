from tkinter import *
import os

from click import pass_context
import window

class Note:
    global default_note_name
    global note_name
    
    def __init__(self):
        self.file_struct = os.listdir("notes")

#       generate new note name
        self.current_list_no = len(self.file_struct)
        self.default_note_name = self.current_list_no + 1
        
        # TKINTER WINDOW VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
        self.new_note = Tk()
        self.new_note.geometry('400x150')
        self.new_note.title("New Note - Skribl")
        self.new_note_frame = Frame(self.new_note)
        self.new_note_frame.pack(pady = 25)
        
        Label(self.new_note_frame, text = "Enter a new name for your note:").pack()
        self.name_input = Entry(self.new_note_frame).pack(pady = 5)
        self.new_name_input = self.name_input#.get()
        
        self.submit_button = Button(self.new_note_frame, text = "Submit")
        self.submit_button.pack()
        self.submit_button.bind("<Button-1>", self.new_note.mainloop())




        
        # TKINTER WINDOW ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



        