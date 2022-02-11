from seqcreator.animation.animation import Animation
from seqcreator.users.sapir.songs.deprecated import under2
from overrides import overrides
from seqcreator.infra import timing
from seqcreator.rendering.function import functions_store
from seqcreator.users.song import Song


class Warm(Animation):
    def __init__(self, element_provider):
        super().__init__("warm", 100, 0, element_provider)

    def render_effects(self):
        # TODO sapir this should not be here, fix time factory issues
        timing.song_settings(bpm=128, beats_per_episode=32, start_offset=0)
        timing.beats(0, 100)
        # Add colors
        self.coloring_effect.uniform([0.6, 0.5, 0.3], self.element_provider.all_segments())
        self.coloring_effect.rainbow(0.3, 0.8, self.element_provider.all_segments())

