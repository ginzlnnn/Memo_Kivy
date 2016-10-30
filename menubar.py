# File name: menubar.py
import kivy
kivy.require('1.9.0')

from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

import os

class MenuBar(Screen):
    def add(self):
        content = Add(cancel=self.dismiss_popup, save=self.save)
        self._popup = Popup(title='Add Note', content=content, size_hint=(None, None), size=(500,500))
        self._popup.open()

    def open(self, path, filename):
        try:
            textfile = open(os.path.join(path, filename[0]))
            content = ShowText(text=textfile.read(),cancel=self.dismiss_popup)
            self._popup = Popup(title=os.path.basename(filename[0]), content=content, size_hint=(None, None), size=(500,500))
            self._popup.open()
            print(self.desk.fileSelect_name)
        except IndexError:
            print('Please Select File!!')

    def dismiss_popup(self):
        self._popup.dismiss()
        self.desk.filechooser._update_files()
        self.desk.filechooser.selection = []

    def delete(self):
        try:
            textfile = 'note/'+self.desk.fileSelect_name
            os.remove(textfile)
            self.desk.filechooser._update_files()
            self.desk.filechooser.selection = []
        except:
            print('Please Select File!!')

    def save(self, filename, content):
        textfile = open(os.path.join('note/', filename), 'w')
        textfile.write(content)

        self.dismiss_popup()

class ShowText(RelativeLayout):
    text = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Add(RelativeLayout):
    cancel = ObjectProperty(None)
    save = ObjectProperty(None)
