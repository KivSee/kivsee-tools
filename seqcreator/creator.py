import requests
import json

def segment_const_color_effect(segment_name, start_time, end_time, hue):
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

def segment_rainbow_effect(segment_name, start_time, end_time, hue_start, hue_end):
    return {
        "effect_config": {
            "start_time": start_time,
            "end_time": end_time,
            "segments": segment_name
        },
        "rainbow": {
            "hue_start" : {
                "linear": {
                    "start": hue_start,
                    "end": hue_end,
                }
            },
            "hue_end" : {
                "linear" : {
                    "start": hue_end,
                    "end": hue_start,
                }
            }

        }
    }

def build_animation(trigger_name, thing_name, config):
    sequence = build_etta(config["segments"], 7000)
    res = requests.put(f"http://192.168.1.9:8082/triggers/{trigger_name}/objects/{thing_name}", json=sequence)
    print(res)
    print("request sent")


def build_basic_seq(segments):
    return {
        "effects": [segment_const_color_effect(segment["name"], 0, 500, 0.3 * idx) for idx, segment in enumerate(segments)],
        "duration_ms": 1000,
        "num_repeats": 0
    }

def build_etta(segments, duration):
    return {
        "effects": [segment_rainbow_effect(segment["name"], 0, int(duration*0.75), 0.3 * idx, 0.7 * idx) for idx, segment in
                     enumerate(segments)],
         "duration_ms": duration,
         "num_repeats": 0
    }


thing_name = "spiral-small"
trigger_name = "etta"
response = requests.get(f"http://192.168.1.9:8081/led-object/{thing_name}")
segments_mapping = response.json()
build_animation(trigger_name, thing_name, segments_mapping)
requests.post(f"http://192.168.1.9:8083/trigger/{trigger_name}")