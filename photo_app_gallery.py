import os

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen


class SquareImage(Image):
    pass


class MyNewGallery(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.add_images_to_gallery()


    def add_images_to_gallery(self, *args):
        compteur_photo = 0
        path = "/home/petchorine/Desktop/monPyhon/mes_projets_python/Double_view/Images"
        for filename in os.listdir(path):
            if os.path.isfile(os.path.join(path, filename)):
                img = SquareImage(source=f"/home/petchorine/Desktop/monPyhon/mes_projets_python/Double_view/Images/{filename}")                
                self.ids.scroll.add_widget(img)
                compteur_photo += 1
                

    def refresh_gallery(self, *args):
        self.ids.scroll.clear_widgets()
        self.add_images_to_gallery()


class MyCamera(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.camera = Camera(play=True)
        self.add_widget(self.camera)


    def take_picture(self, *args):
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