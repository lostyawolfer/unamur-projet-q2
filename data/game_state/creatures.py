# TODO: make docs

"""
|| DATA STRUCTURE ||
--------------------
creatures = {
    "**creature name**": {
        "position": (**int, X**, **int, Y**)
        "health": **int, health**,
        "damage": **int, physical damage**,
        "range": **int, creature's range**
    },
    ... (for all creatures)
}
"""

creatures = {}


def create(name: str, pos: tuple[int, int], health: int, damage: int, attack_range: int):
    if name in creatures: raise ValueError('such creature already exists')
    new_creature = {
        "position": pos,
        "health": health,
        "damage": damage,
        "range": attack_range
    }
    creatures[name] = new_creature



# --------------------
# GETTERS
# --------------------


def get_all_creatures() -> list[str]:
    creature_list = []
    for creature in creatures:
        creature_list.append(creature)
    return creature_list


def get_health(name: str) -> int:
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    return creatures[name]["health"]


def get_pos(name: str) -> tuple[int, int]:
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    return creatures[name]["position"]


def get_damage(name: str) -> tuple[int, int]:
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    return creatures[name]["damage"]


def get_range(name: str) -> tuple[int, int]:
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    return creatures[name]["damage"]




# --------------------
# MANIPULATORS
# --------------------


def _die(name: str):
    creatures.pop(name)


def hurt(name: str, amount: int) -> int | None:
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    if amount < 0: raise ValueError('cannot inflict negative damage')
    new_health = max(0, creatures[name]['health'] - amount)
    creatures[name]['health'] = new_health
    if new_health <= 0:
        _die(name)
    return creatures[name]["health"]