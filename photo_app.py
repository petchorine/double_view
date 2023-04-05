from kivy.app import App
from kivy.uix.camera import Camera
from kivy.core.window import Window

class CameraApp(App):

    def build(self):
        self.camera = Camera(resolution=(640, 480), play=True)
        Window.bind(on_keyboard=self.on_key_press)
        return self.camera

    def on_key_press(self, instance, key, *args):
        if key == ord('p'):
            self.camera.export_to_png("image.png")

if __name__ == '__main__':
    CameraApp().run()
