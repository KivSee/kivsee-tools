from seqcreator.infra.animations_factory import ColoringEffectFactory, MaskingEffectFactory
from seqcreator.network import manager
from seqcreator.users.effects_list_holder import EffectsListHolder
from seqcreator.logging.logger import kivsee_logger as logger


class Animation(object):

    def __init__(self, trigger, duration, repeats, elements_provider):
        self.trigger_name = trigger
        self.duration = duration
        self.holder = EffectsListHolder()
        self.repeats = repeats
        self.element_provider = elements_provider
        self.coloring_effect = ColoringEffectFactory(self.element_provider.all_segments(), self.holder)
        self.masking_effect = MaskingEffectFactory(self.element_provider.all_segments(), self.holder)

    def render_effects(self):
        # stub, overing in child impl
        pass

    def render(self):
        self.render_effects()
        return {
            "effects": self.holder.effects_list,
            "duration_ms": self.duration,
            "num_repeats": self.repeats
        }

    def store_sequence(self):
        logger.info(f"storing {self.trigger_name} sequence")
        seq = self.render()
        manager.store_sequence_all(self.trigger_name, seq, self.element_provider.all_things())


    def play(self):
        logger.info(f"Song: load {self.trigger_name}")
        self.store_sequence()
        logger.info(f"Song: playing {self.trigger_name}")
        manager.play_song(self.trigger_name)