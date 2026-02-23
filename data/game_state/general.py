_rules_init: bool = False

game_rules = {
    "map_size": (0, 0),
    "turns_to_win": 0,
    "spawn": {
        "player_1": (0, 0),
        "player_2": (0, 0)
    },
    "spur": []
}


def create_game_rules(map_size: tuple[int, int], win_condition: int,
                      spawn_player_1: tuple[int, int], spawn_player_2: tuple[int, int],
                      spur: list[tuple[int, int]]):
    # TODO: write specs
    global _rules_init
    if _rules_init: raise Exception('Rules have already been set up before!')
    game_rules["map_size"] = map_size
    game_rules['turns_to_win'] = win_condition
    game_rules['spawn']['player_1'] = spawn_player_1
    game_rules['spawn']['player_2'] = spawn_player_2
    game_rules['spur'] = spur
    _rules_init = True


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