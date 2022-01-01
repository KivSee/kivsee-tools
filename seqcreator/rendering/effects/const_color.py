from seqcreator.infra import timing


def const_color_effect(segment_name, start_time, end_time, hue, sat=1.0, val=0.3):
    return {
        "effect_config": {
            "start_time": start_time,
            "end_time": end_time,
            "segments": segment_name
        },
        "const_color": {
            "color": {
                "hue": hue,
                "sat": sat,
                "val": val
            }
        }
    }


def for_each(start, end, segments, hue=0.5):
    result = []
    for segment in segments:
        segment_name = segment["name"]
        result.append(const_color_effect(segment_name, start, end, hue))
    return result


def all_segments(segments, color):
    tf = timing.get_timing()
    result = [const_color_effect(segment, tf.get_start_time_ms(), tf.get_end_time_ms(), color[0], color[1],
                                 color[2]) for idx, segment in enumerate(segments)]
    return result
