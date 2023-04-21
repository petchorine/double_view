from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class MyCam(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.camera = Camera(resolution=(350, 700), play=True)
        self.add_widget(self.camera)

        button = Button(text="Prendre une photo", size_hint=(1, 0.1))
        button.bind(on_press=self.on_button_press)
        self.add_widget(button)

    def on_button_press(self, instance):
        print("clic")
        self.camera.export_to_png("/home/petchorine/Desktop/monPyhon/mes_projets_python/Double_view/Images/image.png")


class CameraApp(App):

    def build(self):
        Window.size = (350, 700)
        return MyCam()


if __name__ == '__main__':
    CameraApp().run()