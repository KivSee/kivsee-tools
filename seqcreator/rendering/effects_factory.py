from seqcreator.api.element_provider import get_element_provider

class Effects:

    def __init__(self):
        self.things_effects = []

    def add_effect(self, effect):
        current_thing_segments = get_element_provider().current_segments()
        thing_and_effect_json = [(thing_name, effect.to_json(segment_name)) for (thing_name, segment_name) in current_thing_segments]
        self.things_effects.extend(thing_and_effect_json)

    def thing_to_effects(self):
        things = dict()
        for (thing_name, effect_json) in self.things_effects:
            if thing_name in things:
                things[thing_name].append(effect_json)
            else:
                things[thing_name] = [effect_json]
        return things


_EFFECTS = Effects()

def get_effects() -> Effects:
    return _EFFECTS

