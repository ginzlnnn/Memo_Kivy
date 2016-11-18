import kivy
import configparser
# kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty, NumericProperty

Builder.load_file('memo.kv')  # load memo.kv File


class Memo(RelativeLayout):
    titlebar_red = NumericProperty()
    titlebar_green = NumericProperty()
    titlebar_blue = NumericProperty()
    

    def apply_setting(self):
        config = configparser.ConfigParser()
        config.read('setting.ini')
        self.desk.font_menu_size = config.getint('DEFAULT', 'FontSize')
        self.menubar.theme_red = \
            self.titlebar_red = config.getfloat('DEFAULT', 'ColorR')
        self.menubar.theme_green = \
            self.titlebar_green = config.getfloat('DEFAULT', 'ColorG')
        self.menubar.theme_blue = \
            self.titlebar_blue = config.getfloat('DEFAULT', 'ColorB')


class MemoApp(App):

    def build(self):
        app = Memo()
        app.apply_setting()
        return app

if __name__ == "__main__":
    MemoApp().run()
