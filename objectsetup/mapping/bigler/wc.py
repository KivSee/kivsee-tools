from objectsetup.mapping.utils import linear_pos_pixels


val = {
        "numberOfPixels": 80,
        "segments": [{
            "name": "w",
            "pixels": linear_pos_pixels(range(0, 31))
        },
        {
            "name": "c",
            "pixels": linear_pos_pixels(range(31, 46))
        },
        {
            "name": "man",
            "pixels": linear_pos_pixels(range(46, 63))
        },
        {
            "name": "woman",
            "pixels": linear_pos_pixels(range(63, 80))
        }
        ]
    }