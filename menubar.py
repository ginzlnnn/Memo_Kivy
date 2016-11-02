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
    
class MenuBar(Screen):              # Class MenuBar. 
    def dismiss_popup(self):        # Closed current popup and then update files.
        self._popup.dismiss()       
        self.desk.filechooser._update_files()

    def add(self):                  # Create Add note popup that have two button save and cancel.
        content = Add(cancel=self.dismiss_popup, save=self.save)                        # Content is Add class that have 2 button 
                                                                                        # Cancel button call dissmis_popup method,save button call save method,
        self._popup = Popup(title='Add Note', title_font='Waree', content=content,      # Set title name to 'Add Note' and make popup closed manually
                            auto_dismiss=False, size_hint=(None, None), size=(500,500)) # Popup size is 500, 500
        self._popup.open()                                                              # Open popup after create finish.

    def edit(self, path, filename):        
        try:
            textfile = open(os.path.join(path, filename[0]))
            content = Add(cancel=self.dismiss_popup, save=self.save)
            content.text_name.text = os.path.basename(filename[0])
            content.text_content.text = textfile.read()
            self._popup = Popup(title='Edit Note', title_font='Waree', content=content,
                                auto_dismiss=False, size_hint=(None, None), size=(500,500))
            self._popup.open()
        except IndexError:
            self.error_popup('Please Select File!!')

    def open(self, path, filename):
        try:
            textfile = open(os.path.join(path, filename[0]))
            content = ShowText(text=textfile.read(),cancel=self.dismiss_popup)
            self._popup = Popup(title=os.path.basename(filename[0]), title_font='Waree',
                                auto_dismiss=False, content=content, size_hint=(None, None),
                                size=(500,500))
            self._popup.open()
        except IndexError:
            self.error_popup('Please Select File!!')

    def show_delete(self):
        sel = self.desk.filechooser.selection
        if(sel == []):
            self.error_popup('Please Select File!!')
        else:
            content = DeleteFile(delete = self.delete, no=self.dismiss_popup)
            self._popup = Popup(title="Delete file", content=content, auto_dismiss=False, 
                            size_hint=(0.5, 0.2))
            self._popup.open()
            
    def delete(self):
        textfile = 'note/'+self.desk.fileSelect_name
        print(textfile)
        os.remove(textfile)
        self.desk.filechooser.selection = []
        self.dismiss_popup()

    def save(self, filename, content):
        if(len(filename) == 0):
            self.error_popup('Enter Filename!!')

        else:
            textfile = open(os.path.join('note/', filename), 'w')
            textfile.write(content)
            self.desk.filechooser.selection = []
            self.dismiss_popup()

    def error_popup(self, error_text):
        content = ShowError()
        content.text_error.text = error_text
        self.popup_error = Popup(title='Error!', content=content, auto_dismiss=False, 
                            size_hint=(None, None), size=(200,200))
        content.cancel.bind(on_press=self.popup_error.dismiss)

        self.popup_error.open()

class TextMenu(MenuBar):
    def delete(self):
        pass

class PictureMenu(MenuBar):
    def delete(self):
        pass

class DeleteButton():
    pass

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
    pass
