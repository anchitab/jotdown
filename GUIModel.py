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


root = Tk() 
root.geometry("600x500")

# Run main application 
Jotdown = GUIModel(root) 
Jotdown.mainloop()
