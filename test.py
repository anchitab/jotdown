from Tkinter import *
import unittest
import MVC

class TestInput(unittest.TestCase):

     def test(self):
        a = classTest.App(Tk())
        self.assertEqual(a.printy(),"test")

if __name__ == '__main__':
    unittest.main()




   

