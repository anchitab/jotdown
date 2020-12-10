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

class TestInput(unittest.TestCase):

    def test_Input(self):
        testString = 'hi crocodile'
        root = Tk()
        view = View(root)
        view.inputeditor.insert('1.0', testString)
        # view.inputeditor.edit_modified(1)
        view.inputeditor.event_generate("<<Modified>>")
        self.assertEqual(view.outputbox.get(1.0, END), testString)

 
if __name__ == '__main__':
    # root = Tk()
    # # model = Model()
    # view = View(root)
    unittest.main()

# def test_Bold(self):
#         testString = '**hi crocodile**'
#         # self.view = View()
#         boldString = HTMLLabel(text='hi crocodile', font='bold')
#         test = model.getHTML(testString)
#         self.assertEqual(test, boldString)

   # def test_input(self):
    #     testString = "hi crocodile"
    #     root = Tk()
    #     self.view = View(root)
    #     # self.model = Model()
    #     testInput = view.inputeditor.set(testString)
    #     testOutput = view.outputbox.get(1.0, END)
    #     self.assertEqual(testInput, testOutput)

   

    # def test(self):
    #     testString = "hi crocodile"
    #     # self.view = view
    #     # self.model = model
    #     # self.view = View()
    #     # self.model= Model()
    #     testInput = view.inputeditor.get(testString)
    #     testOutput = model.getHTML(testInput)
    #     self.assertEqual(testInput, testOutput)

    # from mock import Mock

# class GUITestCase(unittest.TestCase):
#     def setUp(self):
#         root = Tk()
#         self.view = View(root)

#     # def tearDown(self):
#     #     view.destroy()

#     def test_geometry(self):
#         root.winfo_geometry()

# # run all tests from all sets
# if __name__ == "__main__":
#     unittest.main()
