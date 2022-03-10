from abc import ABC, abstractmethod
from seqcreator.users.common.soundless_animations.even import Even
from seqcreator.users.common.soundless_animations.party import Party
from seqcreator.users.common.soundless_animations.warm import Warm
from seqcreator.infra.logger import kivsee_logger as logger

class User(ABC):

    def __init__(self, name):
        self.name = name

    def play(self, trigger_name) -> bool:
        """Invoke the requested trigger

        Args:
            trigger_name (string): the trigger to invoke, either a song or soundless 
            animation that is implemented by this secuence creator.
        """

        logger.debug(f"{self.name}, got request to create {trigger_name} sequence and play it.")

        if trigger_name == "warm":
            Warm().play()
        elif trigger_name == "party":
            Party().play()
        elif trigger_name == "even":
            Even().play()
        else:
            return False

        return True
            
 