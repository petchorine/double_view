from datetime import datetime
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class Screen1(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        f = FloatLayout()

        maintenant = datetime.now() 
        heure_actuelle = maintenant.strftime("%H:%M:%S")
        
        l = Label(text=f"{heure_actuelle}", font_size="40sp")
        # b = Button(text="Refresh",
        #            size_hint=(None, None),size=(100,100),
        #             pos_hint={"left": 1})
        # b.bind(on_press=self.refresh_time)
        
        self.add_widget(l)
        # self.add_widget(b)
        
        self.time_label = l

    def refresh_time(self, *args):
        maintenant = datetime.now()
        heure_actuelle = maintenant.strftime("%H:%M:%S")
        self.time_label.text = heure_actuelle


class Screen2(Screen):
    pass


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        screen1 = Screen1(name="screen1")
        screen2 = Screen2(name="screen2")


        btn_to_b = Button(text="to b",
                    size_hint=(None, None),size=(100,100), 
                    pos_hint={"right": 1})
        btn_to_b.bind(on_press=self.go_to_b)
        screen1.add_widget(btn_to_b)

        btn_to_time = Button(text="to time")
        btn_to_time.bind(on_press=self.go_to_time)
        screen2.add_widget(btn_to_time)

        self.add_widget(screen1)
        self.add_widget(screen2)
      

    def go_to_b(self, instance):
        self.transition.direction = "left";
        self.current = "screen2"


    def go_to_time(self, instance):
        self.transition.direction = "right";
        screen1 = self.get_screen("screen1")  # get the Screen1 instance
        screen1.refresh_time()  # call the refresh_time method of Screen1
        self.current = "screen1"

class MyGalleryApp(App):
    def build(self):
        Window.size= (350,700)
        return MyScreenManager()

MyGalleryApp().run()