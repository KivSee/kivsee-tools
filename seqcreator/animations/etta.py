import requests
import effects as effects_factory
import functions as func_factory
import config

trigger_name = "etta"

def const_seq(duration):
    return {
        "effect_config": {
            "start_time": 0,
            "end_time": duration,
            "segments": "all"
        },
        "const_color": {
            "color": {
                "hue": 0.5,
                "sat": 1.0,
                "val": 0.3
            }
        }
    }
effects = []
def mapping_sequence(duration):
    effects.append(effects_factory.const_color_effect("all", 0, duration, 0.5))
    effects.append(effects_factory.brightness_effect("all", 0, duration,
                                      func_factory.repeat_function(153, func_factory.linear_function(0, 1))))
    return {
        "effects": effects,
        "duration_ms": duration,
        "num_repeats": 0
    }

def register_sequence():
    duration = 180000
    thing_name = "spiral-small"
    # seq_map = { thing_name: generate_sequence(thing_name) for thing_name in thing_names}
    seq = mapping_sequence(duration)
    print(f"Storing sequence for thing: {thing_name}")
    response = requests.put(f"{config.raspberry_pi_addr}:{config.sequence_service_port}/triggers/{trigger_name}/objects/{thing_name}",
                       json=seq)
    print(response.content)
    thing_name = "spiral-big"
    seq = mapping_sequence(duration)
    print(f"Storing sequence for thing: {thing_name}")
    response = requests.put(f"{config.raspberry_pi_addr}:{config.sequence_service_port}/triggers/{trigger_name}/objects/{thing_name}",
                       json=seq)
    print(response.content)

# milisec = 5882
# repeat_function
# brightness (repeat)


