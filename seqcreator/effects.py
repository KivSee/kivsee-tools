
def const_color_effect(segment_name, start_time, end_time, hue):
    return {
        "effect_config": {
            "start_time": start_time,
            "end_time": end_time,
            "segments": segment_name
        },
        "const_color": {
            "color": {
                "hue": hue,
                "sat": 1.0,
                "val": 0.3
            }
        }
    }

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


def saturation_shift_effect(segment_name, start_time, end_time, function):
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
