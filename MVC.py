import tkinter 
import os 

# import command
from command import *

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import font, filedialog
from tkhtmlview import HTMLLabel

from tkinter import messagebox as mbox
from markdown2 import Markdown

class View(Frame):
    
    file = None

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window(master)
		# self.invoker = Invoker()
        
    def init_window(self, master=None):
        # Default window title when Jotdown opens
        self.master.title("Untitled - Jotdown ✍️") 
        self.pack(fill=BOTH, expand=1)
        self.myfont = font.Font(family="Helvetica", size=14)
        
        # Allow left side to take in text
        self.inputeditor = Text(self, width="1", font=self.myfont, undo=True)
        # Set inputeditor on left side
        self.inputeditor.pack(fill=BOTH, expand=1, side=LEFT)
        # Set outputbox to display text
        self.outputbox = HTMLLabel(self, width="1", background="white", html="<h1> Welcome to Jotdown ✍️ </h1>")
        # Set outputbox on right side
        self.outputbox.pack(fill=BOTH, expand=1, side=RIGHT)
        self.outputbox.fit_height()

        # added new stuff
        self.GUIMenuBar = Menu(self)
        self.GUIFileMenu = Menu(self.GUIMenuBar, tearoff=0)
        self.GUIEditMenu = Menu(self.GUIMenuBar, tearoff=0)
        self.GUIHelpMenu = Menu(self.GUIMenuBar, tearoff=0)
        self.GUIDisplayMenu = Menu(self.GUIMenuBar, tearoff=0) 

		# Allow text to resize to window
        self.master.grid_rowconfigure(0, weight=1) 
        self.master.grid_columnconfigure(0, weight=1)  

		# To open new file  
        newFileCommand = NewFileCommand(self.inputeditor)
        self.GUIFileMenu.add_command(label="New", command=newFileCommand.execute)
	
		# To open a already existing file 
        openFileCommand = OpenFileCommand(self.inputeditor, master)
        self.GUIFileMenu.add_command(label="Open", command=openFileCommand.execute)		
		
		# To save current file 	 
        saveFileCommand = SaveFileCommand(self.inputeditor, master)
        self.GUIFileMenu.add_command(label="Save", command=saveFileCommand.execute)	 

		# To give a dropdown of File Menu
        self.GUIMenuBar.add_cascade(label="File", menu=self.GUIFileMenu)	 

		# To give a feature of undo 
        undoCommand = UndoCommand(self.inputeditor)
        self.GUIEditMenu.add_command(label="Undo", command=undoCommand.execute)	

		# To give a feature of redo
        redoCommand = RedoCommand(self.inputeditor) 
        self.GUIEditMenu.add_command(label="Redo", command=redoCommand.execute)
		
		# To give a feature of cut 
        cutCommand = CutCommand(self.inputeditor)
        self.GUIEditMenu.add_command(label="Cut", command=cutCommand.execute)			 
		
		# to give a feature of copy	 
        copyCommand = CopyCommand(self.inputeditor)
        self.GUIEditMenu.add_command(label="Copy", command=copyCommand.execute)
		
		# To give a feature of paste 
        pasteCommand = PasteCommand(self.inputeditor)
        self.GUIEditMenu.add_command(label="Paste", command=pasteCommand.execute)		 
		
		# To give a dropdown of Edit Menu
        self.GUIMenuBar.add_cascade(label="Edit", menu=self.GUIEditMenu)

        # To give a feature of night mode
        self.GUIDisplayMenu.add_command(label="Nightmode 🌙", command=self.night_mode)
       	 # To give a feature of day mode
        self.GUIDisplayMenu.add_command(label="Daymode ☀️", command=self.day_mode)
        # To give a dropdown of Display Menu
        self.GUIMenuBar.add_cascade(label="Display", menu=self.GUIDisplayMenu)
        
		# To create a feature of description of the notepad 
        self.GUIHelpMenu.add_command(label="About Jotdown", command=self.openAbout) 
        self.GUIMenuBar.add_cascade(label="Help", menu=self.GUIHelpMenu)

        self.master.config(menu=self.GUIMenuBar)

    def openAbout(self):
        showinfo("Jotdown","A minimal text editor for students, by students.") 

    def getMarkdownText(self):
        markdownText = self.inputeditor.get("1.0", END)
        return markdownText

    def outputText(self, html):
        self.outputbox.set_html(html)

class Model():  

    def __init__(self):
        self.md2html = Markdown()

    def getHTML(self, markdownText:Text):
        html = self.md2html.convert(markdownText)        
        return html


class Controller():
	def __init__(self, view:View, model:Model) -> None:
		self.model = model
		self.view = view
		self.view.inputeditor.bind("<<Modified>>", self.processInputText)
		
	def processInputText(self, event):
		view.inputeditor.edit_modified(0)
		markdownText = view.getMarkdownText()
		html = model.getHTML(markdownText)
		view.outputText(html)
        
root = Tk() 
root.geometry("600x500") 

# Run main application 
view = View(root)
model = Model()
controller = Controller(view, model)

root.mainloop()