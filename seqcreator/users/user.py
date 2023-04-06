from abc import ABC, abstractmethod
from seqcreator.users.common.songs.nyan import Nyan
<<<<<<< HEAD
from seqcreator.users.common.songs.sandstorm import Sandstorm
=======
from seqcreator.users.common.songs.overthinker import OverThinker
from seqcreator.users.common.songs.peacock import Peacock
from seqcreator.users.common.songs.req import Req
>>>>>>> ce8c00eada70dd20e1c0a0cbed7ead7f6eb37ade
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
    "req": Req,
    "over": OverThinker
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

<<<<<<< HEAD
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
=======
        trigger_class = triggersToClasses.get(trigger_name)
        if not trigger_class:
>>>>>>> ce8c00eada70dd20e1c0a0cbed7ead7f6eb37ade
            return False
        
        trigger_instance = trigger_class()
        trigger_instance.load()
        trigger_instance.play(offset)
        return True
            
 