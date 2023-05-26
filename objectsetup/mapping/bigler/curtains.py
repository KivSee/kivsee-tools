from objectsetup.mapping.utils import linear_pos_pixels


val = {
        "numberOfPixels": 240,
        "segments": [{
            "name": "all",
            "pixels": linear_pos_pixels(range(0, 240))
        }
        ]
    }