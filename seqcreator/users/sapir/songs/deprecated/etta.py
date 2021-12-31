# import requests
# from rendering.effects import (rainbow, brightness, hue_shift)
# from rendering.function import functions_store
# import config
# from network import manager
#
# trigger_name = "etta"
# effectsList = []
# offset = 55
#
# def mapping_sequence(duration):
#     effectsList.append(rainbow.rainbow_effect("outline", 467, duration, functions_store.linear_function(0.5, 0.6),
#                                               functions_store.linear_function(0.6, 0.5)))
#     effectsList.append(hue_shift.hue_shift_effect("all", 0, duration,
#                                                   functions_store.sin_function(-1, 1, 0, 2)))
#     effectsList.append(rainbow.rainbow_effect("spiral1", 4071, duration, functions_store.linear_function(0.3, 0.7),
#                                               functions_store.linear_function(0.8, 0.2)))
#     effectsList.append(rainbow.rainbow_effect("spiral2", 10935, duration, functions_store.linear_function(0.3, 0.7),
#                                               functions_store.linear_function(0.8, 0.2)))
#     # effectsList.append(brightness.brightness_effect("all", 0, duration,
#     #                                                 functions_store.repeat_function(153, functions_store.linear_function(0.3,
#     #                                                                                                                0.6))))
#
#     return {
#         "effects": effectsList,
#         "duration_ms": duration,
#         "num_repeats": 0
#     }
#
# thing_names = ["spiral-small", "spiral-big"]
#
# def build_and_store_sequence():
#     duration = 180000
#     seq = mapping_sequence(duration)
#     manager.store_sequence_all(trigger_name, seq, thing_names)