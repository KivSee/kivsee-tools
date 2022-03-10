import config
from seqcreator.animations.soundless_animation import SoundlessAnimation
from seqcreator.api import timing, coloring, masking, element_provider, color
from seqcreator.rendering.functions.functions_store import const_function


class Even(SoundlessAnimation):
    def __init__(self):
        super().__init__("even", 1000 * 60, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        timing.song_settings(bpm=60, beats_per_episode=32, start_offset=0)

        self.elements.set(self.elements.all_even())
        timing.beats(0, 60)
        coloring.uniform(color.LIGHT_PURPLE)
        self.elements.set(self.elements.all_odd())
        coloring.uniform(color.LIGHT_TURQUOISE)
        masking.Brightness(const_function(config.brightness_level))
        