from seqcreator.animations.soundless_animation import SoundlessAnimation
from seqcreator.users.sapir.songs.deprecated import under2
from seqcreator.infra import timing
from seqcreator.rendering.function import functions_store
from seqcreator.animations.song import Song


class Warm(SoundlessAnimation):
    def __init__(self, element_provider):
        super().__init__("warm", 100, 0, element_provider)

    def render_effects(self):
        # TODO(sapir): this should not be here, fix time factory issues
        timing.song_settings(bpm=128, beats_per_episode=32, start_offset=0)
        timing.beats(0, 100)
        # Add colors
        self.coloring_effect.uniform([0.6, 0.5, 0.3], self.elements.all_segments())
        self.coloring_effect.rainbow(0.3, 0.8, self.elements.all_segments())

