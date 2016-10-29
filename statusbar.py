# File name: statusbar.py
import kivy
kivy.require('1.9.0')

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class StatusBar(BoxLayout):
    showName = StringProperty('')