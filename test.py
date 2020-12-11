import tkinter 
import os 

from command import *
from factory import *

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
        self.pumpEvents()

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pumpEvents()

    def pumpEvents(self):
        while self.root.dooneevent(tkinter._tkinter.DONT_WAIT):
            pass


class TestInput(TKinterTestCase):

    def test_Input(self):
        inputString = 'hi crocodile' + '\n'
        self.pumpEvents()
        self.view.inputeditor.insert('1.0', inputString)
        self.pumpEvents()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

    def test_Integers(self):
        inputString = '123' + '\n'
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

 
if __name__ == '__main__':
    unittest.main()
