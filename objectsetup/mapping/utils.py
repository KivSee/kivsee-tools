import random

def linear_pos_pixels(r):
    number_of_pixels = len(r)
    if number_of_pixels == 1:
        return [{"index": r[0], "relPos": 0.5}]
    else:
        return [dict({"index": p, "relPos": i / (number_of_pixels - 1)}) for i, p in enumerate(r)]

def get_alternate(r, name, alternate_spacing):
    linear_pos = linear_pos_pixels(r)
    return [
        {
            "name": f"{name}_a1",
            "pixels": [p for p in linear_pos if p["index"] % (alternate_spacing * 2) < alternate_spacing]
        },
                {
            "name": f"{name}_a2",
            "pixels": [p for p in linear_pos if p["index"] % (alternate_spacing * 2) >= alternate_spacing]
        }
    ]

def get_random(r, name):
    return {
        "name": name + "_r",
        "pixels": [{"index": i, "relPos": random.random()} for i in r]
    }

def segments_defs(segment_config):
    name = segment_config['name']
    indices = segment_config['indices']
    number_of_pixels = len(indices)
    indices_rel_pos = linear_pos_pixels(indices)

    normal = {
        "name": name,
        "pixels": indices_rel_pos
    }

    rand = get_random(indices, name)

    dotted = {
        "name": name + "_d",
        "pixels": [{"index": i, "relPos": i / (number_of_pixels - 1)} for i in indices[::5]]
    }

    [alternate1, alternate2] = get_alternate(indices, name, 4)

    symmetry = {
        "name": name + "_s",
        "pixels": [{"index": p["index"], "relPos": p["relPos"] * 2 if p["relPos"] < 0.5 else (1-p["relPos"]) * 2 } for p in indices_rel_pos]
    }

    return [normal, rand, dotted, alternate2, alternate1, symmetry]


