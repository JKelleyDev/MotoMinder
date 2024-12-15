import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.app import App

kivy.require('2.0.0')

# Load the .kv files using Builder

Builder.load_file("LoginScreen.kv")
Builder.load_file("MainScreen.kv")

class LoginScreen(Screen):
    pass
class MainScreen(Screen):
    pass


class MotoMinder(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(LoginScreen(name='login'))
        sm.current = 'main'
        return sm


if __name__ == "__main__":
    MotoMinder = MotoMinder()
    MotoMinder.run()
