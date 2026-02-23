"""
|| DATA STRUCTURE ||
--------------------
creatures = {
    "**creature name**": {
        "position": (**int, X**, **int, Y**)
        "health": **int, health**,
        "damage": **int, physical damage**,
        "range": **int, creature's range**,
        "effects" **list[str]**
    },
    ... (for all creatures)
}
"""


from .general import is_legal_position
from .data import creatures


def create(name: str, pos: tuple[int, int], health: int, damage: int, attack_range: int):
    """
    Creates a new creature with specified data.

    Parameters
    ----------
    name: str - name of the new creature (must be unique)
    pos: tuple[int, int] - initial position
    health: int - initial health
    damage: int - initial melee damage
    attack_range: int - initial attack range

    Raises
    ------
    ValueError: such creature already exists - if creature name is already used
    ValueError: position is outside the map - if parameter pos used illegal coordinates

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    if name in creatures: raise ValueError('such creature already exists')
    if not is_legal_position(pos): raise ValueError(f'position {pos} is outside the map')
    new_creature = {
        "position": pos,
        "health": health,
        "damage": damage,
        "range": attack_range,
        "effects": []
    }
    creatures[name] = new_creature



# --------------------
# GETTERS
# --------------------


def get_health(name: str) -> int:
    """
    Gets the current health of the specified creature.

    Parameters
    ----------
    name: str - name of the creature

    Returns
    -------
    int - current health of specified creature

    Raises
    ------
    ValueError: creature doesn't exist - if the creature name is invalid

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    return creatures[name]["health"]


def get_pos(name: str) -> tuple[int, int]:
    """
    Gets the current position of the specified creature.

    Parameters
    ----------
    name: str - name of the creature

    Returns
    -------
    tuple[int, int] - current position of specified creature

    Raises
    ------
    ValueError: creature doesn't exist - if the creature name is invalid

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    return creatures[name]["position"]


def get_damage(name: str) -> int:
    """
    Gets the melee damage stat of the specified creature.

    Parameters
    ----------
    name: str - name of the creature

    Returns
    -------
    int - the melee damage stat of the specified creature

    Raises
    ------
    ValueError: creature doesn't exist - if the creature name is invalid

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    return creatures[name]["damage"]


def get_range(name: str) -> int:
    """
    Gets the attack range of the specified creature.

    Parameters
    ----------
    name: str - name of the creature

    Returns
    -------
    int - attack range of specified creature

    Raises
    ------
    ValueError: creature doesn't exist - if the creature name is invalid

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    return creatures[name]["range"]


def get_effects(name: str) -> list[str]:
    """
    Gets the list of effects currently affecting the creature.

    Parameters
    ----------
    name: str - name of the creature

    Returns
    -------
    list[str] - list of all effects affecting the creature

    Raises
    ------
    ValueError: creature doesn't exist - if the creature name is invalid

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 20 fév. 2026)
    """
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    return creatures[name]['effects']



# --------------------
# MANIPULATORS
# --------------------


def hurt(name: str, amount: int) -> int:
    """
    Damages the creature by a specified amount.

    Parameters
    ----------
    name: str - name of the creature
    amount: int - the amount of damage to deal to named creature (must be positive or 0)

    Returns
    -------
    int - new health of the creature after it took damage

    Raises
    ------
    ValueError: creature doesn't exist - if the creature name is invalid
    ValueError: cannot inflict negative damage - if amount is negative

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    if amount < 0: raise ValueError('cannot inflict negative damage')
    new_health = max(0, creatures[name]['health'] - amount)
    creatures[name]['health'] = new_health
    return new_health


def apply_effect(name: str, effect_name: str) -> list[str]:
    """
    Adds the specified effect to the effect list of the creature.

    Parameters
    ----------
    name: str - name of the creature
    effect_name: str - name of the effect to apply

    Raises
    ------
    ValueError: creature doesn't exist - if creature name is invalid
    ValueError: creature already has effect

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 2, 23 fév. 2026)
    """
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    if effect_name in creatures[name]['effects']: raise ValueError(f"creature {name} already has {effect_name}")
    creatures[name]['effects'].append(effect_name)
    return creatures[name]['effects']


def remove_effect(name: str, effect_name: str) -> list[str]:
    # TODO: write specs
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")

    effects = creatures[name]['effects']
    if effect_name not in effects: raise ValueError(f"creature {name} doesn't have {effect_name}")

    creatures[name]['effects'] = [eff for eff in effects if eff != effect_name]
    return creatures[name]['effects']


def reset_effects(name: str):
    """
    Resets the effect list of the creature.

    Parameters
    ----------
    name: str - name of the creature

    Raises
    ------
    ValueError: creature doesn't exist - if creature name is invalid

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 2, 20 fév. 2026)
    """
    if name not in creatures: raise ValueError(f"creature {name} doesn't exist")
    creatures[name]['effects'] = []