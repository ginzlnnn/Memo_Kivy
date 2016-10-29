# File name: desk.py
import kivy
kivy.require('1.9.0')

from kivy.uix.boxlayout import BoxLayout


class Desk(BoxLayout):
    def selected(self, filename):
        name = filename[0].replace('/home/ginzlennontk/Desktop/memo/note/','')
        print('Filename : ' + name)

