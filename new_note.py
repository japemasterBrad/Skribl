from email.policy import default
from sqlite3 import *
import os

class Note:
    def __init__(self):
        global default_note_name
        global note_name
        
        file_struct = os.listdir("/media/japemasterbrad/ZEUS/DEV/PYTHON/note-app/notes")
        

#       generate new note name
        current_list_no = len(file_struct)
        default_note_name = current_list_no + 1

#       naming note
        note_name_input = input("Name your note:\n")

        if note_name_input != "":
            note_name = note_name_input
        else:
            note_name = "New Note " + str(default_note_name)

        filename = note_name + ".txt"

        os.system("clear")
        print(f"Note name: {note_name}")
        
        input("Press enter to conitnue")
        exit()
        
    def new_note(self):
        print("New note time")
        return 
    
    def get_note_name():
        return note_name