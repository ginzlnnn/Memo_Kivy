# File name: desk.py
import kivy
kivy.require('1.9.0')

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class Desk(BoxLayout):
    fileSelect_name = StringProperty('')
    def selected(self, filename):
        self.fileSelect_name = filename[0].rsplit('/',1)[1]
        print('Filename : ' + self.fileSelect_name)
        self.status_bar.showName = self.fileSelect_name

