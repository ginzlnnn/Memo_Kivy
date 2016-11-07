# File name: desk.py
import kivy

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

import os


# Desk class is a space for user to see files and select it
class Desk(BoxLayout):
    # FilesSelect_name change when select another files
    fileSelect_name = StringProperty('')

    def selected(self, filename):
        try:
            self.fileSelect_name = os.path.basename(filename[0])
            print('Filename : ' + self.fileSelect_name)
        except:
            self.fileSelect_name = ''
        self.status_bar.showName = self.fileSelect_name

    def file_count(self, path):                   # Count files in floder
        list = os.listdir(path=path)    # list files in floder
        number = len(list)
        # Value total in status_bar equal number
        self.status_bar.total = number

    def get_path(self):
        return self.filechooser.selection[0]
