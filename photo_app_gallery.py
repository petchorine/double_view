import os

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.camera import Camera
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView


class SquareImage(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.allow_stretch = True
        self.keep_ratio = False
        self.size_hint_y = None
        self.height = dp(self.width)

class MyNewGallery(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        my_scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.my_gallery_grid = GridLayout(cols=3, spacing=dp(5), padding=dp(5),
                                          size_hint=(1, None), height=1000)
        self.add_images_to_gallery()
        my_scroll.add_widget(self.my_gallery_grid)

        self.add_widget(my_scroll)


    def add_images_to_gallery(self, *args):
        path = "/home/petchorine/Desktop/monPyhon/mes_projets_python/Double_view/Images"
        for filename in os.listdir(path):
            if os.path.isfile(os.path.join(path, filename)):
                img = SquareImage(source=f"/home/petchorine/Desktop/monPyhon/mes_projets_python/Double_view/Images/{filename}")
                self.my_gallery_grid.add_widget(img)

    def refresh_gallery(self, *args):
        self.my_gallery_grid.clear_widgets()
        self.add_images_to_gallery()

class MyCamera(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.camera = Camera(resolution=(350, 700), play=True)
        self.add_widget(self.camera)

        button = Button(text="Prendre une photo", size_hint=(1, 0.1))
        button.bind(on_press=self.on_button_press)
        self.add_widget(button)

    def on_button_press(self, instance):
        path = "/home/petchorine/Desktop/monPyhon/mes_projets_python/Double_view/Images"
        # compte le nbre de fichier dans les dossier destination des photos
        # permet de renommer chaque photo prise avec un nbr en plus
        num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        self.camera.export_to_png(f"/home/petchorine/Desktop/monPyhon/mes_projets_python/Double_view/Images/image{num_files + 1}.png")

class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.screen1 = MyNewGallery(name="screen1")
        screen2 = MyCamera(name="screen2")

        btn_to_screen2 = Button(text="to screen 2",
                                size_hint = (None, None),
                                size = (100,100),
                                pos_hint = {"right": 1})
        btn_to_screen2.bind(on_press=self.to_camera)
        self.screen1.add_widget(btn_to_screen2)

        btn_to_gallery = Button(text="to gallery",
                                size_hint=(None, None),
                                size=(100, 100),
                                pos_hint={"top": 1, "left": 1})
        btn_to_gallery.bind(on_press=self.to_gallery)
        screen2.add_widget(btn_to_gallery)

        self.add_widget(self.screen1)
        self.add_widget(screen2)

    def to_camera(self, *args):
        self.transition.direction = "left"
        self.current = "screen2"

    def to_gallery(self, *args):
        self.transition.direction = "right"
        self.current = "screen1"

        self.screen1.refresh_gallery()


class RefreshGalleryApp(App):
    def build(self):
        Window.size = (350,700)
        return MyScreenManager()

RefreshGalleryApp().run()