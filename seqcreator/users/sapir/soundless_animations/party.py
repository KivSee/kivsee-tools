
from seqcreator.animations.soundless_animation import SoundlessAnimation
from seqcreator.api import timing
from seqcreator.api.color import Color
from seqcreator.api import coloring, masking
from seqcreator.api import element_provider
from seqcreator.rendering.functions.functions_store import const_function


class Party(SoundlessAnimation):
    def __init__(self):
        super().__init__("party", 1000 * 40, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        timing.song_settings(bpm=128, beats_per_episode=32, start_offset=0)

        # print(self.elements.living_room())
        self.elements.set([("whisper", "1"), ("whisper", "3")])
        timing.beats(0, 32)
        coloring.rainbow(speed=6)
        masking.Brightness(const_function(0.8))

        
