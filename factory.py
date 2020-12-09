import tkinter 
import os
from GUIModel import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import font, filedialog
from tkhtmlview import HTMLLabel

class ThemeFactory():
	def night_mode(self): pass
	def day_mode(self): pass


class NightThemeFactory(ThemeFactory):
	# Turn on Night Mode
	def night_mode(self):
		main_color = "#292a31"
		text_color = "white"

		self.inputeditor.config(bg=main_color, fg=text_color)
		self.outputbox.config(bg=main_color, fg=text_color)
		

class DayThemeFactory(ThemeFactory):
	# Turn On Day Mode:
	def day_mode(self):
		main_color = "SystemButtonFace"
		text_color = "black"

		root.config(bg=main_color)
		self.GUIFileMenu.config(bg=main_color, fg=text_color)
		self.GUIEditMenu.config(bg=main_color, fg=text_color)
		self.GUIDisplayMenu.config(bg=main_color, fg=text_color)
		self.GUIMenuBar.config(bg=main_color, fg=text_color)
		self.inputeditor.config(bg=main_color, fg=text_color)
		self.outputbox.config(bg=main_color, fg=text_color)