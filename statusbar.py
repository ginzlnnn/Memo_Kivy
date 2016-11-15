# File name: statusbar.py
import kivy
# kivy.require('1.9.0')

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty


class StatusBar(BoxLayout):             # Show details about desk screen
    # showName keep Files name and send value to statusbar.kv file
    showName = StringProperty('')
    # total keep total in desk screen and send value to statusbar.kv file
    total = NumericProperty(0)
