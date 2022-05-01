from seqcreator.animations.animation import Animation
from seqcreator.infra import network_manager
from seqcreator.infra.logger import kivsee_logger as logger


class SoundlessAnimation(Animation):

    def __init__(self, trigger, duration, repeats):
        super(SoundlessAnimation, self).__init__(trigger, duration, repeats)

    def play(self, offset: int = 0):
        logger.info(f"load {self.trigger_name}")
        self.store_sequence()
        logger.info(f"starting soundless animation {self.trigger_name}")
        network_manager.play_soundless_animation(self.trigger_name, offset*1000)
