# File name: desk.py
import kivy
kivy.require('1.9.0')

from kivy.uix.boxlayout import BoxLayout

class Desk(BoxLayout):
    def selected(self, filename):
        name = filename[0].rsplit('/',1)[1]
        print('Filename : ' + name)
        self.status_bar.showName = name

