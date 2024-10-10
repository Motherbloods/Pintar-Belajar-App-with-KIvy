from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader


class ModeApp(App):
    def build(self):
        # Load sound effect
        self.arrow_sound = SoundLoader.load("arrow_music.mp3")

        base_width = 450
        window_height = int(base_width * (16 / 9))
        Window.size = (base_width, window_height)

        self.root = RelativeLayout()

        with self.root.canvas.before:
            self.background = Rectangle(
                source="board.png",
                pos=self.root.pos,
                size=Window.size,
            )

        back_layout = RelativeLayout(
            size_hint=(None, None), size=(Window.width, 50), pos_hint={"top": 0.95}
        )

        back_btn = Button(
            background_normal="arrow.png",
            size_hint=(None, None),
            size=(40, 40),
            pos_hint={"x": 0.05, "center_y": 0.5},
            on_press=self.play_sound_and_go_back,
        )

        mode_label = Label(
            text="PILIH MODE",
            font_size=28,
            pos_hint={"center_x": 0.55, "center_y": 0.5},
            color=(0.4, 0.2, 1, 1),
        )

        back_layout.add_widget(back_btn)
        back_layout.add_widget(mode_label)
        self.root.add_widget(back_layout)

        zones = ["ZONA ARITMATIKA", "ZONA BANGUN DATAR", "ZONA PECAHAN"]

        for i, zone in enumerate(zones):
            btn = Button(
                text=zone,
                size_hint=(0.8, 0.12),
                pos_hint={"center_x": 0.5, "center_y": 0.65 - (i * 0.15)},
                background_normal="",
                background_color=(0.4, 0.2, 1, 0.8),
                color=(1, 1, 1, 1),
                font_size=24,
            )
            btn.bind(on_press=lambda x, z=zone: self.play_sound_and_select_zone(z))
            self.root.add_widget(btn)

        return self.root

    def play_sound_and_go_back(self, instance):
        if self.arrow_sound:
            self.arrow_sound.play()
        self.go_back(instance)

    def play_sound_and_select_zone(self, zone):
        if self.arrow_sound:
            self.arrow_sound.play()
        self.on_zone_select(zone)

    def go_back(self, instance):
        App.get_running_app().stop()
        from main3 import MainApp

        MainApp().run()

    def on_zone_select(self, zone):
        print(f"Selected zone: {zone}")

    def on_size(self, *args):
        self.background.size = Window.size

    def on_stop(self):
        pass


if __name__ == "__main__":
    ModeApp().run()
