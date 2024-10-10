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
from kivy.clock import Clock


class ClickableImage(ButtonBehavior, Image):
    pass


class Divider(Widget):
    def __init__(self, **kwargs):
        super(Divider, self).__init__(**kwargs)
        with self.canvas:
            Color(0.7, 0.7, 0.7, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


class AnimatedImage(BoxLayout):
    def __init__(self, base_path="./assets/avatar/gif/ninja/ninja", **kwargs):
        super().__init__(**kwargs)
        self.base_path = base_path
        self.images = [f"{self.base_path}-{i}.png" for i in range(6)]
        self.current_image = 0
        self.img = Image(source=self.images[self.current_image])
        self.add_widget(self.img)
        Clock.schedule_interval(self.update_image, 0.1)

    def update_image(self, dt):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.img.source = self.images[self.current_image]
        self.img.reload()

    def update_animation(self, new_base_path):
        self.base_path = new_base_path
        self.images = [f"{self.base_path}-{i}.png" for i in range(6)]
        self.current_image = 0
        self.img.source = self.images[self.current_image]


class AvatarGifApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation="horizontal", padding=20, spacing=15)

        # Left side - Static Avatar
        left_layout = AnchorLayout(anchor_x="center", anchor_y="center")
        self.static_avatar = ClickableImage(
            source="./assets/avatar/png/ninja.png",
            size_hint=(None, None),
            size=(200, 200),
        )
        self.static_avatar.bind(on_press=self.show_avatar_options)
        left_layout.add_widget(self.static_avatar)

        # Right side - Animated Avatar
        right_layout = AnchorLayout(anchor_x="center", anchor_y="center")
        self.animated_avatar = AnimatedImage(size_hint=(None, None), size=(200, 200))
        right_layout.add_widget(self.animated_avatar)

        # Add both layouts to main layout
        main_layout.add_widget(left_layout)
        main_layout.add_widget(right_layout)

        return main_layout

    def show_avatar_options(self, instance):
        popup_layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        current_avatar_layout = BoxLayout(
            orientation="vertical", size_hint_y=None, height=200, spacing=10
        )
        current_avatar_layout.add_widget(
            Label(text="Avatar Saat Ini", size_hint_y=None, height=40, font_size=18)
        )
        current_avatar = Image(
            source=self.static_avatar.source, size_hint=(None, None), size=(150, 150)
        )
        current_avatar_layout.add_widget(current_avatar)

        popup_layout.add_widget(current_avatar_layout)
        popup_layout.add_widget(Divider(size_hint_y=None, height=2))

        popup_layout.add_widget(
            Label(text="Pilih Avatar Lain", size_hint_y=None, height=40, font_size=18)
        )

        avatar_grid = GridLayout(cols=3, spacing=10, size_hint_y=None, height=200)

        avatar_options = {
            "./assets/avatar/png/male.png": "./assets/avatar/gif/male/male",
            "./assets/avatar/png/female.png": "./assets/avatar/gif/female/female",
            "./assets/avatar/png/ninja.png": "./assets/avatar/gif/ninja/ninja",
        }

        for static_path, animated_base_path in avatar_options.items():
            avatar = ClickableImage(
                source=static_path,
                size_hint=(None, None),
                size=(100, 100),
            )
            avatar.bind(
                on_press=lambda instance, path=static_path, anim_path=animated_base_path: self.change_avatar(
                    instance, path, anim_path
                )
            )
            avatar_grid.add_widget(avatar)

        popup_layout.add_widget(avatar_grid)

        close_button = Button(
            text="Tutup",
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={"center_x": 0.5},
        )
        close_button.bind(on_press=self.close_popup)
        popup_layout.add_widget(close_button)

        self.popup = Popup(
            title="Pilih Avatar",
            content=popup_layout,
            size_hint=(None, None),
            size=(400, 600),
        )
        self.popup.open()

    def change_avatar(self, instance, static_path, animated_base_path):
        self.static_avatar.source = static_path
        self.animated_avatar.update_animation(animated_base_path)
        print(f"Avatar changed to: {static_path}")
        self.popup.dismiss()

    def close_popup(self, instance):
        self.popup.dismiss()


if __name__ == "__main__":
    AvatarGifApp().run()
