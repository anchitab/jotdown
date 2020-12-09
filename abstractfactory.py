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


