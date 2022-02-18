from seqcreator.users.sapir.soundless_animations.warm import Warm
from seqcreator.users.user import User
from seqcreator.network import manager
from seqcreator.users.sapir.songs.deprecated import etta, baz, under_basic
from seqcreator.users.sapir.songs.under import Under
from seqcreator.logging.logger import kivsee_logger as logger

# all_things = {
#   "spiral-small": ["spiral1", "spiral2", "spiral3", "subout1", "subout2", "subout3", "subout4", "subout5",
#                           "subout6", "subout7", "subout8", "subout9", "subout10"],
#   "spiral-big": ["spiral1", "spiral2", "spiral3", "spiral4", "spiral5", "subout1", "subout2", "subout3", "subout4", "subout5",
#                           "subout6", "subout7", "subout8", "subout9", "subout10"],
#   "osb": ["1", "2", "3", "4"],
#   "table": ["1", "2", "3", "4"]
# }

class Sapir(User):

    def __init__(self):
        # TODO(Sapir): the element provider should retrieve the elements from the led-object-service
        super().__init__("sapir", ["spiral-small", "spiral-big"],
                         ["spiral1", "spiral2", "spiral3", "subout1", "subout2", "subout3", "subout4", "subout5",
                          "subout6", "subout7", "subout8", "subout9", "subout10"])

    def play(self, trigger_name):
        logger.debug(f"{self.name}, got request to create {trigger_name} sequence and play it.")

        if trigger_name == "warm":
            warm = Warm(self.elements)
            warm.play()

        elif trigger_name == "under":
            under = Under(self.elements)
            under.play()
        
        else:
            raise Exception(f"trigger '{self.trigger_name}' not supported by '{self.name}'")
