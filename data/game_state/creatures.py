"""
!! DATA STRUCTURE !!
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



import inspect
from functools import wraps
def _creature_exists(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        name = bound_args.arguments.get("name")
        if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
        return func(*args, **kwargs)
    return wrapper


@_creature_exists
def _kill_creature(name: str):
    creatures.pop(name)


@_creature_exists
def get_creature_health(name: str) -> int:
    return creatures[name]["health"]


@_creature_exists
def update_creature_health(name: str, update: int) -> int | None:
    creatures[name]["health"] += update
    if get_creature_health(name) <= 0:
        _kill_creature(name)
        return None
    return creatures[name]["health"]


@_creature_exists
def get_creature_pos(name: str) -> tuple[int, int]:
    return creatures[name]["position"]