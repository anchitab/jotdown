import tkinter 
import os	 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import font, filedialog
from tkhtmlview import HTMLLabel

from tkinter import messagebox as mbox
from markdown2 import Markdown

class GUIModel(Frame): 
	# Adds vertical scrollbar 
#	GUIScrollBar = Scrollbar(GUITextArea)	 
#	file = None

	def __init__(self, master=None):

		Frame.__init__(self, master)
		self.master = master
		self.myfont = font.Font(family="Helvetica", size=14)
		self.init_window()

	def init_window(self):
		# Default window title when Jotdown opens		
		self.master.title("Untitled - Jotdown")
		self.pack(fill=BOTH, expand=1)
		# Allow left side to take in text
		self.inputeditor = Text(self, width="1", font=self.myfont)
		# Set inputeditor on left side
		self.inputeditor.pack(fill=BOTH, expand=1, side=LEFT)
		# Set outputbox to display text
		self.outputbox = HTMLLabel(self, width="1", background="white", html="<h1> Welcome to Jotdown ✍️ </h1>")
		# Set outputbox on right side
		self.outputbox.pack(fill=BOTH, expand=1, side=RIGHT)
		self.outputbox.fit_height()
		self.inputeditor.bind("<<Modified>>", self.onInputChange)		
		self.GUIMenuBar = Menu(self) 
		self.GUIFileMenu = Menu(self.GUIMenuBar, tearoff=0) 
		self.GUIEditMenu = Menu(self.GUIMenuBar, tearoff=0) 
		self.GUIHelpMenu = Menu(self.GUIMenuBar, tearoff=0) 

		# Set jotdown.ico icon 
#		try: 
#				self.root.wm_iconbitmap("Jotdown.ico") 
#		except: 
#				pass

		# Let window size to change
		
		# try: 
		# 	self.thisWidth = kwargs['width'] 
		# except KeyError: 
		# 	pass

		# try: 
		# 	self.GUIHeight = kwargs['height'] 
		# except KeyError: 
		# 	pass
		# Center the window 
#		screenWidth = self.root.winfo_screenwidth() 
#		screenHeight = self.root.winfo_screenheight() 
	
		# For right-allign 
#		top = (screenHeight / 2) - (self.GUIHeight /2) 

		# For left-alling 
#		left = (screenWidth / 2) - (self.thisWidth / 2) 
		
		# For top and bottom 
#		self.root.geometry('%dx%d+%d+%d' % (self.thisWidth, self.GUIHeight, left, top)) 

		# Allow text to resize to window
		self.master.grid_rowconfigure(0, weight=1) 
		self.master.grid_columnconfigure(0, weight=1)  
		
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

		self.master.config(menu=self.GUIMenuBar)

#		self.GUIScrollBar.pack(side=RIGHT,fill=Y)					 
		
		# Scrollbar will adjust automatically according to the content		 
#		self.GUIScrollBar.config(command=self.GUITextArea.yview)	 
#		self.GUITextArea.config(yscrollcommand=self.GUIScrollBar.set) 
	
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
			self.master.title(os.path.basename(self.file) + " - Jotdown") 
			self.inputeditor.delete(1.0,END)

			file = open(self.file,"r") 

			self.inputeditor.insert(1.0,file.read())

			file.close() 

	def newFile(self): 
		self.master.title("Untitled - Jotdown") 
		self.file = None
		self.inputeditor.delete(1.0,END)

	def saveFile(self): 
		
		if self.file == None: 
			# Save as new file + name file
			self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")]) 

			if self.file == "": 
				self.file = None
			else: 
				
				# Save the file 
				file = open(self.file,"w") 
				file.write(self.inputeditor.get(1.0,END)) #
				file.close() 
				
				# Set window title 
				self.master.title(os.path.basename(self.file) + " - Jotdown") 
		
		# If file already named save using that name (does not ask for user input)	
		else: 
			file = open(self.file,"w") 
			file.write(self.inputeditor.get(1.0,END))
			file.close()  

	def copy(self): 
		self.inputeditor.event_generate("<<Copy>>") 

	def paste(self): 
		self.inputeditor.event_generate("<<Paste>>")

	def cut(self): 
		self.inputeditor.event_generate("<<Cut>>")

# Convert the inputer text to markdown and output converted text to outputbox
	def onInputChange(self, event):
		self.inputeditor.edit_modified(0)
		md2html = Markdown()
		markdownText = self.inputeditor.get("1.0", END)
		html = md2html.convert(markdownText)
		self.outputbox.set_html(html)	

root = Tk() 
root.geometry("600x500")

# Run main application 
Jotdown = GUIModel(root) 
Jotdown.mainloop()
