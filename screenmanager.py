# File names: memo.py
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty

loadscreen = Builder.load_file('screenmanager.kv')      #load screenmanager.kv File

class ScreenManager(AnchorLayout):
    pass
class ScreenmanagerApp(App):
    def build(self):
        return loadscreen   
if __name__ == "__main__":
    ScreenmanagerApp().run()
