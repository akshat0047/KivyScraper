import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
# kivy.require('1.11.1')  # replace with your current kivy version !

Builder.load_file('scrape.kv')


class ScrapyScreen(Screen):

    def scrape(self):
        link = self.ids.surl.text
        depth = self.ids.sdepth.text
        option = self.ids.btn.text

        print(link)
        print(depth)
        print(option)

class SeleniumScreen(Screen):

    def scrape(self):
        link = self.ids.ssurl.text
        depth = self.ids.ssdepth.text
        option = self.ids.ssdropdown

        print(link)
        print(depth)
        print(option)

class CustomDropDown(DropDown):
    pass

sm = ScreenManager()
sm.add_widget(ScrapyScreen(name='scrapy'))
sm.add_widget(SeleniumScreen(name='selenium'))
sm.current = 'scrapy'


class TurboScraperApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TurboScraperApp().run()
