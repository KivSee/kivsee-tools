import requests

import config
from seqcreator.rendering.effects import (rainbow, brightness, hue_shift, const_color)
from seqcreator.rendering.function import functions_store
from seqcreator.network import manager


thing_names = ["spiral-small", "spiral-big"]
trigger_name = "under"
effectsList = []
elements = []

def get_segments(thing_name):
    response = requests.get(f"{config.raspberry_pi_addr}:{config.object_service_port}/led-object/{thing_name}")
    return response.json()


def mapping_sequence(duration):
    data = [("spiral1", 1166), ("spiral2", 4666), ("spiral3", 8367), ("subout1", 10400), ("subout5", 12240),
            ("subout6", 16020), ("subout7", 19700), ("subout8", 23530), ("subout9", 24780)]

    for a_tuple in enumerate(data):
        timestamp = a_tuple[1][1]
        segment_name = a_tuple[1][0]
        effectsList.append(
            rainbow.rainbow_effect(segment_name, timestamp, duration, functions_store.linear_function(0.3, 0.7),
                                   functions_store.linear_function(0.8, 0.2)))
    effectsList.append(hue_shift.hue_shift_effect("all", 0, duration, functions_store.linear_function(0, 1)))
    effectsList.append(rainbow.rainbow_effect("all", 24450, duration, functions_store.sin_function(0.0, 0.1, 0, 5),
                                   functions_store.linear_function(0.8, 0.2)))
    effectsList.append(
        rainbow.rainbow_effect("all", 24450, 37450, functions_store.linear_function(0.1, 0.9),
                               functions_store.linear_function(0.9, 0.2)))
    effectsList.append(brightness.brightness_effect("all", 24450, 37450,
                                                     functions_store.repeat_function(28, functions_store.linear_function(0.3, 0.6))))
    effectsList.append(brightness.brightness_effect("all", 24450, duration, functions_store.const_function(0.6)))
    return {
            "effects": effectsList,
            "duration_ms": duration,
            "num_repeats": 0
        }


def build_and_store_sequence():
    duration = 147000
    seq = mapping_sequence(duration)
    manager.store_sequence_all(trigger_name, seq, thing_names)
