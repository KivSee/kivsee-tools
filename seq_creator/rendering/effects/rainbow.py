from rendering.function import functions_store

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

