from seqcreator.api import element_provider
from seqcreator.users.user import User
from seqcreator.users.peacock.elements import Elements
from seqcreator.api import element_provider

class Peacock(User):

    def __init__(self):
        super().__init__('peacock')
        self.elements = Elements(self.name)
        element_provider.set_element_provider(self.elements)

    def play(self, trigger_name,  offset: int):
        if super().play(trigger_name, offset):
           return True

        elif trigger_name == "nyan":
            Nyan(element_provider.get_element_provider()).play(offset)

        else:
            raise Exception(f"trigger '{self.trigger_name}' not supported by '{self.name}'")
