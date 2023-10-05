import random

from objectsetup.mapping.utils import get_alternate, get_random, segments_defs

total_pixels = 590

segments = [
    {
        "name": "body",
        "indices": range(0, 197),
    },
    {
        "name": "tail",
        "indices": range(197, 301),
    },
    {
        "name": "wing_r",
        "indices": range(301, 396),
    },
    {
        "name": "head",
        "indices": range(396, 496),
    },
    {
        "name": "wing_l",
        "indices": range(496, 590),
    },
    {
        "name": "crown",
        "indices": range(433, 444),
    },
    {
        "name": "neck",
        "indices": list(range(399, 436)) + list(range(447, 499)),
    },
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
