

from seqcreator.api.element_provider import ElementProvider


class Elements(ElementProvider):

    def __init__(self, user_name):
        super().__init__(user_name)
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
