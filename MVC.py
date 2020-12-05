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
        self.inputeditor = Text(self, width = "1", font = self.myfont, undo = True)
        # Set inputeditor on left side
        self.inputeditor.pack(fill = BOTH, expand = 1, side = LEFT)
        # Set outputbox to display text
        self.outputbox = HTMLLabel(self, width = "1", background = "white", html = "<h1> Welcome to Jotdown ✍️ </h1>")
        # Set outputbox on right side
        self.outputbox.pack(fill = BOTH, expand = 1, side = RIGHT)
        self.outputbox.fit_height()
        # Create event where 
        self.inputeditor.bind("<<Modified>>", self.inputText)

    def inputText(self):
        self.inputeditor.edit_modified(0)

    def getMarkdownText(self):
        markdownText = self.inputeditor.get("1.0", END)
        return markdownText

    def outputText(self, html)
        self.outputbox.set_html(html)

class Model():   
    def onInputChange(self):
        self.md2html = Markdown()
    
    def getHTML(self, markdownText):
            html = self.md2html.convert(markdownText)
            return html

class Controller():
    def __init__(self, view:View, model:Model) -> None:
        self.model = model
        self.view = view
        view.init_window(root)
        model.onInputChange()
        markdownText = view.getMarkdownText()
        html = model.getHTML(markdownText)
        view.outputText(html)

root = Tk()
root.geometry("600x500")

#Run main application
view = View(root)
model = Model()
controller = Controller(view, model) 

root.mainloop()