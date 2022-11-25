from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.size = (360, 540)

from Screens import Menu, DishesList, CardItem, DishScreen


class CookBook(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_file('app_interface.kv')
        return screen


CookBook().run()