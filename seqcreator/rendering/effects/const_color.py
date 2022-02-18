from seqcreator.infra import timing
from seqcreator.infra.color import Color
from seqcreator.rendering.effects.effect import Effect

class ConstColor(Effect):

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
