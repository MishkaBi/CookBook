from kivy.uix.screenmanager import Screen


class Dish(Screen):

    def __init__(self, **kw):
        super(Dish, self).__init__(**kw)
        self.name = 'dish'
