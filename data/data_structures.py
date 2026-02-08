game_rules = {
    "map-size": (39, 40),
    "turns-to-win": 25,
    "spawn": ((20, 3), (20, 38)),                        # First tuple = Spawn of Player 1, Second tuple = Spawn of Player 2.
    "spur": ((20, 38), (20, 39), (21, 38), (21, 39))
}

creatures = {
    "bear": {
        "position": (10, 10),
        "health": 20,
        "damage": 5,
        "range": 3
    },
    "wolf": {
        "position": (15, 10),
        "health": 10,
        "damage": 3,
        "range": 2
    }
}

heroes = {
    "player_1": {
        "hero_1": {
            "class": "mage",
            "position": [15, 10],
            "health": 10,
            "max_health":10,
            "damage": 3,
            "level":1
        },
        "hero_2": {
            ...
        },
    },

    "player_2": {
        "hero_1": {
            ...
        },
    }
}
