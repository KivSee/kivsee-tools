from seqcreator.api import timing
from seqcreator.rendering.effects.deprecated import functions_store


def rainbow_effect(segment_name, start_time, end_time, function_start, function_end):
    return {
        "effect_config": {
            "start_time": start_time,
            "end_time": end_time,
            "segments": segment_name
        },
        "rainbow": {
            "hue_start": function_start,
            "hue_end": function_end
        }
    }


def for_each(start, end, segments):
    return [
        rainbow_effect(segment["name"], start, end, functions_store.linear_function(0.3 * idx, 0.7 * idx),
                       functions_store.linear_function(0.8 * idx, 0.2 * idx)) for
        idx, segment in enumerate(segments)]


def all_segments(segments, f1, f2):
    tf = timing.get_timing()
    result = [rainbow_effect(segment, tf.get_start_time_ms(), tf.get_end_time_ms(), f1, f2) for segment in segments]
    return result
