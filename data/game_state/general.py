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
    """
    Checks if the specified position exists within confines of the map.

    Parameters
    ----------
    pos: tuple[int, int] - position to check

    Returns
    -------
    bool - True if position is within the map, False otherwise

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    if not 1 <= pos[0] <= game_rules["map-size"][0]: return False
    if not 1 <= pos[1] <= game_rules["map-size"][1]: return False
    return True