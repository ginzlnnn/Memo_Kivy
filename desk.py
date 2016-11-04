# File name: desk.py
import kivy
kivy.require('1.9.0')

from kivy.uix.boxlayout import BoxLayout

from kivy.properties import StringProperty

import os
 
class Desk(BoxLayout):                       # Desk class is a space for user to see files and select it
    fileSelect_name = StringProperty('')    # FilesSelect_name change when select another files
    def selected(self, filename):           
        try:
            self.fileSelect_name = os.path.basename(filename[0])
            print('Filename : ' + self.fileSelect_name)
        except:
            self.fileSelect_name = ''
        self.status_bar.showName = self.fileSelect_name

    def file_count(self, path):                   # Count files in floder 'note'
        list = os.listdir(path = path)    # list files in floder 'note'
        number = len(list)
        self.status_bar.total = number      # Value total in status_bar equal number

    def get_path(self):
        return self.filechooser.selection[0]
