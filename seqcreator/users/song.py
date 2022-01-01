from abc import abstractmethod

from seqcreator.animation.animation import Animation
from seqcreator.infra.animations_factory import ColoringEffectFactory, MaskingEffectFactory
from seqcreator.network import manager
from seqcreator.users.effects_list_holder import EffectsListHolder
from seqcreator.logging.logger import kivsee_logger as logger


class Song(Animation):

    def __init__(self, trigger, duration, repeats, element_provider):
        super(Song, self).__init__(trigger, duration, repeats, element_provider)

    def render_effects(self):
        # stub, overing in child impl
        pass

    def play(self):
        logger.info(f"Song: load {self.trigger_name}")
        self.store_sequence()
        logger.info(f"Song: playing {self.trigger_name}")
        manager.play_song(self.trigger_name)
