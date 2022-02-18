from abc import abstractmethod, ABC
from seqcreator.rendering.effects_factory import ColoringEffectFactory, MaskingEffectFactory
from seqcreator.network import manager
from seqcreator.users.effects_list_holder import EffectsListHolder
from seqcreator.logging.logger import kivsee_logger as logger


class Animation(ABC):

    def __init__(self, trigger, duration, repeats, elements):
        self.trigger_name = trigger
        self.duration = duration
        self.holder = EffectsListHolder()
        self.repeats = repeats
        self.elements = elements
        self.coloring_effect = ColoringEffectFactory(self.elements, self.holder)
        self.masking_effect = MaskingEffectFactory(self.elements, self.holder)

    @abstractmethod
    def render_effects(self):
        """The business logic, the method the builds the sequence.
        """

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
        manager.store_sequence_all(self.trigger_name, seq, self.elements.all_things())

    def play(self):
        logger.info(f"load {self.trigger_name}")
        self.store_sequence()
        logger.info(f"starting soundless animation {self.trigger_name}")
        manager.play_animation(self.trigger_name)