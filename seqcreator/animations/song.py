from abc import abstractmethod
from seqcreator.animations.animation import Animation
from seqcreator.infra import network_manager
from seqcreator.infra.logger import kivsee_logger as logger
from seqcreator.api import timing

class Song(Animation):

    def __init__(self, trigger, duration, repeats):
        super(Song, self).__init__(trigger, duration, repeats)

    def play(self, offset):
        logger.info(f"load {self.trigger_name}")
        self.store_sequence()
        logger.info(f"playing {self.trigger_name}")
        
        tf = timing.get_timing()
        bpm = tf._bpm

        offset_in_ms = int(offset)*1000
        print(repr(offset_in_ms))
        
        network_manager.play_song(self.trigger_name, offset_in_ms)
