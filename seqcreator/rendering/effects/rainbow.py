from seqcreator.api import timing
from seqcreator.api.color import Color
from seqcreator.rendering.effects.base_effect import BaseEffect


class Rainbow(BaseEffect):

    def __init__(self, start, end):
        super().__init__()
        self.function_start = start
        self.function_end = end

    def get_effect_params_json(self):
        return {
            "rainbow": {
                "hue_start": self.function_start,
                "hue_end": self.function_end
            }
        }
