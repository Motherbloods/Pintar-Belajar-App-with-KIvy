from kivy.core.audio import SoundLoader


class SoundManager:
    bgm_instance = None

    @classmethod
    def initialize_bgm(cls):
        if cls.bgm_instance is None:
            cls.bgm_instance = SoundLoader.load("./assets/bgm.mp3")
            if cls.bgm_instance:
                cls.bgm_instance.loop = True
                cls.bgm_instance.play()

    @classmethod
    def stop_bgm(cls):
        if cls.bgm_instance:
            cls.bgm_instance.stop()
            cls.bgm_instance = None
