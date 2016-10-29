# File name: menubar.py
import kivy
kivy.require('1.9.0')

from kivy.uix.screenmanager import ScreenManager, Screen

import os

class MenuBar(Screen):
    def open(self, path, filename):
        try:
            f = open(os.path.join(path, filename[0]))
            print(f.read())
        except IndexError:
            print('Please Select File!!')
