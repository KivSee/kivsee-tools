val = {
        "numberOfPixels": 240,
        "segments": [{
            "name": "all",
            "pixels": [dict({"index": n}) for n in range(0, 240)]
        },
        {
            "name": "head",
            "pixels": [dict({"index": n}) for n in range(0, 10)]
        },
        {
            "name": "body",
            "pixels": [dict({"index": n}) for n in range(10, 20)]
        },
        {
            "name": "wing_l",
            "pixels": [dict({"index": n}) for n in range(20, 30)]
        },
        {
            "name": "wing_r",
            "pixels": [dict({"index": n}) for n in range(30, 40)]
        }
        ]
    }