from seqcreator.api import timing
from seqcreator.api.color import Color
from seqcreator.rendering.effects.base_effect import BaseEffect


class Saturation(BaseEffect):

    def __init__(self, mult_factor):
        super().__init__()
        self.mult_factor = mult_factor

    def get_effect_params_json(self):
        return {
            "saturation": {
                "mult_factor": self.mult_factor
            }
        }
