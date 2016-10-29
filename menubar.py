# File name: menubar.py
import kivy
kivy.require('1.9.0')

from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

import os

class MenuBar(Screen):
    def open(self, path, filename):
        box = BoxLayout()
        try:
            f = open(os.path.join(path, filename[0]))
            box.add_widget(Label(text=f.read()))
            popup = Popup(title=self.desk.fileSelect_name, content=box, size_hint=(None, None), size=(300, 300))
            print(self.desk.fileSelect_name)
            popup.open()
        except IndexError:
            print('Please Select File!!')
