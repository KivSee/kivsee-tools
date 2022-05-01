from seqcreator.api import element_provider
from seqcreator.users.amir.elements import Elements
from seqcreator.users.user import User
from seqcreator.infra import network_manager
from seqcreator.infra.logger import kivsee_logger as logger

class Amir(User):

    def __init__(self):
        super().__init__('amir')
        self.elements = Elements(self.name)
        element_provider.set_element_provider(self.elements)

    def play(self, trigger_name,  offset: int):
        if super().play(trigger_name, offset):
           return True

        # elif trigger_name == "custome_trigger":
        #     under = Under()
        #     under.play()
        
        else:
            raise Exception(f"trigger '{self.trigger_name}' not supported by '{self.name}'")
