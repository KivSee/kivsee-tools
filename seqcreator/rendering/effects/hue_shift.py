from seqcreator.api import timing
from seqcreator.api.color import Color
from seqcreator.rendering.effects.base_effect import BaseEffect


class HueShift(BaseEffect):

    def __init__(self, offset_factor):
        super().__init__()
        self.offset_factor = offset_factor

    def get_effect_params_json(self):
        return {
            "hue": {
                "offset_factor": self.offset_factor
            }
        }
