
from asyncio.log import logger
import config
from seqcreator.animations.soundless_animation import SoundlessAnimation
from seqcreator.api import timing
from seqcreator.api import color
from seqcreator.api import coloring, masking
from seqcreator.api import element_provider
from seqcreator.infra.logger import kivsee_logger as logger
from seqcreator.rendering.functions.functions_store import linear_function

class Romantic(SoundlessAnimation):
    def __init__(self):
        super().__init__("romantic", 1000 * 30, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        timing.song_settings(bpm=32, beats_per_episode=32, start_offset=0)

        self.elements.set_all()
        timing.beats(0, 64)
        coloring.rainbow_static(0.7, 1.0)
        # coloring.rainbow(0.7, 1.0)
        logger.info(f"Adjusting brightness level to {config.brightness_level}")
        timing.cycle(4)
        masking.brightness_sin(0.3, 0.6, 1)
        # masking.brightness(config.brightness_level)
        
        
