#     ChiTrain
#     Copyright (C) 2018 Dorian Turba
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from kivy import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class Category(BoxLayout):
    Builder.load_file('kv_files/CollectionCard.kv')
    name: StringProperty
    description: StringProperty

    def __init__(self, name: str = 'Name', description: str= 'desc', **kwargs):
        super().__init__(**kwargs)
        self.name = StringProperty(name)
        self.description = StringProperty(description)


class MainWindow(BoxLayout):
    Builder.load_file('kv_files/MainWindow.kv')
    category = ObjectProperty(None)


class MeteorApp(App):
    def build(self):
        window = MainWindow()
        return window


if __name__ == '__main__':
    Config.set('graphics', 'resizable', False)
    Config.set('graphics', 'height', 50 * 16)
    Config.set('graphics', 'width', 50 * 10)
    MeteorApp().run()

# def main_2() -> None:
#     my_list = ["This", "is", 4, 13327]
#     with open('binary.dat', 'wb') \
#             as my_file:
#         # Open the file C:\\binary.dat for writing. The letter r before the
#         # filename string is used to prevent backslash escaping.
#         pickle.dump(my_list, my_file)
#         my_file.close()
#     with open('binary.dat', 'rb') \
#             as my_file:
#         loaded_list = pickle.load(my_file)
#         my_file.close()
#     print(loaded_list)
#     return None
