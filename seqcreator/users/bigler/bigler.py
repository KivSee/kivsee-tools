from seqcreator.api import element_provider
from seqcreator.users.bigler.elements import Elements
from seqcreator.users.bigler.soundless_animations.deprecated import Warm
from seqcreator.users.user import User
from seqcreator.infra import network_manager
from seqcreator.infra.logger import kivsee_logger as logger

class Bigler(User):

    def __init__(self):
        super().__init__('bigler')
        self.elements = Elements(self.name)
        element_provider.set_element_provider(self.elements)

    def play(self, trigger_name):
        if super().play(trigger_name):
           return True

        # elif trigger_name == "under":
        #     under = Under()
        #     under.play()
        
        else:
            raise Exception(f"trigger '{self.trigger_name}' not supported by '{self.name}'")
