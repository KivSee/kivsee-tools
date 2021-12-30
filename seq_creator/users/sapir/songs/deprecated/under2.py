# import requests
# import config
# from infra import timing
# from infra.animations_factory import coloring_effect, masking_effect, get_effects_list, get_elements
# from network import manager
#
# trigger_name = "under"
#
# elements = get_elements()
#
# thing_names = ["spiral-small", "spiral-big"]
#
# note_to_elem1 = {
#     "D": "spiral1",
#     "Bb": "spiral2",
#     "F": "spiral3",
#     "C": "subout1",
#     "Eb": "subout2",
#     "A": "subout3",
# }
#
# note_to_elem2 = {
#     "D": "subout4",
#     "Bb": "subout5",
#     "F": "subout6",
#     "C": "subout7",
#     "G": "subout8",
#     "A": "subout9",
# }
#
# notes = ["A", "C", "D", "F", "Bb", "Eb"]
#
# note_to_color = {
#     "A": (0.0, 1.0, 1.0),
#     "C": (0.15, 1.0, 1.0),
#     "D": (0.3, 1.0, 1.0),
#     "F": (0.5, 1.0, 1.0),
#     "Bb": (0.7, 1.0, 1.0),
#     "Eb": (0.85, 1.0, 1.0),
# }
#
# def mapping_sequence(duration):
#     timing.song_settings(bpm=128, beats_per_episode=32, start_offset=0)
#     timing.beats(2, 20)
#
#     # make uniform coloring
#     for note in notes:
#         elements = [note_to_elem1[note]]
#         c = note_to_color[note]
#         coloring_effect.uniform([c[0], 0.4, 0.5])
#
#     return {
#         "effects": get_effects_list(),
#         "duration_ms": duration,
#         "num_repeats": 0
#     }
#
# def build_and_store_sequence():
#     duration = 147000
#     seq = mapping_sequence(duration)
#     manager.store_sequence_all(trigger_name, seq, thing_names)
