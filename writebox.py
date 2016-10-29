from kivy.uix.relativelayout import RelativeLayout
class WriteBox(RelativeLayout):
    def on_touch_down(self, touch):
        print('work')