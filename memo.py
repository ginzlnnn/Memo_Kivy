import kivy
# kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty

Builder.load_file('memo.kv')  # load memo.kv File


class Memo(AnchorLayout):
    pass


class MemoApp(App):

    def build(self):
        return Memo()

if __name__ == "__main__":
    MemoApp().run()
