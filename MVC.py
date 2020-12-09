import tkinter 
import os 

from command import *
from abstractfactory import *

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
        self.master.title("Untitled - Jotdown") 
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
        openFileCommand = OpenFileCommand(self.inputeditor)
        self.GUIFileMenu.add_command(label="Open", command=openFileCommand.execute)		
		
		# To save current file 	 
        saveFileCommand = SaveFileCommand(self.inputeditor)
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

        #creates ThemeFactory object
        themeFactory = ThemeFactory(self.inputeditor, self.outputbox)
       	# To give a feature of day mode
        self.GUIDisplayMenu.add_command(label="Daymode ☀️", command=themeFactory.getDayTheme)
        # To give a feature of night mode
        self.GUIDisplayMenu.add_command(label="Nightmode 🌙", command=themeFactory.getNightTheme)

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

class Command(View):
	def execute(self) -> None:
	    pass 

class OpenFileCommand(Command):
	def __init__(self, inputEditor: Text) -> None:
		self.inputEditor = inputEditor

	def execute(self) -> None:
		self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
		
		if self.file == "": 
			# if there is no file to open 
			self.file = None
		
		else: 	
			# Open the file 
			# Change window title 
			self.master.title(os.path.basename(self.file) + " - Jotdown") 
			self.inputEditor.delete(1.0,END)

			file = open(self.file,"r") 

			self.inputEditor.insert(1.0,file.read())

			file.close() 

class NewFileCommand(Command):
	def __init__(self, inputEditor: Text) -> None:
		self.inputEditor = inputEditor

	def execute(self) -> None:
		# print("reachednewfile")
		self.file = None
		self.inputEditor.delete(1.0,END)

class SaveFileCommand(Command):
	def __init__(self, inputEditor: Text) -> None:
		self.inputEditor = inputEditor

	def execute(self) -> None:
		if self.file == None: 
			# Save as new file + name file
			self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")]) 

			if self.file == "": 
				self.file = None
			else: 
				# Save the file 
				file = open(self.file,"w") 
				file.write(self.inputEditor.get(1.0,END)) 
				file.close() 
				
				# Set window title 
				self.master.title(os.path.basename(self.file) + " - Jotdown") 
		
		# If file already named save using that name (does not ask for user input)	
		else: 
			file = open(self.file,"w") 
			file.write(self.inputEditor.get(1.0,END))
			file.close()

class CopyCommand(Command):
	def __init__(self, inputEditor: Text) -> None:
		self.inputEditor = inputEditor

	def execute(self) -> None:
	    self.inputEditor.event_generate("<<Copy>>")

class CutCommand(Command):
	def __init__(self, inputEditor: Text) -> None:
		self.inputEditor = inputEditor

	def execute(self) -> None:
	    self.inputEditor.event_generate("<<Cut>>")

class PasteCommand(Command):
	def __init__(self, inputEditor: Text) -> None:
		self.inputEditor = inputEditor

	def execute(self) -> None:
	    self.inputEditor.event_generate("<<Paste>>")

class UndoCommand(Command):
	def __init__(self, inputEditor: Text) -> None:
		self.inputEditor = inputEditor

	def execute(self) -> None:
	    self.inputEditor.event_generate("<<Undo>>")

class RedoCommand(Command):
	def __init__(self, inputEditor: Text) -> None:
		self.inputEditor = inputEditor

	def execute(self) -> None:
	    self.inputEditor.event_generate("<<Redo>>")

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