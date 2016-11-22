import kivy
import configparser
# kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty, NumericProperty, ListProperty, StringProperty

Builder.load_file('memo.kv')  # load memo.kv File


class Memo(RelativeLayout):
    titlebar_red = NumericProperty()
    titlebar_green = NumericProperty()
    titlebar_blue = NumericProperty()
    wallpaper = StringProperty('')

    def setting(self):
        content = Setting(set_color = self.set_color,
                          set_textsize = self.set_textsize,
                          font_size = self.menubar.font_menu_size,
                          default = self.load_default,
                          close = self.apply_setting,
                          wallpaper = self.wallpaper,
                          color = (self.titlebar_red,self.titlebar_green,
                                   self.titlebar_blue, 1))
        self._popup = Popup(title='SETTING', title_font='Waree',
                            title_size = self.menubar.font_menu_size,
                            auto_dismiss=False, content=content,
                            size_hint=(None, None), size=(600, 600))
        self._popup.open()

    def dismiss_popup(self):  # Closed current popup and then update files.
        self._popup.dismiss()   

    def set_textsize(self, size):
        self.menubar.font_menu_size = int(size)
        
    def set_color(self, color):
        self.menubar.theme_red = self.titlebar_red = color[0]
        self.menubar.theme_green = self.titlebar_green = color[1]
        self.menubar.theme_blue = self.titlebar_blue = color[2]
        
    def apply_setting(self, wallpaper):
        config = configparser.ConfigParser()
        config.read('setting.ini', encoding=('utf-8'))
        config['USER']['FontSize'] = str(self.menubar.font_menu_size) 
        config['USER']['ColorR'] = str(self.menubar.theme_red)
        config['USER']['ColorG'] = str(self.menubar.theme_green)
        config['USER']['ColorB'] = str(self.menubar.theme_blue)
        config['USER']['wallpaper'] = wallpaper
        self.wallpaper = wallpaper
        with open('setting.ini', 'w', encoding=('utf-8')) as configfile:
            config.write(configfile)
        self.dismiss_popup()
        
    def load_default(self):
        config = configparser.ConfigParser()
        config.read('setting.ini', encoding=('utf-8'))
        config['USER']['FontSize'] = config['DEFAULT']['FontSize']
        config['USER']['ColorR'] = config['DEFAULT']['ColorR']
        config['USER']['ColorB'] = config['DEFAULT']['ColorB']
        config['USER']['ColorG'] = config['DEFAULT']['ColorG']
        config['USER']['wallpaper'] = config['DEFAULT']['wallpaper']
        with open('setting.ini', 'w', encoding=('utf-8')) as configfile:
            config.write(configfile)
        self.load_setting()
        self.dismiss_popup()
        
    def load_setting(self):
        config = configparser.ConfigParser()
        config.read('setting.ini', encoding=('utf-8'))
        self.menubar.font_menu_size = config.getint('USER', 'FontSize')
        self.menubar.theme_red = \
            self.titlebar_red = config.getfloat('USER', 'ColorR')
        self.menubar.theme_green = \
            self.titlebar_green = config.getfloat('USER', 'ColorG')
        self.menubar.theme_blue = \
            self.titlebar_blue = config.getfloat('USER', 'ColorB')
        self.wallpaper = config['USER']['wallpaper']

class Setting(RelativeLayout):
    close = ObjectProperty(None)
    set_color = ObjectProperty(None)
    set_textsize = ObjectProperty(None)
    font_size = ObjectProperty(None)
    color = ObjectProperty(None)
    default = ObjectProperty(None)
    wallpaper = ObjectProperty(None)
    import_file = ObjectProperty(None)
    
    def load_wallpaper(self):
        content = ImportWallpaper(import_wallpaper=self.import_wallpaper,
                                source=str(self.wallpaper),
                                cancel=self.dismiss_popup)
        self._popup = Popup(title='Choose Wallpaper', title_font='Waree',
                            auto_dismiss=False, content=content,
                            size_hint=(None, None), size=(600, 600))
        self._popup.open()

    def import_wallpaper(self, path):
        self.wallpaper = path
        self.dismiss_popup()
        
    def dismiss_popup(self):  # Closed current popup and then update files.
        self._popup.dismiss()


class ImportWallpaper(RelativeLayout):
    import_wallpaper = ObjectProperty(None)
    source = StringProperty('')
    cancel = ObjectProperty(None)

    def show_picture(self, path):
        try:
            self.source = str(path[0])
        except:
            self.source = ''

            
class MemoApp(App):
    
    def build(self):
        app = Memo()
        app.load_setting()
        return app

if __name__ == "__main__":
    MemoApp().run()
