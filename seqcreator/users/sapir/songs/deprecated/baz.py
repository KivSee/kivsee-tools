# from seqcreator.rendering.effects import (const_color, brightness, hue_shift, saturation, rainbow)
# from seqcreator.rendering.function import functions_store
# import requests
# import config
# from seqcreator.network import manager

# effects = []
# trigger_name = "baz"
# thing_names = ["spiral-small", "spiral-big"]
# duration = 22000


# def relative_duration(val=1.0):
#     return int(duration * val)

# def build_baz(segments, duration):
#     curr_start = 0
#     effects.extend(const_color.for_each(0, relative_duration(0.5), segments, 0.7))
#     effects.extend(hue_shift.for_each(0, relative_duration(0.25), segments))
#     # effects.extend(saturation.for_each(relative_duration(0.25), relative_duration(0.5), segments))
#     # effects.extend(rainbow.for_each(relative_duration(0.1), relative_duration(0.9), segments))
#     # effects.extend(brightness.for_time(relative_duration(0.1), relative_duration(0.9), segments))
#     # effects.extend(hue_shift.for_each(relative_duration(0.1), relative_duration(0.9), segments))
#     # effects.extend(rainbow.for_each(relative_duration(0.75), int(duration), segments))
#     # effects.append(brightness.brightness_effect("all", 0, duration, functions_store.const_function(0.5)))

#     # print(effects)
#     return {
#         # const_color_effect_list + hue_shift_effect_list + saturation_shift_list +
#         "effects": effects,
#         "duration_ms": duration,
#         "num_repeats": 0
#     }


# def mapping_sequence(duration, thing_name):
#     response = manager.get_segments(thing_name)
#     segments_mapping = response.json()
#     return build_baz(segments_mapping["segments"], duration)


# def build_and_store_sequence():
#     for thing_name in thing_names:
#         seq = mapping_sequence(duration, thing_name)
#         manager.store_sequence_thing(trigger_name, seq, thing_name)