from seqcreator.animation.animation import Animation
from seqcreator.network import manager
from seqcreator.logging.logger import kivsee_logger as logger


class Song(Animation):

    def __init__(self, trigger, duration, repeats, elements):
        super(Song, self).__init__(trigger, duration, repeats, elements)

    def render_effects(self):
        # stub, needs to be overridden by child
        pass

    def play(self):
        logger.info(f"Song: load {self.trigger_name}")
        self.store_sequence()
        logger.info(f"Song: playing {self.trigger_name}")
        manager.play_song(self.trigger_name)
