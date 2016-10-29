
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix import label


class WriteBox(RelativeLayout):
    def on_touch_down(self, touch):
        print('call input text i hope?')
if __name__ == "__main__":
    TutorialApp().run()
