from seqcreator.api import timing
from seqcreator.api.color import Color
from seqcreator.rendering.effects.base_effect import BaseEffect

class ConstColor(BaseEffect):

    def __init__(self, color: Color):
        super().__init__()
        self.color = color

    def get_effect_params_json(self):
        return {
            "const_color": {
                "color": {
                    "hue": self.color.hue,
                    "sat": self.color.sat,
                    "val": self.color.val
                }
            }
        }
