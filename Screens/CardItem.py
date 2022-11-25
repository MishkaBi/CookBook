from kivy.uix.screenmanager import Screen


class CardItem(Screen):

    def __init__(self, **kw):
        super(CardItem, self).__init__(**kw)
        self.name = 'dish'