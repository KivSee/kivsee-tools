
def as_alternate_1(elements):
    return [("peacock1", f"{e[1]}_a1") for e in elements]

def as_alternate_2(elements):
    return [("peacock1", f"{e[1]}_a2") for e in elements]

def as_symmetric(elements):
    return [("peacock1", f"{e[1]}_s") for e in elements]

def as_random(elements):
    return [("peacock1", f"{e[1]}_r") for e in elements]
