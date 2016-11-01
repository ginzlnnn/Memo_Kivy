# File name: desk.py
import kivy
kivy.require('1.9.0')

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

import os

class Desk(BoxLayout):
    fileSelect_name = StringProperty('')
    def selected(self, filename):
        try:
            self.fileSelect_name = os.path.basename(filename[0])
            print('Filename : ' + self.fileSelect_name)
        except:
            self.fileSelect_name = ''
        self.status_bar.showName = self.fileSelect_name

    def file_count(self):
        list = os.listdir(path = 'note')
        number = len(list)
        print(list)
        self.status_bar.total = number
