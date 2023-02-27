import random

wing_l = list(range(0, 115))
wing_l_r = wing_l.copy()
random.shuffle(wing_l_r)

def swap(l, i1, i2):
    t = l[i1]
    l[i1] = l[i2]
    l[i2] = t

wing_l_a1 = []
for i in range(0, len(wing_l), 10):
    if i < len(wing_l):
        wing_l_a1.append(i)
    if i + 1 < len(wing_l):
        wing_l_a1.append(i + 1)
    if i + 2 < len(wing_l):
        wing_l_a1.append(i + 2)
    if i + 3 < len(wing_l):
        wing_l_a1.append(i + 3)
    if i + 4 < len(wing_l):
        wing_l_a1.append(i + 4)

wing_l_a2 = []
for i in range(0, len(wing_l), 10):
    if i + 5 < len(wing_l):
        wing_l_a2.append(i + 5)
    if i + 6 < len(wing_l):
        wing_l_a2.append(i + 6)
    if i + 7 < len(wing_l):
        wing_l_a2.append(i + 7)
    if i + 8 < len(wing_l):
        wing_l_a2.append(i + 8)
    if i + 9 < len(wing_l):
        wing_l_a2.append(i + 9)

wing_l_d = wing_l[0::5]

wing_l_s = []
for i in range(0, int(len(wing_l) / 2)):
    wing_l_s.append(i)
    wing_l_s.append(len(wing_l) - 1 - i)
if len(wing_l) % 2 == 1:
    wing_l_s.append(int(len(wing_l) / 2))

val = {
        "numberOfPixels": 740,
        "segments": [{
        #     "name": "all",
        #     "pixels": [dict({"index": n}) for n in range(0, 720)]
        # },
        # {
            "name": "head",
            "pixels": [dict({"index": n}) for n in range(158, 295)]
        },
        {
            "name": "body",
            "pixels": [dict({"index": n}) for n in list(range(305, 385)) + list(range(550, 650))]
        },
        {
            "name": "wing_l",
            "pixels": [dict({"index": n}) for n in range(0, 115)]
        },
        {
            "name": "wing_l_r",
            "pixels": [dict({"index": n}) for n in wing_l_r]
        },
        {
            "name": "wing_l_a1",
            "pixels": [dict({"index": n}) for n in wing_l_a1]
        },
        {
            "name": "wing_l_a2",
            "pixels": [dict({"index": n}) for n in wing_l_a2]
        },
        {
            "name": "wing_l_d",
            "pixels": [dict({"index": n}) for n in wing_l_d]
        },
        {
            "name": "wing_l_s",
            "pixels": [dict({"index": n}) for n in wing_l_s]
        },
        {
            "name": "tail",
            "pixels": [dict({"index": n}) for n in range(400, 530)]
        },
        # {
        #     "name": "wing_r",
        #     "pixels": [dict({"index": n}) for n in range(0, 0)]
        # }
        ]
    }