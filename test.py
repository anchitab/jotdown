import tkinter 
import os

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import font, filedialog
from tkhtmlview import HTMLLabel
from tkinter import messagebox as mbox
from markdown2 import Markdown

import unittest
import MVC
from MVC import *

class TKTestCase(unittest.TestCase):
    def setUp(self):
        self.root= tkinter.Tk()
        self.view = MVC.View(self.root)
        self.model = MVC.Model()
        self.controller = MVC.Controller(self.view, self.model)
        self.pumpEvents()

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pumpEvents()

    def pumpEvents(self):
        while self.root.dooneevent(tkinter._tkinter.DONT_WAIT):
            pass


class TestInputEditor(TKTestCase):
    
    def test_Input(self):
        inputString = 'hi crocodile' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

    def test_StringandInt_Input(self):
        inputString = 'hi 123 crocodiles' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

    def test_Special_Characters_Input(self):
        inputString = '!?~' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

    def test_All_Types_Input(self):
        inputString = 'hello 123 crocodiles!' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

class TestOutputBox(TKTestCase):
    
    def test_Initial_Output(self):
        inputString = 'Welcome to Jotdown ✍️' + '\n'
        self.pumpEvents()
        self.view.outputbox.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)
  

class TestInput(TKTestCase):

    def test_Input(self):
        inputString = 'hi crocodile' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

    def test_StringandInt(self):
        inputString = 'hi 123 crocodiles' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

    def test_Special_Characters(self):
        inputString = '!?@#$%^&*' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

    def test_All_Types(self):
        inputString = 'hello 123 crocodiles!' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

    def test_decimalsAndChars(self):
        inputString = '3.1415 pi' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

    def test_spaces(self):
        inputString = ' tests' + '\n'
        expectedString = 'tests' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), expectedString)

    def test_trailingSpaces(self):
        inputString = 'tests ' + '\n'
        expectedString = 'tests' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), expectedString)

class TestMarkdownFeatures(TKTestCase):
    def test_Bold(self):
        inputString = '**hi crocodile**' 
        expectedString = 'hi crocodile' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), expectedString)

    def test_Italics(self):
        inputString = '*hi crocodile*' 
        expectedString = 'hi crocodile' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), expectedString)

    def test_Bullets(self):
        inputString = '- carrots' + '\n' + '- hummus' + '\n' + '- celery'
        expectedString = '\n' + '\t•\t' + 'carrots\n' + '\t•\t' + 'hummus\n' + '\t•\t' + 'celery\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), expectedString)

    def test_Headers1(self):
        inputString = '#Biology'
        expectedString = 'Biology' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), expectedString)

    def test_Headers4(self):
        inputString = '####Biology'
        expectedString = 'Biology' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), expectedString)

if __name__ == '__main__':
    unittest.main()
