from objectsetup.mapping.utils import linear_pos_pixels


val = {
        "numberOfPixels": 240,
        "segments": [{
            "name": "all",
            "pixels": linear_pos_pixels(range(0, 240))
        },
        {
            "name": "bottom",
            "pixels": linear_pos_pixels(range(0, 34)) + linear_pos_pixels(range(204, 240))
        },
        {
            "name": "left",
            "pixels": linear_pos_pixels(range(34, 78))
        },
        {
            "name": "top",
            "pixels":linear_pos_pixels(range(78, 160))
        },
        {
            "name": "right",
            "pixels": linear_pos_pixels(range(160, 204))
        }
        ]
    }