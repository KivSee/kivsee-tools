import requests
import json
from dotenv import dotenv_values

config = dotenv_values("../.env")

raspberry_pi_addr = config["RASPBERRY_ADDR"]
object_service_port = config["OBJ_SERVICE_PORT"]
sequence_service_port = config["SEQ_SERVICE_PORT"]
trigger_service_port = config["TRIG_SERVICE_PORT"]


def const_color_effect(segment_name, start_time, end_time, hue):
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


def rainbow_effect(segment_name, start_time, end_time, function_start, function_end):
    return {
        "effect_config": {
            "start_time": start_time,
            "end_time": end_time,
            "segments": segment_name
        },
        "rainbow": {
            "hue_start": function_start,
            "hue_end": function_end
        }
    }


def hue_shift_effect(segment_name, start_time, end_time, function):
    return {
        "effect_config": {
            "start_time": start_time,
            "end_time": end_time,
            "segments": segment_name
        },
        "hue": {
            "offset_factor": function
        }
    }


def saturation_shift_effect(segment_name, start_time, end_time, function):
    return {
        "effect_config": {
            "start_time": start_time,
            "end_time": end_time,
            "segments": segment_name
        },
        "saturation": {
            "mult_factor": function
        }
    }


def brightness_effect(segment_name, start_time, end_time, function):
    return {
        "effect_config": {
            "start_time": start_time,
            "end_time": end_time,
            "segments": segment_name
        },
        "brightness": {
            "mult_factor": function
        }
    }


def linear_function(start, end):
    return {
        "linear": {
            "start": start,
            "end": end,
        }
    }


def const_function(val):
    return {
        "const_value": {
            "value": val,
        }
    }


def sin_function(min, max, phase, repeats):
    return {
        "sin": {
            "min": min,
            "max": max,
            "phase": phase,
            "repeats": repeats,
        }
    }


def steps_function(num_steps,
                   diff_per_step,
                   first_step_value):
    return {
        "steps": {
            "num_steps": num_steps,
            "diff_per_step": diff_per_step,
            "first_step_value": first_step_value,
        }
    }


def repeat_function(number_of_times, function):
    return {
        "repeat": {
            "numberOfTimes": number_of_times,
            "funcToRepeat": function,
        }
    }


def half_function(f1, f2):
    return {
        "half": {
            "f1": f1,
            "f2": f2,
        }
    }


def comb2_function(f1, amount1, f2, amount2):
    return {
        "comb2": {
            "f1": f1,
            "amount1": amount1,
            "f2": f2,
            "amount2": amount2,
        }
    }


def store_animation(trigger_name, thing_name, config, duration):
    sequence = build_effects_list(config["segments"], duration)
    res = requests.put(f"{raspberry_pi_addr}:{sequence_service_port}/triggers/{trigger_name}/objects/{thing_name}",
                       json=sequence)
    print(res)
    print("request sent")


def const_list(start, end, segments):
    return [const_color_effect(segment["name"], start, end, 0.4) for
            idx, segment in enumerate(segments)]


def hue_shift_list(start, end, segments):
    return [hue_shift_effect(segment["name"], start, end, comb2_function(sin_function(-1, 1, 0, 1.9), 0.7, sin_function(-1, 1, 0, 3), 0.3))  for
            idx, segment in
            enumerate(segments)]


def saturation_list(start, end, segments):
    return [saturation_shift_effect(segment["name"], start, end, const_function(0.5)) for
            idx, segment in
            enumerate(segments)]


def rainbow_list(start, end, segments):
    return [rainbow_effect(segment["name"], start, end, linear_function(0.3 * idx, 0.7 * idx), linear_function(0.8 * idx, 0.2 * idx)) for
            idx, segment in enumerate(segments)]


def brightness_list(start, end, segments):
    return [brightness_effect(segment["name"], start, end, comb2_function(sin_function(-1, 1, 0, 1.9), 0.7, sin_function(-1, 1, 0, 3), 0.3)) for
            idx, segment in
            enumerate(segments)]


def build_effects_list(segments, duration):
    const_color_effect_list = const_list(0, int(duration * 0.5), segments)
    hue_shift_effect_list = hue_shift_list(0, int(duration * 0.25), segments)
    saturation_shift_list = saturation_list(int(duration * 0.25), int(duration * 0.5), segments)
    rainbow2_color_effect_list = rainbow_list(int(duration * 0.1), int(duration * 0.9), segments)
    brightness_effect_list = brightness_list(int(duration * 0.1), int(duration * 0.9), segments)
    hue_shift2_effect_list = hue_shift_list(int(duration * 0.1), int(duration * 0.9), segments)
    rainbow_effect_list = rainbow_list(int(duration * 0.75), int(duration), segments)

    return {
        # const_color_effect_list + hue_shift_effect_list + saturation_shift_list +
        "effects": const_color_effect_list,
        "duration_ms": duration,
        "num_repeats": 0
    }


thing_name = "spiral-small"
trigger_name = "etta"
duration = 22000

response = requests.get(f"{raspberry_pi_addr}:{object_service_port}/led-object/{thing_name}")
segments_mapping = response.json()
store_animation(trigger_name, thing_name, segments_mapping, duration)
print(requests.post(f"{raspberry_pi_addr}:{trigger_service_port}/trigger/{trigger_name}"))
