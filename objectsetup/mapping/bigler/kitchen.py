from objectsetup.mapping.utils import linear_pos_pixels


val = {
        "numberOfPixels": 150,
        "segments": [{
            "name": "all",
            "pixels": linear_pos_pixels(range(0, 150))
        }
        ]
    }