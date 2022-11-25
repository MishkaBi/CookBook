from kivy.uix.screenmanager import Screen


class MenuScreen(Screen):

    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        self.name = 'menu'
        self.button1_name = 'Страви'
        self.button2_name = 'Вихід'