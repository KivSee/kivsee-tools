
from seqcreator.animations.soundless_animation import SoundlessAnimation
from seqcreator.api import timing
from seqcreator.api.color import Color
from seqcreator.api import coloring


class Warm(SoundlessAnimation):
    def __init__(self):
        super().__init__("warm", 1000 * 30, 0)

    def render_effects(self):
        timing.song_settings(bpm=128, beats_per_episode=32, start_offset=0)

        timing.beats(0, 5)
        coloring.uniform(Color(0.25, 1.0, 0.5))

        timing.beats(5, 10)
        coloring.uniform(Color(0.8, 1.0, 0.5))

        timing.beats(10, 15)
        coloring.uniform(Color(0.0, 0.6, 0.5))

        timing.beats(15, 20)
        coloring.uniform(Color(0.6, 1.0, 0.5))
