
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class WriteBox(RelativeLayout):
    def on_touch_up(self, touch):
        b = BoxLayout()
        textInput = TextInput(text='work')
        self.add_widget(b)
        b.add_widget(textInput)
        print(textInput)
        return b

if __name__ == "__main__":
    TutorialApp().run()
