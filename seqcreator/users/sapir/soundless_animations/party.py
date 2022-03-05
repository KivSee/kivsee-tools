
from seqcreator.animations.soundless_animation import SoundlessAnimation
from seqcreator.api import timing
from seqcreator.api.color import Color
from seqcreator.api import coloring
from seqcreator.api import element_provider


class Party(SoundlessAnimation):
    def __init__(self):
        super().__init__("party", 1000 * 40, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        timing.song_settings(bpm=128, beats_per_episode=32, start_offset=0)

        self.elements.set_all()
        timing.beats(0, 32)
        coloring.rainbow(speed=4)

        
