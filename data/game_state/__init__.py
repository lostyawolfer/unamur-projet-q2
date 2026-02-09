from . import creatures
from . import heroes
from . import hero_classes
from .creatures import creatures as creature_dict
from .heroes import heroes as hero_dict
from .general import *


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
    ValueError: pos is outside the map - when the specified position is not valid
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
            res['creatures'][creature] = creature_dict[creature].copy()

    for player in hero_dict:
        for hero in hero_dict[player]:
            if hero_dict[player][hero]['position'] == pos:
                res['heroes'][player][hero] = hero_dict[player][hero].copy()

    return res


def get_all_entity_positions() -> dict:
    ...


def update_visuals():
    """Syncs the rendered visuals in terminal with the saved game state."""
    ...