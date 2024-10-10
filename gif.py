from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout


class AnimatedImage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Daftar gambar yang akan digunakan dalam animasi
        self.images = [
            "./assets/avatar/gif/ninja/ninja-0.png",
            "./assets/avatar/gif/ninja/ninja-1.png",
            "./assets/avatar/gif/ninja/ninja-2.png",
            "./assets/avatar/gif/ninja/ninja-3.png",
            "./assets/avatar/gif/ninja/ninja-4.png",
            "./assets/avatar/gif/ninja/ninja-5.png",
        ]

        # Indeks gambar saat ini
        self.current_image = 0

        # Buat widget Image dan tambahkan ke layout
        self.img = Image(source=self.images[self.current_image])
        self.add_widget(self.img)

        # Set timer untuk mengganti gambar setiap 0.5 detik
        Clock.schedule_interval(self.update_image, 0.1)

    def update_image(self, dt):
        # Ganti ke gambar berikutnya
        self.current_image = (self.current_image + 1) % len(self.images)
        self.img.source = self.images[self.current_image]
        self.img.reload()  # Perbarui gambar


class AnimationApp(App):
    def build(self):
        return AnimatedImage()


if __name__ == "__main__":
    AnimationApp().run()
