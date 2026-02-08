from .creatures import creatures as creature_dict
from .heroes import heroes as hero_dict

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

def get_entities_at(pos: tuple[int, int]) -> dict:
    if not is_legal_position(pos): raise ValueError(f'{pos} is outside of the map!')
    res = {
        "creatures": {},
        "heroes": {
            "player-1": {},
            "player-2": {}
        }
    }

    for creature in creature_dict:
        if creature_dict[creature]["position"] == pos:
            res['creatures'][creature] = creature_dict[creature]

    for player in hero_dict:
        for hero in hero_dict[player]:
            if hero_dict[player][hero]['position'] == pos:
                res['heroes'][player][hero] = hero_dict[player][hero]

    return res

def get_all_entity_positions() -> dict:
    ...

def update_visuals():
    """Syncs the rendered visuals in terminal with the saved game state."""
    ...