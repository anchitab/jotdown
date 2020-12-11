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
from MVC import View
from MVC import Model

# # WORKING BASE TEST
# class GUITestCase(unittest.TestCase):
#     def test_helloworld(self):
#         testInput = "hello world"
#         self.assertEqual(testInput, "hello world")

# # run all tests from all sets
# if __name__ == "__main__":
#     unittest.main()

import time

class TKinterTestCase(unittest.TestCase):
    """These methods are going to be the same for every GUI test,
    so refactored them into a separate class
    """
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

    # def test_Bold(self):
    #     inputString = '*hi crocodile*'
    #     boldString = 'hi crocodile' 
    #     self.pump_events()
    #     self.view.inputeditor.insert('1.0', inputString)
    #     self.pump_events()
    #     self.assertEqual(self.view.outputbox.get("1.0", END), boldString)
 
if __name__ == '__main__':
    unittest.main()