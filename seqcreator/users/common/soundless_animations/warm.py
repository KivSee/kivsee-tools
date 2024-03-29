
from asyncio.log import logger
import config
from seqcreator.animations.soundless_animation import SoundlessAnimation
from seqcreator.api import timing
from seqcreator.api.color import Color
from seqcreator.api import coloring, masking
from seqcreator.api import element_provider
from seqcreator.infra.logger import kivsee_logger as logger
from seqcreator.rendering.functions.functions_store import linear_function

class Warm(SoundlessAnimation):
    def __init__(self):
        super().__init__("warm", 1000 * 30, 0)
        self.elements = element_provider.get_element_provider()

    def render_effects(self):
        timing.song_settings(bpm=128, beats_per_episode=32, start_offset=0)

        self.elements.set(self.elements.all())
        timing.beats(0, 64)
        coloring.hue_range(0.035, 0.035, 1)
        logger.info(f"Adjusting brightness level to {config.brightness_level}")
        masking.brightness(config.brightness_level)
        
        
