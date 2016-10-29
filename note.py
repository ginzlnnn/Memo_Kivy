# File name: note.py
import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
kivy.require('1.9.0')

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
Builder.load_file('savebar.kv')
Builder.load_file('writebox.kv')
Window.clearcolor = (1, 1, 1, 1)

class Note(Screen):
    def writeNote(self):
        b = BoxLayout()
        t = TextInput(font_size = 50)
        f = FloatLayout()
        b.add_widget(f)
        b.add_widget(t)
        
        return b
        

