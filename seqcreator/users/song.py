from abc import abstractmethod
from seqcreator.infra.animations_factory import ColoringEffectFactory, MaskingEffectFactory
from seqcreator.network import manager
from seqcreator.users.effects_list_holder import EffectsListHolder
from seqcreator.logging.kivsee_logger import kivseeLogger as logger

class Song(object):

    # TODO @abstractmethod
    def __init__(self, trigger, duration, repeats, thing_names):
        self.trigger_name = trigger
        self.duration = duration
        self.holder = EffectsListHolder()
        self.repeats = repeats
        self.thing_names = thing_names
        self.segments = ["spiral1", "spiral2", "spiral3", "subout1", "subout2", "subout3", "subout4", "subout5",
                         "subout6", "subout7", "subout8", "subout9", "subout10"]
        self.coloring_effect = ColoringEffectFactory(self.segments, self.holder)
        self.masking_effect = MaskingEffectFactory(self.segments, self.holder)

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
        logger.info(f"storing for each element in {self.user.get_elements()}")
        seq = self.render()
        manager.store_sequence_all(self.trigger_name, seq, self.thing_names)


    def play(self):
        logger.info(f"Song: load {self.trigger_name}")
        self.store_sequence()
        logger.info(f"Song: playing {self.trigger_name}")
        manager.play_song(self.trigger_name)
