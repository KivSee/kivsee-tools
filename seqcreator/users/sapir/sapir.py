from seqcreator.api import element_provider
from seqcreator.users.user import User
from seqcreator.users.sapir.songs.under_sapir import Under
from seqcreator.users.sapir.elements import Elements

class Sapir(User):

    def __init__(self):
        super().__init__('sapir')
        self.elements = Elements(self.name)
        element_provider.set_element_provider(self.elements)

    def play(self, trigger_name,  offset: int):
        if super().play(trigger_name, offset):
           return True

        elif trigger_name == "under":
            Under().play(offset)

        else:
            raise Exception(f"trigger '{self.trigger_name}' not supported by '{self.name}'")
