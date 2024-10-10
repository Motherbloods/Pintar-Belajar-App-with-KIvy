from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.core.audio import SoundLoader


class MainApp(App):
    def build(self):
        # Load sound effects
        self.arrow_sound = SoundLoader.load(
            "arrow_music.mp3"
        )  # Pastikan file suara tersedia
        self.bgm_sound = SoundLoader.load("bgm.mp3")

        # Set ukuran window (sesuaikan jika diperlukan)
        Window.size = (800, 600)

        # Gunakan RelativeLayout agar kita bisa bebas mengatur posisi elemen
        self.root = RelativeLayout()

        with self.root.canvas.before:
            self.background = Rectangle(
                source="board.png", pos=self.root.pos, size=Window.size
            )

        # Update ukuran background jika ukuran window berubah
        self.root.bind(size=self.update_background, pos=self.update_background)

        # Tambahkan icon musik di pojok kiri atas
        music_icon = Image(
            source="th.jpeg",
            size_hint=(None, None),
            size=(50, 50),
            pos=(10, Window.height - 60),
        )
        self.root.add_widget(music_icon)

        # Tambahkan label untuk judul di tengah
        title = Label(
            text="PINTAR BERHITUNG",
            font_size=36,
            pos_hint={"center_x": 0.5, "center_y": 0.75},
            color=(0, 0, 0, 1),
        )
        self.root.add_widget(title)

        # Tambahkan tombol untuk "PILIH MODE" dan "KELUAR GAME"
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
        )
        self.keluar_game_btn = Button(
            text="KELUAR GAME",
            font_size=24,
            size_hint=(1, None),
            height=50,
            background_normal="",
            background_color=(0.8, 0.8, 0.8, 1),
            color=(0, 0, 0, 1),
        )

        self.profile_icon = Image(
            source="th.jpeg",
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={"center_x": 0.7, "center_y": 0.495},
        )
        self.root.add_widget(self.profile_icon)

        btn_layout.add_widget(self.pilih_mode_btn)
        btn_layout.add_widget(self.keluar_game_btn)
        self.root.add_widget(btn_layout)

        # Buat layout vertikal untuk panah atas, tombol enter, dan panah bawah
        arrow_layout = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(80, 200),
            pos_hint={"right": 0.98, "center_y": 0.2},
            spacing=10,
        )

        # Tambahkan panah atas sebagai gambar dengan fungsi on_press
        self.arrow_up = Button(
            background_normal="arrow_up.png",
            background_down="arrow_up.png",
            border=(0, 0, 0, 0),
            size_hint=(None, None),
            size=(60, 60),
        )
        self.arrow_up.bind(on_press=self.on_arrow_up)

        # Tambahkan label enter
        self.enter_button = Button(
            text="enter",
            font_size=20,
            size_hint=(None, None),
            size=(60, 40),
            color=(0, 0, 0, 1),
            background_color=(0.8, 0.8, 0.8, 1),
        )
        self.enter_button.bind(on_press=self.on_enter)

        # Tambahkan panah bawah sebagai gambar dengan fungsi on_press
        self.arrow_down = Button(
            background_normal="arrow_down.png",
            background_down="arrow_down.png",
            border=(0, 0, 0, 0),
            size_hint=(None, None),
            size=(60, 60),
        )
        self.arrow_down.bind(on_press=self.on_arrow_down)

        arrow_layout.add_widget(self.arrow_up)
        arrow_layout.add_widget(self.enter_button)
        arrow_layout.add_widget(self.arrow_down)

        self.root.add_widget(arrow_layout)

        # Bind keyboard events
        Window.bind(on_key_down=self._on_keyboard_down)

        if self.bgm_sound:
            self.bgm_sound.loop = True  # Set loop
            self.bgm_sound.play()

        return self.root

    def play_arrow_sound(self):
        if self.arrow_sound:
            self.arrow_sound.play()

    def on_arrow_up(self, instance):
        self.play_arrow_sound()
        self.move_selection_up()

    def on_arrow_down(self, instance):
        self.play_arrow_sound()
        self.move_selection_down()

    def on_enter(self, instance):
        self.handle_selection()

    def move_selection_up(self):
        self.profile_icon.pos_hint = {"center_x": 0.7, "center_y": 0.495}
        self.pilih_mode_btn.background_color = (0.7, 0.7, 0.7, 1)
        self.keluar_game_btn.background_color = (0.8, 0.8, 0.8, 1)

    def move_selection_down(self):
        self.profile_icon.pos_hint = {"center_x": 0.7, "center_y": 0.415}
        self.pilih_mode_btn.background_color = (0.8, 0.8, 0.8, 1)
        self.keluar_game_btn.background_color = (0.7, 0.7, 0.7, 1)

    def handle_selection(self):
        if self.profile_icon.pos_hint["center_y"] == 0.55:
            print("PILIH MODE selected")
            # Add your logic for PILIH MODE here
        else:
            print("KELUAR GAME selected")
            App.get_running_app().stop()

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 82:  # Up arrow
            self.play_arrow_sound()
            self.move_selection_up()
        elif keycode == 81:  # Down arrow
            self.play_arrow_sound()
            self.move_selection_down()
        elif keycode == 40:  # Enter key
            self.handle_selection()

    def update_background(self, *args):
        self.background.size = Window.size
        self.background.pos = (0, 0)


if __name__ == "__main__":
    MainApp().run()
