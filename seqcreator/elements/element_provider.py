from seqcreator.network import manager
from seqcreator.logging.logger import kivsee_logger as logger


class ElementProvider:

    def __init__(self, user_name):
        self._user_name = user_name
        self.thing_to_segments = {
            "spiral-small": ["spiral1", "spiral2", "spiral3", "subout1", "subout2", "subout3", "subout4", "subout5",
                                    "subout6", "subout7", "subout8", "subout9", "subout10"],
            "spiral-big": ["spiral1", "spiral2", "spiral3", "spiral4", "spiral5", "subout1", "subout2", "subout3", "subout4", "subout5",
                                    "subout6", "subout7", "subout8", "subout9", "subout10"],
            "osb": ["1", "2", "3", "4"],
            "table": ["1", "2", "3", "4"]
        }

    def current_segments(self):
        return [('spiral-big', 'spiral1'), ('osb', '1')]

_ELEMENTS = None

def set_element_provider(elements_provider: ElementProvider):
    global _ELEMENTS
    _ELEMENTS = elements_provider

def get_element_provider() -> ElementProvider:
    return _ELEMENTS