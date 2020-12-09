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

    def change_theme(self):
        print("NIGHTTHEMEFACTORY")
        
        main_color = "#292a31"
        text_color = "white"
        self.inputEditor.config(bg=main_color, fg=text_color)
        self.outputbox.config(bg=main_color, fg=text_color)
        

class DayThemeFactory(ThemeCreator):
    def __init__(self, inputEditor:Text, outputbox: HTMLLabel):
        self.inputEditor = inputEditor
        self.outputbox = outputbox

    # Turn On Day Mode:
    def change_theme(self):
        print("DAYTHEMEFACTORY")

        main_color = "SystemButtonFace"
        text_color = "black"
        
        self.inputEditor.config(bg=main_color, fg=text_color)
        self.outputbox.config(bg=main_color, fg=text_color)

class themeFactory():
    def __init__(self, inputEditor:Text, outputbox: HTMLLabel):
        self.inputEditor = inputEditor
        self.outputbox = outputbox
    
    # @staticmethod
    def getTheme(self, themeType):        
        print("THEMEFACTORY")
        print(themeType)

        if themeType == "NightMode":
            return NightThemeFactory(self.inputEditor, self.outputbox)
        if themeType == "DayMode":
            return DayThemeFactory(self.inputEditor, self.outputbox)

        # try:
        #     if themeType == "NightMode":
        #         return NightThemeFactory(self.inputEditor, self.outputbox)
        #     if themeType == "DayMode":
        #         return DayThemeFactory(self.inputEditor, self.outputbox)
        #     raise AssertionError("Theme not found")
        # except AssertionError as _e:
        #     print(_e)