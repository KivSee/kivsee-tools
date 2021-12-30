from users.sapir.songs.deprecated import under2
from overrides import overrides
from infra import timing

from users.song import Song


class Under(Song):
    def __init__(self, thing_names):
        super().__init__("under", 147000, 0, thing_names)


    # @overrides(Song)
    def render_effects(self):
        timing.song_settings(bpm=128, beats_per_episode=32, start_offset=0)
        timing.beats(2, 20)
        self.coloring_effect.uniform([0.6, 0.4, 0.5])

