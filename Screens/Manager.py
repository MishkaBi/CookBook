from kivy.uix.screenmanager import ScreenManager
from Screens import Menu, DishesList
from Screens.DishesList import DishesListScreen
from Screens.DishScreen import Dish
from CardItem import CardItem


class Manager(ScreenManager):
    def __init__(self):
        super(Manager, self).__init__()

        # register all screens
        self.add_widget(Menu.MenuScreen(name='menu'))
        self.add_widget(DishesList.DishesListScreen(name='dishes_list'))
        self.add_widget(Dish(name='dish'))
        self.add_widget(CardItem(name='card_item'))

