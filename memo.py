# File names: memo.py
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_file('menubar.kv')
Builder.load_file('desk.kv')
Builder.load_file('statusbar.kv')
Builder.load_file('note.kv')

class Memo(AnchorLayout):
    pass

class MemoApp(App):
    def build(self):
        return Memo()
    
if __name__ == "__main__":
    MemoApp().run()