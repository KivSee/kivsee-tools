from seqcreator.rendering.effects.deprecated import functions_store
from seqcreator.api import timing


def brightness_effect(segment_name, start_time, end_time, function):
    return {
        "effect_config": {
            "start_time": start_time,
            "end_time": end_time,
            "segments": segment_name
        },
        "brightness": {
            "mult_factor": function
        }
    }


def for_time(start, end, segments):
    return [brightness_effect(segment["name"], start, end,
                              functions_store.comb2_function(functions_store.sin_function(-1, 1, 0, 1.9), 0.7,
                                                             functions_store.sin_function(-1, 1, 0, 3), 0.3))
            for
            idx, segment in
            enumerate(segments)]


def all_segments(segments, function):
    tf = timing.get_timing()
    result = [brightness_effect(segment, tf.get_start_time_ms(), tf.get_end_time_ms(), function) for idx, segment in
              enumerate(segments)]
    return result
