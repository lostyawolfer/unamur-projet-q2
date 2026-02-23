from copy import deepcopy # TODO: get rid of deepcopy
from .data import creatures as creature_dict
from .data import heroes as hero_dict
from .data import game_rules


_rules_initiated: bool = False


def create_game_rules(map_size: tuple[int, int], win_condition: int,
                      spawn_player_1: tuple[int, int], spawn_player_2: tuple[int, int],
                      spur: list[tuple[int, int]]):
    # TODO: write specs
    global _rules_initiated
    if _rules_initiated: raise Exception('rules have already been set up before')
    game_rules["map_size"] = map_size
    game_rules['turns_to_win'] = win_condition
    game_rules['spawn']['player_1'] = spawn_player_1
    game_rules['spawn']['player_2'] = spawn_player_2
    game_rules['spur'] = spur
    _rules_initiated = True


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
    if not 1 <= pos[0] <= game_rules["map_size"][0]: return False
    if not 1 <= pos[1] <= game_rules["map_size"][1]: return False
    return True


def get_entities_at(pos: tuple[int, int]) -> dict:
    """
    Gets all entities at the specified position.

    Parameters
    ----------
    pos: tuple[int, int] - position to check

    Returns
    -------
    dict - container of all entities that exist in that position.

    {
        "creatures": { (creature name): {(all creature info in a dict...)} },
        "heroes": {
            "player_1": { (hero name): {(all hero info in a dict...)} },
            "player_2": { (hero name): {(all hero info in a dict...)} }
        }
    }

    Raises
    ------
    ValueError: pos is outside the map - when the specified position is invalid

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    if not is_legal_position(pos): raise ValueError(f'{pos} is outside the map')
    res = {
        "creatures": {},
        "heroes": {
            "player_1": {},
            "player_2": {}
        }
    }

    for creature in creature_dict:
        if creature_dict[creature]["position"] == pos:
            res['creatures'][creature] = deepcopy(creature_dict[creature])

    for player in hero_dict:
        for hero in hero_dict[player]:
            if hero_dict[player][hero]['position'] == pos:
                res['heroes'][player][hero] = deepcopy(hero_dict[player][hero])

    return res


def get_all_entity_positions() -> dict:
    # TODO: write specs
    res = {
        "creatures": {},
        "heroes": {
            "player_1": {},
            "player_2": {}
        }
    }
    for creature in creature_dict:
        res['creatures'][creature] = creature_dict[creature]['position']

    for player in hero_dict:
        for hero in hero_dict[player]:
            res['heroes'][player][hero] = hero_dict[player][hero]['position']

    return res