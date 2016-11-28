from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
# File name: menubar.py
import kivy
import os
import shutil
import configparser
import fnmatch


kivy.require('1.9.0')


class MenuBar(Screen):  # Class MenuBar.
    font_menu_size = NumericProperty(12)
    theme_red = NumericProperty()
    theme_green = NumericProperty()
    theme_blue = NumericProperty()

    def dismiss_popup(self):  # Closed current popup and then update files.
        self._popup.dismiss()
        self.desk.filechooser._update_files()

    def open(self, path, filename):
        try:
            if fnmatch.fnmatch(filename[0],'*.txt'):
                textfile = open(os.path.join(path, filename[0]),
                                encoding=('utf-8'))
                content = ShowText(text=textfile.read(),
                                   cancel=self.dismiss_popup)
            else:
                content = ShowPicture(source=self.desk.get_path(),
                                      cancel=self.dismiss_popup)
            self._popup = Popup(title=os.path.basename(
                    self.desk.get_path()), title_font='Waree',
                                    auto_dismiss=False, content=content,
                                    size_hint=(None, None), size=(500, 500))
            self._popup.open()
        except IndexError:
            self.error_popup('Please Select File!!')

    # Create Add note popup that have two button save and cancel.
    def add(self):
        # Content is Add class that have 2 button
        content = Add(cancel=self.dismiss_popup, save=self.save)
        # Cancel button call dissmis_popup method,save button call save method
        # Set title name to 'Add Note' and make popup closed manually
        # Popup size is 500, 500
        self._popup = Popup(title='Add Note', title_font='Waree',
                            content=content, auto_dismiss=False,
                            size_hint=(None, None), size=(500, 500))
        self._popup.open()  # Open popup after create finish.

    def edit(self, path, filename):
        try:
            if fnmatch.fnmatch(filename[0],'*.txt'):
                textfile = open(os.path.join(path, filename[0]),
                                encoding=('utf-8'))
                content = Add(cancel=self.dismiss_popup, save=self.save)
                content.text_name.text = os.path.basename(filename[0])
                content.text_content.text = textfile.read()
                self._popup = Popup(title='Edit Note', title_font='Waree',
                                    content=content, auto_dismiss=False,
                                    size_hint=(None, None), size=(500, 500))
                self._popup.open()
            else:
                pass
        except IndexError:
            self.error_popup('Please Select File!!')

    def import_picture(self):
        content = ImportPicture(import_file=self.import_file,
                                source=str(ImportPicture.source),
                                cancel=self.dismiss_popup)
        self._popup = Popup(title='Import Picture', title_font='Waree',
                            auto_dismiss=False, content=content,
                            size_hint=(None, None), size=(600, 600))
        self._popup.open()

    def import_file(self, path):
        name = os.path.basename(path)
        shutil.copyfile(path, './picture/' + name)
        self.dismiss_popup()

    def rename_popup(self, path, filename):
        try:
            content = Rename(dismiss_popup=self.dismiss_popup)
            content.filename.text = os.path.basename(filename[0])
            content.path = path
            content.oldname = filename[0]
            self._popup = Popup(title='Rename', title_font='Waree',
                                content=content, auto_dismiss=False,
                                size_hint=(None, None),size=(400, 150))
            self._popup.open()
        except IndexError:
            self.error_popup('Please Select File!!')

    def show_delete(self):
        sel = self.desk.filechooser.selection
        if(sel == []):
            self.error_popup('Please Select File!!')
        else:
            content = DeleteFile(delete=self.delete, no=self.dismiss_popup)
            self._popup = Popup(title="Delete file", content=content,
                                auto_dismiss=False, size_hint=(0.5, 0.2))
            self._popup.open()

    def delete(self):
        path = self.desk.get_path()
        os.remove(path)
        self.desk.filechooser.selection = []
        self.dismiss_popup()

    def save(self, filename, content):
        if(len(filename) == 0):
            self.error_popup('Enter Filename!!')
        else:
            if(filename.endswith('.txt')):
                textfile = open(os.path.join('note/', filename), 'w',
                                encoding=('utf-8'))
            else:
                textfile = open(os.path.join('note/', filename+'.txt'), 'w',
                                encoding=('utf-8'))
            textfile.write(content)
            self.desk.filechooser.selection = []
            self.dismiss_popup()

    def error_popup(self, error_text):
        content = ShowError()
        content.text_error.text = error_text
        self.popup_error = Popup(
            title='Error!', content=content, auto_dismiss=False, size_hint=(
                None, None), size=(
                200, 200))
        content.cancel.bind(on_press=self.popup_error.dismiss)

        self.popup_error.open()


class DeleteButton():
    pass


class DeleteFile(RelativeLayout):
    delete = ObjectProperty(None)
    no = ObjectProperty(None)


class ShowPicture(RelativeLayout):
    source = StringProperty(None)
    cancel = ObjectProperty(None)


class ImportPicture(RelativeLayout):
    import_file = ObjectProperty(None)
    source = StringProperty()
    cancel = ObjectProperty(None)

    def show_picture(self, path):
        try:
            self.source = str(path[0])
        except:
            self.source = ''


class ShowText(RelativeLayout):
    text = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Add(RelativeLayout):
    cancel = ObjectProperty(None)
    save = ObjectProperty(None)

class Rename(RelativeLayout):
    dismiss_popup = ObjectProperty(None)
    cancel = dismiss_popup
    path = ObjectProperty(None)
    oldname = ObjectProperty(None)
    def rename(self):
        os.rename(self.oldname, (self.path+'/'+self.filename.text))
        self.dismiss_popup()


class ShowError(RelativeLayout):
    pass
