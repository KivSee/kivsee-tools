from abc import abstractmethod
from seqcreator.animations.animation import Animation
from seqcreator.infra import network_manager
from seqcreator.infra.logger import kivsee_logger as logger

class Song(Animation):

    def __init__(self, trigger, duration, repeats):
        super(Song, self).__init__(trigger, duration, repeats)

    def play(self, offset: int):
        logger.info(f"load {self.trigger_name}")
        self.store_sequence()
        logger.info(f"playing {self.trigger_name}")
        network_manager.play_song(self.trigger_name, offset*1000)
