

from seqcreator.api.element_provider import ElementProvider


class Elements(ElementProvider):

    def __init__(self, user_name):
        super().__init__(user_name)
        
    def living_room(self):
        return  [('spiral-big', 'spiral1'), ('spiral-big', 'spiral2'), ('spiral-big', 'spiral3'), ('spiral-big', 'spiral4'), ('spiral-big', 'spiral5'), ('spiral-big', 'outline'), ('spiral-big', 'spiral6'), ('spiral-big', 'subout1'), ('spiral-big', 'subout2'), ('spiral-big', 'subout3'), ('spiral-big', 'subout4'), ('spiral-big', 'subout5'), ('spiral-big', 'subout6'), ('spiral-big', 'subout7'), ('spiral-big', 'subout8'), ('spiral-big', 'subout9'), ('spiral-big', 'subout10'), ('spiral-small', 'spiral1'), ('spiral-small', 'spiral2'), ('spiral-small', 'spiral3'), ('spiral-small', 'outline'), ('spiral-small', 'subout1'), ('spiral-small', 'subout2'), ('spiral-small', 'subout3'), ('spiral-small', 'subout4'), ('spiral-small', 'subout5'), ('spiral-small', 'subout6'), ('spiral-small', 'subout7'), ('spiral-small', 'subout8'), ('spiral-small', 'subout9'), ('spiral-small', 'subout10')]