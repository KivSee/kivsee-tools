from seqcreator.api import timing
from seqcreator.rendering.effects.base_effect import BaseEffect

class SnakeEffect(BaseEffect):

    def __init__(self, head, tail_length):
        super().__init__()
        self.head = head
        self.tail_length = tail_length

    def get_effect_params_json(self):
        return {
            "snake": {
                "head": self.head,
                "tail_length": self.tail_length,
            }
        }
