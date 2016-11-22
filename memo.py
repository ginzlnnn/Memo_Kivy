import kivy
import configparser
# kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty, NumericProperty, ListProperty

Builder.load_file('memo.kv')  # load memo.kv File


class Memo(RelativeLayout):
    titlebar_red = NumericProperty()
    titlebar_green = NumericProperty()
    titlebar_blue = NumericProperty()

    def setting(self):
        content = Setting(set_color = self.set_color,
                          default = self.load_default,
                          close = self.apply_setting,
                          color = (self.titlebar_red,self.titlebar_green,
                                   self.titlebar_blue, 1))
        self._popup = Popup(title='SETTING', title_font='Waree',
                            auto_dismiss=False, content=content,
                            size_hint=(None, None), size=(600, 500))
        self._popup.open()

    def dismiss_popup(self):  # Closed current popup and then update files.
        self._popup.dismiss()   
    
    def set_color(self, color):
        self.menubar.theme_red = self.titlebar_red = color[0]
        self.menubar.theme_green = self.titlebar_green = color[1]
        self.menubar.theme_blue = self.titlebar_blue = color[2]
        
    def apply_setting(self):
        config = configparser.ConfigParser()
        config.read('setting.ini')
        config['USER']['FontSize'] = str(self.desk.font_menu_size) 
        config['USER']['ColorR'] = str(self.menubar.theme_red)
        config['USER']['ColorB'] = str(self.menubar.theme_green)
        config['USER']['ColorG'] = str(self.menubar.theme_blue)
        with open('setting.ini', 'w') as configfile:
            config.write(configfile)
        self.dismiss_popup()
        
    def load_default(self):
        config = configparser.ConfigParser()
        config.read('setting.ini')
        self.desk.font_menu_size = config.getint('DEFAULT', 'FontSize')
        self.menubar.theme_red = \
            self.titlebar_red = config.getfloat('DEFAULT', 'ColorR')
        self.menubar.theme_green = \
            self.titlebar_green = config.getfloat('DEFAULT', 'ColorG')
        self.menubar.theme_blue = \
            self.titlebar_blue = config.getfloat('DEFAULT', 'ColorB')
        self.dismiss_popup()
        
    def load_setting(self):
        config = configparser.ConfigParser()
        config.read('setting.ini')
        self.desk.font_menu_size = config.getint('USER', 'FontSize')
        self.menubar.theme_red = \
            self.titlebar_red = config.getfloat('USER', 'ColorR')
        self.menubar.theme_green = \
            self.titlebar_green = config.getfloat('USER', 'ColorG')
        self.menubar.theme_blue = \
            self.titlebar_blue = config.getfloat('USER', 'ColorB')

class Setting(RelativeLayout):
    close = ObjectProperty(None)
    set_color = ObjectProperty(None)
    color = ObjectProperty(None)
    default = ObjectProperty(None)
    
class MemoApp(App):
    
    def build(self):
        app = Memo()
        app.load_setting()
        return app

if __name__ == "__main__":
    MemoApp().run()
