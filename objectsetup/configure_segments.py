import imp
import os
import requests
from objectsetup.mapping.sapir import spiralbig
from objectsetup.mapping.sapir import spiralsmall
from objectsetup.mapping.sapir import sofa
from objectsetup.mapping.sapir import osb
from objectsetup.mapping.sapir import table
from objectsetup.mapping.sapir import kitchen as sapir_kitchen
from objectsetup.mapping.sapir import whisper
from objectsetup.mapping.bigler import curtains
from objectsetup.mapping.bigler import shelf
from objectsetup.mapping.bigler import kitchen as bigler_kitchen
from objectsetup.mapping.bigler import ac_top
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

def send_for_user(user):
    dir = f"objectsetup/mapping/{user}"
    list_modules = os.listdir(dir)
    list_modules.remove("__init__.py")
    for module_name in list_modules:
        thing_name = module_name.split(".")[0]
        thing_config = imp.load_source("module", os.path.join(dir, module_name)).val
        configure(thing_name, thing_config)

def run(user):
    send_for_user(user)
    # print("User name is not supported")
    requests.post(f"{config.raspberry_pi_addr}:{config.trigger_service_port}/trigger/{mapping_trigger_name}")