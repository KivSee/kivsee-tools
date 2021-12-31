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
        print(f"{self.name}, {trigger_name} attempt to play!!!")

        # if trigger_name == "baz":
        #     print("1")
        #     baz.build_and_store_sequence()
        #     manager.play_animation(trigger_name)
        #
        # elif trigger_name == "etta":
        #     print("2")
        #     etta.build_and_store_sequence()
        #     manager.play_song(trigger_name)
        #
        # elif trigger_name == "under_basic":
        #     print("3")
        #     under_basic.build_and_store_sequence()
        #     manager.play_song("under")

        if trigger_name == "under":
            # TODO sapir pass an element provider
            under = Under(self.get_elements())
            under.play()
            print("Success!")
            return
        else:
            print("5")
            raise Exception(f"trigger '{self.trigger_name}' not supported by '{self.name}'")
