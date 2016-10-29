# File name: note.py
import kivy
kivy.require('1.9.0')

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file('savebar.kv')
Builder.load_file('writebox.kv')
Window.clearcolor = (1, 1, 1, 1)

class Note(Screen):
    pass
