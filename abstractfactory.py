import tkinter 
import os 

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import font, filedialog
from tkhtmlview import HTMLLabel

from tkinter import messagebox as mbox
from markdown2 import Markdown

from abc import ABCMeta, abstractstaticmethod

class ThemeCreator():
    @abstractstaticmethod
    def change_theme(self):
        pass

class NightThemeFactory(ThemeCreator):
    # Turn on Night Mode
    def __init__(self, inputEditor:Text, outputbox: HTMLLabel):
        self.inputEditor = inputEditor
        self.outputbox = outputbox
        

    


