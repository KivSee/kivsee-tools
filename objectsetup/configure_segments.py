import requests
from objectsetup.mapping.sapir import spiralbig
from objectsetup.mapping.sapir import spiralsmall
from objectsetup.mapping.sapir import sofa
from objectsetup.mapping.sapir import osb
from objectsetup.mapping.sapir import table
from objectsetup.mapping.sapir import kitchen
from objectsetup.mapping.sapir import whisper
from objectsetup.mapping.bigler import curtains
from objectsetup.mapping.bigler import shelf
from objectsetup.mapping.bigler import kitchen
from objectsetup.mapping.bigler import ac_top
from objectsetup.mapping.bigler import cabbage1
from objectsetup.mapping.bigler import cabbage2
from objectsetup.mapping.bigler import star
from objectsetup.mapping.bigler import gloves
from objectsetup.mapping.bigler import tv
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
    segments_list = thing_segment_mapping["segments"]
    last_pixel_index = thing_segment_mapping["numberOfPixels"]
    segments_list.insert(0, {"name": "all","pixels": [dict({"index": n}) for n in range(0, last_pixel_index)]})
    requests.put(f"{config.raspberry_pi_addr}:{config.object_service_port}/thing/{name}", json=thing_segment_mapping)
    sequence = mapping_sequence(segments_list)
    res = requests.put(f"{config.raspberry_pi_addr}:{config.sequence_service_port}/triggers/{mapping_trigger_name}/objects/{name}", json=sequence)
    print(res)
    print("request sent")

def run(user):
    if user == "sapir":
        configure("spiral-big", spiralbig.val)
        configure("spiral-small", spiralsmall.val)
        configure("sofa", sofa.val)
        configure("osb", osb.val)
        configure("table", table.val)
        configure("kitchen", kitchen.val)
        configure("whisper", whisper.val)
    elif user == "amir":
        pass
    elif user == "bigler":
        configure("curtains", curtains.val)
        configure("shelf", shelf.val)
        configure("kitchen", kitchen.val)
        configure("ac_top", ac_top.val)
        configure("cabbage1", cabbage1.val)
        configure("cabbage2", cabbage2.val)
        configure("star", star.val)
        configure("gloves", gloves.val)
        configure("tv", tv.val)
    else:
        print("User name is not supported")

    # Playing {mapping_trigger_name} sequence
    requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/trigger/{mapping_trigger_name}")