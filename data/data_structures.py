# guys please look at the structures i wrote in creatures.py and heroes.py
# i really tried my best at fully showing the entire way the structures look like

game_rules = {
    "map-size": (39, 40),
    "turns-to-win": 25,
    "spawn": {"player_1": (20, 3), "player_2": (20, 38)},
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
            "prev_position": [14, 10],
            "position": [15, 10],
            "health": 10,
            "max_health":10,
            "damage": 3,
            "level":1
        },
        "hero_2": {
            ...
        },
        "turns_on_goal" : 0
    },

    "player_2": {
        "hero_1": {
            ...
        },
        "turns_on_goal" : 0
    }
}
