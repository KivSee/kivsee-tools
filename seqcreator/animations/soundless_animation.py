from abc import abstractmethod, ABC
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.network import manager
from seqcreator.logging.logger import kivsee_logger as logger


class SoundlessAnimation(ABC):

    def __init__(self, trigger, duration, repeats):
        self.trigger_name = trigger
        self.duration = duration
        self.repeats = repeats

    @abstractmethod
    def render_effects(self):
        """The business logic, the method the builds the sequence.
        """

    def store_sequence(self):
        logger.info(f"storing {self.trigger_name} sequence")
        self.render_effects()
        thing_to_effects = get_effects().thing_to_effects()
        per_thing_config = {thing_name: {
            "effects": effects,
            "duration_ms": self.duration,
            "num_repeats": self.repeats
        } for (thing_name, effects) in thing_to_effects.items()}
        manager.store_sequence_all(self.trigger_name, per_thing_config)

    def play(self):
        logger.info(f"load {self.trigger_name}")
        self.store_sequence()
        logger.info(f"starting soundless animation {self.trigger_name}")
        manager.play_soundless_animation(self.trigger_name)