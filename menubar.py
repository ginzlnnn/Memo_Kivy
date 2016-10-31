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
        self._popup = Popup(title='Add Note', content=content,
                            size_hint=(None, None), size=(500,500))
        self._popup.open()

    def edit(self, path, filename):        
        try:
            textfile = open(os.path.join(path, filename[0]))
            content = Add(cancel=self.dismiss_popup, save=self.save)
            content.text_name.text = os.path.basename(filename[0])
            content.text_content.text = textfile.read()
            self._popup = Popup(title='Edit Note', content=content,
                                size_hint=(None, None), size=(500,500))
            self._popup.open()
        except IndexError:
            self.error_popup('Please Select File!!')

    def open(self, path, filename):
        try:
            textfile = open(os.path.join(path, filename[0]))
            content = ShowText(text=textfile.read(),cancel=self.dismiss_popup)
            self._popup = Popup(title=os.path.basename(filename[0]),
                                content=content, size_hint=(None, None),
                                size=(500,500))
            self._popup.open()
            print(self.desk.fileSelect_name)
        except IndexError:
            self.error_popup('Please Select File!!')

    def dismiss_popup(self):
        self._popup.dismiss()
        self.desk.filechooser._update_files()

    def show_delete(self):
        sel = self.desk.filechooser.selection
        if(sel == []):
            self.error_popup('Please Select File!!')
        else:
            content = DeleteFile(delete = self.delete, no=self.dismiss_popup)
            self._popup = Popup(title="Delete file", content=content,
                            size_hint=(0.5, 0.2))
            self._popup.open()
            
    def delete(self):
        textfile = 'note/'+self.desk.fileSelect_name
        os.remove(textfile)
        self.desk.filechooser.selection = []
        self.dismiss_popup()

    def save(self, filename, content):
        if(len(filename) == 0):
            self.dismiss_popup()
            add_again = Add(cancel=self.dismiss_popup, save=self.save)
            add_again.text_name.text = 'Enter Filename!!'
            add_again.text_content.text = content
            self._popup = Popup(title='Add Note', content=add_again,
                            size_hint=(None, None), size=(500,500))
            self._popup.open()

        else:
            textfile = open(os.path.join('note/', filename), 'w')
            textfile.write(content)
            self.desk.filechooser.selection = []
            self.dismiss_popup()

    def error_popup(self, error_text):
        content = ShowError(cancel=self.dismiss_popup)
        content.text_error.text = error_text
        self._popup = Popup(title='Error!', content=content, 
                            size_hint=(None, None), size=(200,200))
        self._popup.open()

class DeleteFile(RelativeLayout):
    delete = ObjectProperty(None)
    no = ObjectProperty(None)

class ShowText(RelativeLayout):
    text = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Add(RelativeLayout):
    cancel = ObjectProperty(None)
    save = ObjectProperty(None)

class ShowError(RelativeLayout):
    cancel = ObjectProperty(None)
