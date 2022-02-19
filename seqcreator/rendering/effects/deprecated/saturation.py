from seqcreator.rendering.effects.deprecated import functions_store


def saturation_effect(segment_name, start_time, end_time, function):
    return {
        "effect_config": {
            "start_time": start_time,
            "end_time": end_time,
            "segments": segment_name
        },
        "saturation": {
            "mult_factor": function
        }
    }


def for_each(start, end, segments):
    return [saturation_effect(segment["name"], start, end, functions_store.const_function(0.5)) for
            idx, segment in
            enumerate(segments)]