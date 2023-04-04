from abc import ABC, abstractmethod
from seqcreator.users.common.songs.nyan import Nyan
from seqcreator.users.common.songs.peacock import Peacock
from seqcreator.users.common.songs.req import Req
from seqcreator.users.common.songs.under import Under
from seqcreator.users.common.soundless_animations.romantic import Romantic
from seqcreator.users.common.soundless_animations.even import Even
from seqcreator.users.common.soundless_animations.party import Party
from seqcreator.users.common.soundless_animations.snake import Snake
from seqcreator.users.common.soundless_animations.warm import Warm
from seqcreator.infra.logger import kivsee_logger as logger
from seqcreator.users.peacock.soundless_animations.purim import Purim

triggersToClasses = {
    "warm": Warm,
    "party": Party,
    "even": Even,
    "romantic": Romantic,
    "under": Under,
    "snake": Snake,
    "nyan": Nyan,
    "peacock": Peacock,
    "purim": Purim,
    "req": Req
}

class User(ABC):

    def __init__(self, name):
        self.name = name

    def play(self, trigger_name, offset) -> bool:
        """Invoke the requested trigger

        Args:
            trigger_name (string): the trigger to invoke, either a song or soundless 
            animation that is implemented by this sequence creator.
        """

        logger.debug(f"{self.name}, got request to create {trigger_name} sequence and play it.")

        trigger_class = triggersToClasses.get(trigger_name)
        if not trigger_class:
            return False
        
        trigger_instance = trigger_class()
        trigger_instance.load()
        trigger_instance.play(offset)
        return True
            
 