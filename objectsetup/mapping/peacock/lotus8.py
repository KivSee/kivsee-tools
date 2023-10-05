import random

from objectsetup.mapping.utils import get_alternate, get_random, segments_defs

total_pixels = 240

segments = [
    {
        "name": "all",
        "indices": range(0, total_pixels),
    }
]

segments_config = [segments_defs(s) for s in segments]
flatten = [item for sublist in segments_config for item in sublist]

val = {
        "numberOfPixels": total_pixels,
        "segments": flatten
    }
