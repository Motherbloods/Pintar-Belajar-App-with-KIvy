from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.core.audio import SoundLoader
from sound_manager import SoundManager


class MainApp(App):
    def build(self):
        SoundManager.initialize_bgm()

        # Load sound effects
        self.arrow_sound = SoundLoader.load("./assets/arrow_music.mp3")

        # Set ukuran window (sesuaikan jika diperlukan)
        base_width = 450
        window_height = int(base_width * (16 / 9))
        Window.size = (base_width, window_height)
        self.root = RelativeLayout()

        with self.root.canvas.before:
            self.background = Rectangle(
                source="./assets/bg.png", pos=self.root.pos, size=Window.size
            )

        self.root.bind(size=self.update_background, pos=self.update_background)

        music_icon = Image(
            source="./assets/th.jpeg",
            size_hint=(None, None),
            size=(50, 50),
            pos=(10, Window.height + 100),
        )
        self.root.add_widget(music_icon)

        title_image = Image(
            source="./assets/Play.png",
            size_hint=(None, None),
            size=(720, 1280),  # Sesuaikan dengan ukuran gambar
            pos_hint={"center_x": 0.5, "center_y": 0.75},
        )
        self.root.add_widget(title_image)

        btn_layout = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(400, 200),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            spacing=20,
        )

        self.pilih_mode_btn = Button(
            text="PILIH MODE",
            font_size=24,
            size_hint=(1, None),
            height=50,
            background_normal="",
            background_color=(0.8, 0.8, 0.8, 1),
            color=(0, 0, 0, 1),
            on_press=self.play_sound_and_go_to_mode,
        )
        self.keluar_game_btn = Button(
            text="KELUAR GAME",
            font_size=24,
            size_hint=(1, None),
            height=50,
            background_normal="",
            background_color=(0.8, 0.8, 0.8, 1),
            color=(0, 0, 0, 1),
            on_press=self.play_sound_and_exit,
        )

        btn_layout.add_widget(self.pilih_mode_btn)
        btn_layout.add_widget(self.keluar_game_btn)
        self.root.add_widget(btn_layout)

        return self.root

    def play_sound_and_go_to_mode(self, instance):
        if self.arrow_sound:
            self.arrow_sound.play()
        self.go_to_mode(instance)

    def play_sound_and_exit(self, instance):
        if self.arrow_sound:
            self.arrow_sound.play()
        self.exit_game(instance)

    def go_to_mode(self, instance):
        App.get_running_app().stop()
        from mode import ModeApp

        ModeApp().run()

    def exit_game(self, instance):
        App.get_running_app().stop()

    def update_background(self, *args):
        self.background.size = Window.size
        self.background.pos = (0, 0)

    def on_stop(self):
        pass


if __name__ == "__main__":
    MainApp().run()
