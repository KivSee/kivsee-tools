import imp
import os
import requests
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
    requests.put(f"{config.raspberry_pi_addr}:{config.object_service_port}/thing/{name}", json=thing_segment_mapping)
    sequence = mapping_sequence(segments_list)
    res = requests.put(f"{config.raspberry_pi_addr}:{config.sequence_service_port}/triggers/{mapping_trigger_name}/objects/{name}", json=sequence)

def send_for_user(user):
    dir = os.path.join('objectsetup', 'mapping', user)
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