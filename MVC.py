import tkinter 
import os     
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import font, filedialog
from tkhtmlview import HTMLLabel

from tkinter import messagebox as mbox
from markdown2 import Markdown

class View(Frame):
    def init_window(self, master = None):
        # Default window title when Jotdown opens
        Frame.__init__(self, master)
        self.master.title("Untitled - Jotdown")
        self.myfont = font.Font(family="Helvetica", size=14)
        self.pack(fill=BOTH, expand=1)
        # Allow left side to take in text
        self.inputeditor = Text(self, width="1", font = self.myfont, undo = True)
        # Set inputeditor on left side
        self.inputeditor.pack(fill = BOTH, expand = 1, side = LEFT)
        
        # Set outputbox on right side
        self.outputbox.pack(fill = BOTH, expand = 1, side = RIGHT)
        

class Model():   
    pass
    
class Controller():
    def __init__(self, view:View, model:Model) -> None:
        self.model = model
        self.view = view
        view.init_window(root)

root = Tk()
root.geometry("600x500")

#Run main application
view = View(root)
model = Model()
controller = Controller(view, model) 

root.mainloop()