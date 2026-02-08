from .classes import *

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


# --------------
# creatures
# --------------


creatures = {}

def get_all_creatures() -> list[str]:
    creature_list = []
    for creature in creatures:
        creature_list.append(creature)
    return creature_list

def create_creature(name: str, position: tuple[int, int], health: int, damage: int, attack_range: int):
    if name in creatures: raise ValueError('such creature already exists')
    new_creature = {
        "position": position,
        "health": health,
        "damage": damage,
        "range": attack_range
    }
    creatures[name] = new_creature

def _kill_creature(name: str):
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    creatures.pop(name)

def get_creature_health(name: str) -> int:
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    return creatures[name]["health"]

def update_creature_health(name: str, update: int) -> int | None:
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    creatures[name]["health"] += update
    if get_creature_health(name) <= 0:
        _kill_creature(name)
        return None
    return creatures[name]["health"]


def get_creature_pos(name: str) -> tuple[int, int]:
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    return creatures[name]["position"]




heroes = {
    "player-1": {
        "hero-1": {
            "name": "megacool character with nice backstory",
            "class": mage,
            "position": [15, 10],
            "health": 10,
            "max-health": 10,
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


def get_raw_board_data():
    """ Get the initial raw board data from the .lon file.

    Version:
    --------
    Romain Pezzutto (v.1 08/02/2026)
    """

    f = open("board.lon", "r")
    board_file = f.readlines()
    f.close()

    raw_data = []
    section_name = ""
    section_data = []

    for line in board_file:
        if line[-2] == ":":
            raw_data.append([section_name, section_data])
            section_name = line[:-2]
            section_data = []
        else:
            section_data.append(line[:-1])

    raw_data.append([section_name, section_data])
    raw_data.pop(0)

    return raw_data


def get_game_rules(raw_data):
    """ Get the game rules from the raw data of the .lon file.

    Parameters:
    -----------
    raw_data: Raw data retrieved from the .lon file. (list)

    """

    pass


def update_visuals():
    """Syncs the rendered visuals in terminal with the saved game state."""
    ...



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
    for creature in creatures:
        if creatures[creature]["position"] == pos:
            res['creatures'][creature] = creatures[creature]
    for player in heroes:
        for hero in heroes[player]:
            if heroes[player][hero]['position'] == pos:
                res['heroes'][player][hero] = heroes[player][hero]
    return res

def get_all_entity_positions() -> dict:
    ...