import requests
from objectsetup.objects.sapir import spiralbig
from objectsetup.objects.sapir import spiralsmall
from objectsetup.objects.sapir import sofa
from objectsetup.objects.sapir import osb
from objectsetup.objects.sapir import table
from objectsetup.objects.sapir import kitchen
from objectsetup.objects.sapir import whisper
import config

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

def configure(name, thing_segment_mapping):
    requests.put(f"{config.raspberry_pi_addr}:{config.object_service_port}/thing/{name}", json=thing_segment_mapping)
    sequence = mapping_sequence(thing_segment_mapping["segments"])
    res = requests.put(f"{config.raspberry_pi_addr}:{config.sequence_service_port}/triggers/{mapping_trigger_name}/objects/{name}", json=sequence)
    print(res)
    print("request sent")


def run():
    print(config.__dict__)
    if config.user_name == "sapir":
        configure("spiral-big", spiralbig.val)
        configure("spiral-small", spiralsmall.val)
        configure("sofa", sofa.val)
        configure("osb", osb.val)
        configure("table", table.val)
        configure("kitchen", kitchen.val)
        configure("whisper", whisper.val)
    elif config.user_name == "amir":
        pass
    elif config.user_name == "bigler":
        pass
    else:
        print("User name is not supported")

    requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/trigger/{mapping_trigger_name}")