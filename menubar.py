# File name: menubar.py
import kivy
kivy.require('1.9.0')

from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView

import os

class MenuBar(Screen):
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
            print('Please Select File!!')

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_delete(self):
        sel = self.desk.filechooser.selection
        if(sel == []):
            print('Please Select File!!')
        else:
            content = DeleteFile(delete = self.delete, no=self.dismiss_popup)
            self._popup = Popup(title="Delete file", content=content,
                            size_hint=(0.5, 0.2))
            self._popup.open()
            
    def delete(self):
        textfile = 'note/'+self.desk.fileSelect_name
        os.remove(textfile)
        self.desk.filechooser._update_files()
        self.desk.filechooser.selection = []
        self.dismiss_popup()

class DeleteFile(RelativeLayout):
    delete = ObjectProperty(None)
    no = ObjectProperty(None)
    
class ShowText(RelativeLayout):
    text = ObjectProperty(None)
    cancel = ObjectProperty(None)


