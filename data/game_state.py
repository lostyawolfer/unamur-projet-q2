# TODO: make the dicts clean; add more helper functions to manipulate them

from classes import *

game_rules = {
    "map-size": (39, 40),
    "turns-to-win": 25,
    "spawn": [
        (20, 3),
        (20, 38)
    ],
    "spur": [
        (20, 38),
        (20, 39),
        (21, 38),
        (21, 39)
    ]
}

creatures = {
    "creatures": {
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
        },
    }
}

heroes = {
    "player-1": {
        "hero-1": {
            "name": "megacool character with nice backstory",
            "class": mage,
            "position": [15, 10],
            "health": 10,
            "damage": 3
        },
        "hero-2": {
            ...
        },
        "hero-3": ...,
        "hero-4": ...
    },

    "player-2": {
        "hero-1": ...,
        "hero-2": ...,
        "hero-3": ...,
        "hero-4": ...,
    }
}

def create_hero(player: str, name: str, cls: str):
    if len(heroes[player]) >= 4: raise
    if not class_exists(cls): raise ValueError(f"class {cls} doesn't exist")
    for char in name:
        if not char.isalpha(): raise ValueError("hero names can only contain letters")


def update_visuals():
    """Syncs the rendered visuals in terminal with the saved game state."""
    ...