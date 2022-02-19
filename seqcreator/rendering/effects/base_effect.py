
from abc import ABC, abstractmethod

from seqcreator.api import timing


class BaseEffect(ABC):

    def __init__(self):
        super().__init__()

    def to_json(self, segment_name):
        tf = timing.get_timing()
        params = self.get_effect_params_json()
        return {
            "effect_config": {
                "start_time": tf.get_start_time_ms(),
                "end_time": tf.get_end_time_ms(),
                "segments": segment_name
            },
            **params
        }

    @abstractmethod
    def get_effect_params_json(self):
        pass

