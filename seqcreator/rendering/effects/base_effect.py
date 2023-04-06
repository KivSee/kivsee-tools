
from abc import ABC, abstractmethod

from seqcreator.api.timing import get_timing
from seqcreator.api.context import timing


class BaseEffect(ABC):

    def __init__(self):
        super().__init__()

    def to_json(self, segment_name):
        params = self.get_effect_params_json()

        tf = get_timing()
        if tf:
            return {
                "effect_config": {
                    "start_time": tf.get_start_time_ms(),
                    "end_time": tf.get_end_time_ms(),
                    "segments": segment_name,
                    "repeat_num": tf.repeats,
                    "repeat_start": 0,
                    "repeat_end": 1,
                },
                **params
            }
        else:
            current_time_frame = timing.get_timing()
            current_cycle = timing.get_cycle()
            repeats_attributes = {
                "repeat_num": current_time_frame.total_units / current_cycle.units_in_cycle,
                "repeat_start": current_cycle.cycle_start_rel,
                "repeat_end": current_cycle.cycle_end_rel,
            } if current_cycle else {}
            return {
                "effect_config": {
                    "start_time": current_time_frame.start_time_ms,
                    "end_time": current_time_frame.end_time_ms,
                    "segments": segment_name,
                    **repeats_attributes,
                },
                **params
            }


    @abstractmethod
    def get_effect_params_json(self):
        pass

