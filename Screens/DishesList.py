from kivy.uix.screenmanager import Screen


class DishesListScreen(Screen):

    def __init__(self, **kw):
        super(DishesListScreen, self).__init__(**kw)
        self.name = 'dishes_list'

