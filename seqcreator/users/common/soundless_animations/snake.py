import config
from seqcreator.animations.soundless_animation import SoundlessAnimation
from seqcreator.api import timing, coloring, masking, element_provider, color
from seqcreator.rendering.functions.functions_store import const_function


class Snake(SoundlessAnimation):
    def __init__(self):
        super().__init__("snake", 1000 * 9, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        timing.song_settings(bpm=60, beats_per_episode=32, start_offset=0)

        
        # self.elements.set([("snake_test", "all")])
        self.elements.set(self.elements.get_all_segments())
        timing.beats(0, 3)
        coloring.rainbow_static(0.74, 0.84)
        masking.snake()
        masking.brightness(config.brightness_level)

        self.elements.set(self.elements.get_all_segments())
        timing.beats(3, 6)
        coloring.rainbow_static(0.0, 0.16)
        masking.snake_backward()
        masking.brightness(config.brightness_level)

        self.elements.set(self.elements.get_all_segments())
        timing.beats(6, 9)
        coloring.rainbow_static(0.32, 0.5)
        masking.snake_bidrectional()
        masking.brightness(config.brightness_level)

        # timing.beats(3, 6)
        # coloring.uniform(color.LIGHT_PURPLE)
        # masking.snake_bidrectional()
        # masking.brightness(config.brightness_level)
        

        # self.elements.set(self.elements.all_even())
        # coloring.uniform(color.LIGHT_TURQUOISE)
        # masking.snake()

        # self.elements.set(self.elements.all_odd())
        # coloring.uniform(color.LIGHT_TURQUOISE)
        # masking.snake()
