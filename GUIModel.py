import tkinter 
import os	 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class GUIModel: 

	root = Tk() 

	# Window default sizing
	GUIWidth = 300
	GUIHeight = 300
	GUITextArea = Text(root)
	GUIMenuBar = Menu(root) 
	GUIFileMenu = Menu(GUIMenuBar, tearoff=0) 
	GUIEditMenu = Menu(GUIMenuBar, tearoff=0) 
	GUIHelpMenu = Menu(GUIMenuBar, tearoff=0) 
	
	# Adds vertical scrollbar 
	GUIScrollBar = Scrollbar(GUITextArea)	 
	file = None

	def __init__(self,**kwargs): 

		# Set jotdown.ico icon 
		try: 
				self.root.wm_iconbitmap("Jotdown.ico") 
		except: 
				pass

		# Let window size to change

		try: 
			self.thisWidth = kwargs['width'] 
		except KeyError: 
			pass

		try: 
			self.GUIHeight = kwargs['height'] 
		except KeyError: 
			pass

		# Default window title when Jotdown opens
		self.root.title("Untitled - Jotdown") 

		# Center the window 
		screenWidth = self.root.winfo_screenwidth() 
		screenHeight = self.root.winfo_screenheight() 
	
		# For right-allign 
		top = (screenHeight / 2) - (self.GUIHeight /2) 

		# For left-alling 
		left = (screenWidth / 2) - (self.thisWidth / 2) 
		
		# For top and bottom 
		self.root.geometry('%dx%d+%d+%d' % (self.thisWidth, self.GUIHeight, left, top)) 

		# Allow text to resize to window
		self.root.grid_rowconfigure(0, weight=1) 
		self.root.grid_columnconfigure(0, weight=1) 

		# Add controls (widget) 
		self.GUITextArea.grid(sticky = N + E + S + W) 
		
		# To open new file 
		self.GUIFileMenu.add_command(label="New", command=self.newFile)	 
		
		# To open a already existing file 
		self.GUIFileMenu.add_command(label="Open", command=self.openFile) 
		
		# To save current file 
		self.GUIFileMenu.add_command(label="Save", command=self.saveFile)	 

		self.GUIMenuBar.add_cascade(label="File", menu=self.GUIFileMenu)	 
		
		# To give a feature of cut 
		self.GUIEditMenu.add_command(label="Cut", command=self.cut)			 
	
		# to give a feature of copy	 
		self.GUIEditMenu.add_command(label="Copy", command=self.copy)		 
		
		# To give a feature of paste 
		self.GUIEditMenu.add_command(label="Paste", command=self.paste)		 
		
		# To give a feature of editing 
		self.GUIMenuBar.add_cascade(label="Edit", menu=self.GUIEditMenu)	 
		
		# To create a feature of description of the notepad 
		self.GUIHelpMenu.add_command(label="About Jotdown", command=self.openAbout) 
		self.GUIMenuBar.add_cascade(label="Help", menu=self.GUIHelpMenu) 

		self.root.config(menu=self.GUIMenuBar) 

		self.GUIScrollBar.pack(side=RIGHT,fill=Y)					 
		
		# Scrollbar will adjust automatically according to the content		 
		self.GUIScrollBar.config(command=self.GUITextArea.yview)	 
		self.GUITextArea.config(yscrollcommand=self.GUIScrollBar.set) 
	
	def openAbout(self): 
		showinfo("Jotdown","A minimal text editor for students, by students.") 

	def openFile(self): 
		
		self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")]) 

		if self.file == "": 
			
			# if there is no file to open 
			self.file = None
		else: 
			
			# Open the file 
			# Change window title 
			self.root.title(os.path.basename(self.file) + " - Jotdown") 
			self.GUITextArea.delete(1.0,END) 

			file = open(self.file,"r") 

			self.GUITextArea.insert(1.0,file.read()) 

			file.close() 

	def newFile(self): 
		self.root.title("Untitled - Jotdown") 
		self.file = None
		self.GUITextArea.delete(1.0,END) 

	def saveFile(self): 

		if self.file == None: 
			# Save as new file + name file
			self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")]) 

			if self.file == "": 
				self.file = None
			else: 
				
				# Save the file 
				file = open(self.file,"w") 
				file.write(self.GUITextArea.get(1.0,END)) 
				file.close() 
				
				# Set window title 
				self.root.title(os.path.basename(self.file) + " - Jotdown") 
				
			
		else: 
			file = open(self.file,"w") 
			file.write(self.GUITextArea.get(1.0,END)) 
			file.close()  

	def copy(self): 
		self.GUITextArea.event_generate("<<Copy>>") 

	def paste(self): 
		self.GUITextArea.event_generate("<<Paste>>") 

	def cut(self): 
		self.GUITextArea.event_generate("<<Cut>>")

	def run(self): 

		# Run main application 
		self.root.mainloop() 


# Run main application 
Jotdown = GUIModel(width=600,height=400) 
Jotdown.run()