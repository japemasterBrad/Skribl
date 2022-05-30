from tkinter import *

class Window:
    def __init__(self, note_name) -> None:
        root = Tk()
        root.title(note_name + " - Skribl")
        root.geometry("600x450")

        button_frame = Button(root)
        button_frame.pack(side = 'top')
        
        save_button = Button(button_frame, text = "Save")
        save_button.pack(side = "left")
        
        exit_without_saving_button = Button(root, text = "Exit without saving")
        exit_without_saving_button.pack(side = "right")
        
        body_frame = Frame(root, background="RED")
        body_frame.pack(side = "bottom", padx=10, pady=10)

        body = Text(body_frame)
        body.pack(side = "bottom")

        root.mainloop()