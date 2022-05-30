from array import array
from fileinput import filename
from re import I, L
from select import select
from tkinter import *

import os
from xml.dom.minidom import TypeInfo
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

        def open_note(event):
            _selection = get_selection()
            selection = list(_selection)
            selection_delete_point = selection.__len__() - 4
            
            delete_point = None               

            # for i in enumerate(selection):
            #     print(i)
            #     if i == selection_delete_point:
            #         while delete_point != selection.__len__():
            #             selection.remove(i)
            #             # print(selection)
                        
                
                
###############################################################################################
            # selection is now an array
            # - loop throguh array to find ".txt" to os.remove
            # - remove them from array
            # - convert back to string again
###############################################################################################



            
        def get_selection(): 
            selection = notes_list.get(ANCHOR)
            return selection
            
        notes_list = Listbox(note_list, width=40, height=9)
        notes_list.pack()
        notes_list.bind("<Button-1>", open_note) # OPEN FROM CLASS
        


        for notes in file_struct:
            notes_list.insert(END, notes)
            

        
        open_button = Button(button_frame, text="New Note", command=new_note.Note)
        open_button.pack(pady=10)

        root.mainloop()

            
if __name__ == "__main__":
    Main()
