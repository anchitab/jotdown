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

class TestInput(unittest.TestCase):

    def testBold(self):
        testString = '**hi crocodile**'
        # self.view = View()
        boldString = HTMLLabel(text='hi crocodile', font='bold')
        test = model.getHTML(testString)
        self.assertEqual(test, boldString)


if __name__ == '__main__':
    model = Model()
    unittest.main()




   

