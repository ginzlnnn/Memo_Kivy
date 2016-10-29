# File names: memo.py
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty

'''Builder.load_file('menubar.kv')
Builder.load_file('desk.kv')
Builder.load_file('statusbar.kv')
Builder.load_file('note.kv')'''
loadscreen = Builder.load_file('screenmanager.kv')

class ScreenManager(AnchorLayout):
    pass
class ScreenmanagerApp(App):
    def build(self):
        return loadscreen   
if __name__ == "__main__":
    ScreenmanagerApp().run()