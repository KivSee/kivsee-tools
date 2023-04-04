from abc import abstractmethod, ABC
from seqcreator.rendering.effects_factory import get_effects
from seqcreator.infra import network_manager
from seqcreator.infra.logger import kivsee_logger as logger


class Animation(ABC):

    def __init__(self, trigger, duration, repeats):
        """_summary_

        Args:
            trigger (_type_): name of the trigger
            duration (_type_): length of the animation in miliseconds
            repeats (_type_): how many times to repeat the animation within the time duration
        """
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
        network_manager.store_sequence_all(self.trigger_name, per_thing_config)

    @abstractmethod
    def play(self):
        """ Triggers the animation, either for sound or soundless animation.
        """

    def load(self):
        pass
