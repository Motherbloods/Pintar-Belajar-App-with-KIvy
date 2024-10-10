from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


# Custom widget: Avatar yang bisa diklik (menggunakan ButtonBehavior untuk Image)
class ClickableImage(ButtonBehavior, Image):
    pass


# Widget custom untuk garis pemisah
class Divider(Widget):
    def __init__(self, **kwargs):
        super(Divider, self).__init__(**kwargs)
        with self.canvas:
            Color(0.7, 0.7, 0.7, 1)  # Warna abu-abu
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


class AvatarApp(App):
    def build(self):
        # Layout utama
        self.main_layout = AnchorLayout(anchor_x="center", anchor_y="center")

        # Membuat avatar utama yang bisa diklik
        self.avatar = ClickableImage(
            source="./assets/avatar/png/ninja.png",
            size_hint=(None, None),
            size=(200, 200),
        )
        self.avatar.bind(on_press=self.show_avatar_options)  # Mengikat event klik

        self.main_layout.add_widget(self.avatar)
        return self.main_layout

    def show_avatar_options(self, instance):
        # Layout popup yang menampilkan avatar saat ini dan opsi lainnya
        popup_layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        # Layout untuk avatar saat ini dan label
        current_avatar_layout = BoxLayout(
            orientation="vertical", size_hint_y=None, height=200, spacing=10
        )
        current_avatar_layout.add_widget(
            Label(text="Avatar Saat Ini", size_hint_y=None, height=40, font_size=18)
        )
        current_avatar = Image(
            source=self.avatar.source, size_hint=(None, None), size=(150, 150)
        )
        current_avatar_layout.add_widget(current_avatar)

        popup_layout.add_widget(current_avatar_layout)

        # Divider/ganti Separator
        popup_layout.add_widget(Divider(size_hint_y=None, height=2))

        # Opsi avatar lain
        popup_layout.add_widget(
            Label(text="Pilih Avatar Lain", size_hint_y=None, height=40, font_size=18)
        )

        # Grid layout untuk menampilkan avatar lainnya secara rapi
        avatar_grid = GridLayout(cols=3, spacing=10, size_hint_y=None, height=200)

        # Tambahkan opsi avatar lain sebagai gambar yang bisa diklik
        other_avatar1 = ClickableImage(
            source="./assets/avatar/png/male.png",
            size_hint=(None, None),
            size=(100, 100),
        )
        other_avatar2 = ClickableImage(
            source="./assets/avatar/png/female.png",
            size_hint=(None, None),
            size=(100, 100),
        )
        other_avatar3 = ClickableImage(
            source="./assets/avatar/png/ninja.png",
            size_hint=(None, None),
            size=(100, 100),
        )

        # Bind klik untuk avatar lainnya
        other_avatar1.bind(on_press=self.change_avatar)
        other_avatar2.bind(on_press=self.change_avatar)
        other_avatar3.bind(on_press=self.change_avatar)

        # Tambahkan avatar lainnya ke grid layout
        avatar_grid.add_widget(other_avatar1)
        avatar_grid.add_widget(other_avatar2)
        avatar_grid.add_widget(other_avatar3)

        popup_layout.add_widget(avatar_grid)

        # Tambahkan tombol untuk menutup popup
        close_button = Button(
            text="Tutup",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"center_x": 0.5},
        )
        close_button.bind(on_press=self.close_popup)
        popup_layout.add_widget(close_button)

        # Membuat popup
        self.popup = Popup(
            title="Pilih Avatar",
            content=popup_layout,
            size_hint=(None, None),
            size=(400, 600),
        )
        self.popup.open()

    def change_avatar(self, instance):
        # Ganti avatar utama dengan avatar yang dipilih
        self.avatar.source = instance.source  # Memperbarui avatar utama
        print(f"Avatar changed to: {instance.source}")

        # Menutup popup setelah avatar dipilih
        self.popup.dismiss()

    def close_popup(self, instance):
        # Menutup popup secara manual
        self.popup.dismiss()


if __name__ == "__main__":
    AvatarApp().run()
