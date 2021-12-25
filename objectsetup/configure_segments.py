import requests
import json

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

object_val = {
        "numberOfPixels": 1168,
        "segments": [{
            "name": "spiral1",
            "indices": list(range(0, 92))
        },
        {
            "name": "spiral2",
            "indices": list(range(92, 391))
        },
        {
            "name": "spiral3",
            "indices": list(range(391, 691))
        },
        {
            "name": "spiral4",
            "indices": list(range(691, 850))
        },
        {
            "name": "spiral5",
            "indices": list(range(830, 878))
        },
        {
            "name": "outline",
            "indices": list(range(878, 1168))
        },
        {
            "name": "spiral6",
            "indices": list(range(1168, 1307))
        },
        {
            "name": "subout1",
            "indices": list(range(878, 932))
        },
        {
            "name": "subout2",
            "indices": list(range(932, 954)) + list(range(1150, 1168))
        },
        {
            "name": "subout3",
            "indices": list(range(954, 987))
        },
        {
            "name": "subout4",
            "indices": list(range(987, 1021))
        },
        {
            "name": "subout5",
            "indices": list(range(1021, 1028)) + list(range(1152, 1057))
        },
        {
            "name": "subout6",
            "indices": list(range(1028, 1048))
        },
        {
            "name": "subout7",
            "indices": list(range(1057, 1091))
        },
        {
            "name": "subout8",
            "indices": list(range(1091, 1101))
        },
        {
            "name": "subout9",
            "indices": list(range(1101, 1123))
        },
        {
            "name": "subout10",
            "indices": list(range(1123, 1152))
        }
        ]
    }

configure("spiral-big", object_val)