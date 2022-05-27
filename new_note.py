from tkinter import *
import os

from click import pass_context
import window

class Note:
    
    def __init__(self, ):
        def get_name_input(self):
            name = name_input.get()
            
        global default_note_name
        global note_name
        
        file_struct = os.listdir("notes")

#       generate new note name
        current_list_no = len(file_struct)
        default_note_name = current_list_no + 1
        
        # TKINTER WINDOW VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
        new_note = Tk()
        new_note.geometry('400x150')
        new_note.title("New Note - Skribl")
        new_note_frame = Frame(new_note)
        new_note_frame.pack(pady = 25)
        
        Label(new_note_frame, text = "Enter a new name for your note:").pack()
        name_input = Entry(new_note_frame)
        name_input.pack(pady = 5)
        button = Button(new_note_frame, text = "Submit", command = get_name_input(self)).pack()

        new_note.mainloop()
        # TKINTER WINDOW ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        
        # naming note
        # note_name_input = input("Name your note:\n")


        # if note_name_input != "":
        #     note_name = note_name_input
        # else:
        #     note_name = "New Note " + str(default_note_name)

        # filename = note_name + ".txt"
        
    def new_note(self):
        print("New note time")
        return None
    
    def get_note_name():
        return note_name

    def open_note(self):
        window.Window(note_name)
        


        