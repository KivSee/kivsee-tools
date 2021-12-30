from users.song import Song
from users.sapir.me import Sapir

class Under(Song):
    def __init__(self):
        super().__init__(Sapir(), "under", 147000)

    def render_effects(self):
        # stub, overing in child impl
        pass
