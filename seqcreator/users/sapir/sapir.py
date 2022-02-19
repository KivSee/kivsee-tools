from seqcreator.api import element_provider
from seqcreator.users.sapir.soundless_animations.warm import Warm
from seqcreator.users.user import User
from seqcreator.infra import network_manager
from seqcreator.users.sapir.songs.under import Under
from seqcreator.infra.logger import kivsee_logger as logger

class Sapir(User):

    def __init__(self):
        super().__init__('sapir')
        element_provider.set_element_provider(element_provider.ElementProvider('sapir'))

    def play(self, trigger_name):
        logger.debug(f"{self.name}, got request to create {trigger_name} sequence and play it.")

        if trigger_name == "warm":
            warm = Warm()
            warm.play()

        elif trigger_name == "under":
            under = Under()
            under.play()
        
        else:
            raise Exception(f"trigger '{self.trigger_name}' not supported by '{self.name}'")