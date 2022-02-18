from seqcreator.animations.soundless_animation import SoundlessAnimation
from seqcreator.infra.color import Color
from seqcreator.rendering.effects import coloring
from seqcreator.users.sapir.songs.deprecated import under2
from seqcreator.infra import timing
from seqcreator.rendering.function import functions_store
from seqcreator.animations.song import Song


class Warm(SoundlessAnimation):
    def __init__(self):
        super().__init__("warm", 1000 * 30, 0)

    def render_effects(self):
        # TODO(sapir): this should not be here, fix time factory issues
        timing.song_settings(bpm=128, beats_per_episode=32, start_offset=0)

        timing.beats(0, 5)
        coloring.uniform(Color(0.25, 1.0, 0.5))

        timing.beats(5, 10)
        coloring.uniform(Color(0.8, 1.0, 0.5))

        timing.beats(10, 15)
        coloring.uniform(Color(0.0, 0.6, 0.5))

        timing.beats(15, 20)
        coloring.uniform(Color(0.6, 1.0, 0.5))
