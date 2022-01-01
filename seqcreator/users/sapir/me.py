from overrides import overrides
from seqcreator.users.user import User
from seqcreator.network import manager
from seqcreator.users.sapir.songs.deprecated import etta, baz, under_basic
from seqcreator.users.sapir.songs.under import Under


class Sapir(User):

    def __init__(self):
        super().__init__("sapir", ["spiral-small", "spiral-big"])
        # TODO get the elements from the leds-object?

    def play(self, trigger_name):
        # logger.debug(f"{self.name}, {trigger_name} attempt to play!!!")

        if trigger_name == "baz":
            baz.build_and_store_sequence()
            manager.play_animation(trigger_name)

        elif trigger_name == "etta":
            etta.build_and_store_sequence()
            manager.play_song(trigger_name)

        elif trigger_name == "under_basic":
            under_basic.build_and_store_sequence()
            manager.play_song("under")

        elif trigger_name == "under":
            # TODO sapir pass an element provider
            under = Under(self.get_elements())
            under.play()

        else:
            raise Exception(f"trigger '{self.trigger_name}' not supported by '{self.name}'")
