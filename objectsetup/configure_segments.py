import requests
import json
from objects.sapir import spiralbig
from objects.sapir import spiralsmall
def segment_const_color_effect(segment_name, hue):
    return {
        "effect_config": {
            "start_time": 0,
            "end_time": 500,
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

def mapping_sequence(segments):
    return {
        "effects": [segment_const_color_effect(segment["name"], 0.3 * idx) for idx, segment in enumerate(segments)],
        "duration_ms": 1000,
        "num_repeats": 0
    }

def configure(name, config):
    mapping_trigger_name = "mapping"
    requests.put(f"http://192.168.1.9:8081/led-object/{name}", json=config)
    sequence = mapping_sequence(config["segments"])
    res = requests.put(f"http://192.168.1.9:8082/triggers/{mapping_trigger_name}/objects/{name}", json=sequence)
    requests.post(f"http://192.168.1.9:8083/trigger/{mapping_trigger_name}")
    print("request sent")


configure("spiral-big", spiralbig.spiral_big_val)
configure("spiral-small", spiralsmall.spiral_small_val)