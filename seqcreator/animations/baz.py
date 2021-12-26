import effects as effects_factory
import functions as func_factory
import requests
from config import *

def const_list(start, end, segments):
    return [effects_factory.const_color_effect(segment["name"], start, end, 0.4) for
            idx, segment in enumerate(segments)]

def hue_shift_list(start, end, segments):
    return [effects_factory.hue_shift_effect(segment["name"], start, end,
                                             func_factory.comb2_function(func_factory.sin_function(-1, 1, 0, 1.9), 0.7,
                                                                         func_factory.sin_function(-1, 1, 0, 3), 0.3))
            for
            idx, segment in
            enumerate(segments)]


def saturation_list(start, end, segments):
    return [effects_factory.saturation_shift_effect(segment["name"], start, end, func_factory.const_function(0.5)) for
            idx, segment in
            enumerate(segments)]


def rainbow_list(start, end, segments):
    return [
        effects_factory.rainbow_effect(segment["name"], start, end, func_factory.linear_function(0.3 * idx, 0.7 * idx),
                                       func_factory.linear_function(0.8 * idx, 0.2 * idx)) for
        idx, segment in enumerate(segments)]


def brightness_list(start, end, segments):
    return [effects_factory.brightness_effect(segment["name"], start, end,
                                              func_factory.comb2_function(func_factory.sin_function(-1, 1, 0, 1.9), 0.7,
                                                                          func_factory.sin_function(-1, 1, 0, 3), 0.3))
            for
            idx, segment in
            enumerate(segments)]


effects = []


def build_baz(segments, duration):
    effects.extend(const_list(0, int(duration * 0.5), segments))
    effects.extend(hue_shift_list(0, int(duration * 0.25), segments))
    effects.extend(saturation_list(int(duration * 0.25), int(duration * 0.5), segments))
    effects.extend(rainbow_list(int(duration * 0.1), int(duration * 0.9), segments))
    effects.extend(brightness_list(int(duration * 0.1), int(duration * 0.9), segments))
    effects.extend(hue_shift_list(int(duration * 0.1), int(duration * 0.9), segments))
    effects.extend(rainbow_list(int(duration * 0.75), int(duration), segments))
    effects.append(effects_factory.brightness_effect("all", 0, duration, func_factory.const_function(0.5)))

    # print(effects)
    return {
        # const_color_effect_list + hue_shift_effect_list + saturation_shift_list +
        "effects": effects,
        "duration_ms": duration,
        "num_repeats": 0
    }


trigger_name = "baz"
duration = 22000

thing_names = ["spiral-small", "spiral-big"]


def generate_sequence(thing_name):
    print(f"Getting object segments {thing_name}")
    response = requests.get(f"{raspberry_pi_addr}:{object_service_port}/led-object/{thing_name}")
    segments_mapping = response.json()
    print()

    print(f"Building sequence for {trigger_name}")
    return build_baz(segments_mapping["segments"], duration)


def play_animation():
    print(f"Invoke {trigger_name}")
    print(requests.post(f"{raspberry_pi_addr}:{trigger_service_port}/trigger/{trigger_name}"))


def register_sequence():
    # seq_map = { thing_name: generate_sequence(thing_name) for thing_name in thing_names}
    thing_name = "spiral-small"
    seq = generate_sequence(thing_name)
    print("Storing sequence")
    print(requests.put(f"{raspberry_pi_addr}:{sequence_service_port}/triggers/{trigger_name}/objects/{thing_name}",
                       json=seq))
    thing_name = "spiral-big"
    seq = generate_sequence(thing_name)
    print("Storing sequence")
    print(requests.put(f"{raspberry_pi_addr}:{sequence_service_port}/triggers/{trigger_name}/objects/{thing_name}",
                       json=seq))
