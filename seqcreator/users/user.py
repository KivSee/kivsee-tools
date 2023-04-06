from abc import ABC, abstractmethod
from seqcreator.users.common.songs.nyan import Nyan
from seqcreator.users.common.songs.sandstorm import Sandstorm
from seqcreator.users.common.songs.under import Under
from seqcreator.users.common.soundless_animations.romantic import Romantic
from seqcreator.users.common.soundless_animations.even import Even
from seqcreator.users.common.soundless_animations.party import Party
from seqcreator.users.common.soundless_animations.snake import Snake
from seqcreator.users.common.soundless_animations.warm import Warm
from seqcreator.infra.logger import kivsee_logger as logger
from seqcreator.users.peacock.soundless_animations.purim import Purim

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

        if trigger_name == "warm":
            Warm().play()
        elif trigger_name == "party":
            Party().play()
        elif trigger_name == "even":
            Even().play()
        elif trigger_name == "romantic":
            Romantic().play()
        elif trigger_name == "under":
            Under().play(offset)
        elif trigger_name == "snake":
            Snake().play()
        elif trigger_name == "nyan":
            Nyan().play(offset)
        elif trigger_name == "sandstorm":
            Sandstorm().play(offset)
        elif trigger_name == "purim":
            Purim().play(offset)
        else:
            return False

        return True
            
 