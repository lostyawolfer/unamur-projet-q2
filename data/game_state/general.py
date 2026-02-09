game_rules = {
    "map-size": (39, 40),
    "turns-to-win": 25,
    "spawn": {
        "player_1": (20, 3),
        "player_2": (20, 38)
    },
    "spur": [
        (20, 38),
        (20, 39),
        (21, 38),
        (21, 39)
    ]
}

def is_legal_position(pos: tuple[int, int]) -> bool:
    if not 1 <= pos[0] <= game_rules["map-size"][0]: return False
    if not 1 <= pos[1] <= game_rules["map-size"][1]: return False
    return True