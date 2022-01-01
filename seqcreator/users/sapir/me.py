from overrides import overrides
from seqcreator.users.user import User
from seqcreator.network import manager
from seqcreator.users.sapir.songs.deprecated import etta, baz, under_basic
from seqcreator.users.sapir.songs.under import Under
from seqcreator.logging.logger import kivsee_logger as logger


class Sapir(User):

    def __init__(self):
        # TODO this is temporay, the element provider should retrieve the elements from the led-object-service
        super().__init__("sapir", ["spiral-small", "spiral-big"],
                         ["spiral1", "spiral2", "spiral3", "subout1", "subout2", "subout3", "subout4", "subout5",
                          "subout6", "subout7", "subout8", "subout9", "subout10"])

    def play(self, trigger_name):
        logger.debug(f"{self.name}, got request to create {trigger_name} sequence and play it.")

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
            under = Under(self.element_provider)
            under.play()

        else:
            raise Exception(f"trigger '{self.trigger_name}' not supported by '{self.name}'")
