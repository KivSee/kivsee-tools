import requests
from objectsetup.objects.sapir import spiralbig
from objectsetup.objects.sapir import spiralsmall
from objectsetup.objects.sapir import sofa
from objectsetup.objects.sapir import osb
from objectsetup.objects.sapir import table
from objectsetup.objects.sapir import kitchen
from objectsetup.objects.sapir import whisper


def segment_const_color_effect(segment_name, hue):
    return {
        "effect_config": {
            "start_time": 0,
            "end_time": 1000,
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


mapping_trigger_name = "mapping"


def configure(name, config):
    requests.put(f"http://192.168.1.9:8081/thing/{name}", json=config)
    sequence = mapping_sequence(config["segments"])
    res = requests.put(f"http://192.168.1.9:8082/triggers/{mapping_trigger_name}/objects/{name}", json=sequence)
    print(res)
    print("request sent")


def run():
    configure("spiral-big", spiralbig.val)
    configure("spiral-small", spiralsmall.val)
    configure("sofa", sofa.val)
    configure("osb", osb.val)
    configure("table", table.val)
    configure("kitchen", kitchen.val)
    configure("whisper", whisper.val)
    requests.post(f"http://192.168.1.9:8083/trigger/{mapping_trigger_name}")