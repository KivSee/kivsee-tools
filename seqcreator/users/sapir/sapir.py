from seqcreator.api import element_provider
from seqcreator.users.sapir.elements import Elements
from seqcreator.users.sapir.soundless_animations.party import Party
from seqcreator.users.sapir.soundless_animations.warm import Warm
from seqcreator.users.user import User
from seqcreator.infra import network_manager
from seqcreator.users.sapir.songs.under import Under
from seqcreator.infra.logger import kivsee_logger as logger

class Sapir(User):

    def __init__(self):
        super().__init__('sapir')
        self.elements = Elements(self.name)
        element_provider.set_element_provider(self.elements)

    def play(self, trigger_name):
        logger.debug(f"{self.name}, got request to create {trigger_name} sequence and play it.")

        # TODO(sapir): let the animation store itself in a registery and remove this list of conditions
        if trigger_name == "warm":
            Warm().play()

        elif trigger_name == "under":
            Under().play()

        elif trigger_name == "party":
            Party().play()
        
        else:
            raise Exception(f"trigger '{self.trigger_name}' not supported by '{self.name}'")
