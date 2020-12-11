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

class TKinterTestCase(unittest.TestCase):
    def setUp(self):
        self.root= tkinter.Tk()
        self.view = MVC.View(self.root)
        self.model = MVC.Model()
        self.controller = MVC.Controller(self.view, self.model)
        self.pump_events()

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pump_events()

    def pump_events(self):
        while self.root.dooneevent(tkinter._tkinter.DONT_WAIT):
            pass


class TestInputEditor(TKinterTestCase):
    
    def test_Input(self):
        inputString = 'hi crocodile' + '\n'
        self.pump_events()
        self.view.inputeditor.insert('1.0', inputString)
        self.pump_events()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

    def test_Num_Input(self):
        inputString = '123'
        self.pump_events()
        self.view.inputeditor.insert('1.0', inputString)
        self.pump_events()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString + '\n')

    def test_Word_Input(self):
        inputString = 'test'
        self.pump_events()
        self.view.inputeditor.insert('1.0', inputString)
        self.pump_events()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString + '\n')

    # def test_Indent_Input(self):
    #     inputString = '    test'
    #     self.pump_events()
    #     self.view.inputeditor.insert('1.0', inputString)
    #     self.pump_events()
    #     self.assertEqual(self.view.outputbox.get("1.0", END), inputString + '\n')

#     def test_Space_Input(self):
#         inputString = ' '
#         self.pump_events()
#         self.view.inputeditor.insert('1.0', inputString)
#         self.pump_events()
#         self.assertEqual(self.view.outputbox.get("1.0", END), inputString + '\n')    

class TestOutputBox(TKinterTestCase):
    
    def test_Initial_Output(self):
        inputString = 'Welcome to Jotdown ✍️' + '\n'
        self.pump_events()
        self.view.outputbox.insert('1.0', inputString)
        self.pump_events()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)
  

class TestInput(TKinterTestCase):

    def test_Input(self):
        inputString = 'hi crocodile' + '\n'
        self.pump_events()
        self.view.inputeditor.insert('1.0', inputString)
        self.pump_events()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

    def test_Num_Input(self):
        inputString = '123'
        self.pump_events()
        self.view.inputeditor.insert('1.0', inputString)
        self.pump_events()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString + '\n')

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

    def test_decimals(self):
        inputString = '3.1415' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

    def test_decimalsAndInts(self):
        inputString = '3.1415 3' + '\n'
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
 
if __name__ == '__main__':
    unittest.main()
