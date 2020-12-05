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
        #Default window title when Jotdown opens
        Frame.__init__(self, master)
        self.master.title("Untitled - Jotdown")
        self.myfont = font.Font(family="Helvetica", size=14)

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
view = View()
model = Model()
controller = Controller(view, model) 

root.mainloop()