# File name: statusbar.py
import kivy
kivy.require('1.9.0')

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty

class StatusBar(BoxLayout):
    showName = StringProperty('')
    total = NumericProperty(0)
    
    
