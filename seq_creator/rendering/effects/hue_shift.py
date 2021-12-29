from rendering.function import functions_store


def hue_shift_effect(segment_name, start_time, end_time, function):
    return {
        "effect_config": {
            "start_time": start_time,
            "end_time": end_time,
            "segments": segment_name
        },
        "hue": {
            "offset_factor": function
        }
    }

def for_each(start, end, segments):
    return [hue_shift_effect(segment, start, end,
                             functions_store.comb2_function(functions_store.sin_function(-1, 1, 0, 1.9), 0.7,
                                                      functions_store.sin_function(-1, 1, 0, 3), 0.3))
            for
            idx, segment in
            enumerate(segments)]


