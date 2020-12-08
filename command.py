import tkinter 
import os 

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import font, filedialog
from tkhtmlview import HTMLLabel

from tkinter import messagebox as mbox
from markdown2 import Markdown

class Command():
	def __init__(self):
		self.file = None
	# 	self.master = None

	def execute(self) -> None:
	    pass 

class OpenFileCommand(Command):
	def __init__(self, inputEditor: Text, master:Tk) -> None:
		self.inputEditor = inputEditor
		self.master = master

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
	def __init__(self, inputEditor: Text, master:Tk) -> None:
		self.inputEditor = inputEditor
		self.master = master
		self.file = None

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
			print("it came here")
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