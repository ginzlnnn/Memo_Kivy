# File name: desk.py
import kivy

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty

import os
import configparser

# Desk class is a space for user to see files and select it
class Desk(BoxLayout):
    # FilesSelect_name change when select another files
    fileSelect_name = StringProperty('')
    font_menu_size = NumericProperty(12)
    theme_red = NumericProperty(.4)
    theme_green = NumericProperty(.6)
    theme_blue = NumericProperty(1)

    def apply_setting(self):
        config = configparser.ConfigParser()
        config.read('setting.ini')
        self.font_menu_size = int(config['DEFAULT']['FontSize'])
        self.theme_red = float(config['DEFAULT']['ColorR'])
        self.theme_green = float(config['DEFAULT']['ColorG'])
        self.theme_blue = float(config['DEFAULT']['ColorB'])
        
    def selected(self, filename):
        try:
            self.fileSelect_name = os.path.basename(filename[0])
            print('Filename : ' + self.fileSelect_name)
        except:
            self.fileSelect_name = ''
        self.status_bar.showName = self.fileSelect_name

    def file_count(self, path):                   # Count files in floder
        list = os.listdir(path=path)    # list files in floder
        number = len(list)
        # Value total in status_bar equal number
        self.status_bar.total = number
        self.apply_setting() # For Test

    def get_path(self):
        return self.filechooser.selection[0]
