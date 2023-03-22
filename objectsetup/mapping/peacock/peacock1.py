import random

from objectsetup.mapping.utils import get_alternate, get_random, segments_defs

total_pixels = 593

segments = [
    {
        "name": "body",
        "indices": range(0, 197),
    },
    {
        "name": "tail",
        "indices": range(197, 304),
    },
    {
        "name": "wing_r",
        "indices": range(304, 399)[::-1],
    },
    {
        "name": "head",
        "indices": range(399, 499),
    },
    {
        "name": "wing_l",
        "indices": range(499, 593),
    },
    {
        "name": "crown",
        "indices": range(436, 447),
    },
    {
        "name": "neck",
        "indices": list(range(399, 436)) + list(range(447, 499)),
    },
]

segments_config = [segments_defs(s) for s in segments]
[alternate1, alternate2] = get_alternate(range(0, total_pixels), "all", 4)
flatten = [item for sublist in segments_config for item in sublist]
flatten.extend([alternate1, alternate2])
flatten.append(get_random(range(0, total_pixels), "all"))

val = {
        "numberOfPixels": 593,
        "segments": flatten
    }
