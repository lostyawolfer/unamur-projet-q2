game_rules = {
    "map_size": (39, 40),
    "turns_to_win": 25,
    "spawn": {"player_1": (20, 3), "player_2": (20, 38)},
    "spur": ((20, 38), (20, 39), (21, 38), (21, 39))
}

creatures = {
    "bear": {
        "position": (10, 10),
        "health": 20,
        "damage": 5,
        "range": 3,
        "effects": ["stun"]
    },
    "wolf": {
        "position": (15, 10),
        "health": 10,
        "damage": 3,
        "range": 2,
        "effects": []
    }
}

heroes = {
    "player_1": {
        "hero_1": {
            "class": "mage",
            "prev_position": [14, 10],
            "position": [15, 10],
            "health": 10,
            "max_health": 10,
            "damage": 3,
            "level": 1,
            "effects": []
        },
        "hero_2": {
            ...
        },
        "turns_on_spur": 0
    },

    "player_2": {
        "hero_1": {
            ...
        },
        "turns_on_spur": 0
    }
}
