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
        self.pump_events()

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pump_events()


class TestInput(TKinterTestCase):

    def test_Input(self):
        inputString = 'hi crocodile' + '\n'
        self.pump_events()
        self.view.inputeditor.insert('1.0', inputString)
        self.pump_events()
        self.assertEqual(self.view.outputbox.get("1.0", END), inputString)

 
if __name__ == '__main__':
    unittest.main()
