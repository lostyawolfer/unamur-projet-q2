# TODO: make a function that deduces who owns a hero with an arbitrary name if one exists
# TODO: make all functions not require player name (since all heroes names are unique in the entire game)
#       ^ it can be specified though, if the player is known
# TODO: make docs

"""
|| DATA STRUCTURE ||
--------------------
heroes = {
    "player_1": {
        "**hero name**": {
            "class": **str: "barbarian", "healer", "mage" or "rogue"**,
            "level": **int, level number**,
            "max_health": **int, max health**,
            "health": **int, health**,
            "damage": **int, physical damage**,
            "position": (**int, X**, **int, Y**)
        },
        ... (4 heroes total)
    },
    "player_2": {
        ... (same thing)
    }
}
"""
from math import floor
from .hero_classes import stats as hcls_stats, get_abilities as hcls_get_ab
from .hero_classes import class_exists
from .general import game_rules, is_legal_position


heroes = {
    'player_1': {},
    'player_2': {}
}

_HERO_TEMPLATE = {
    'class': '',
    'level': 0,
    'max_health': 0,
    'health': 0,
    'damage': 0,
    'position': (0, 0)
}


def create(player: str, name: str, hcls: str):
    if len(heroes[player]) >= 4: raise ValueError(f'player {player} already has 4 or more heroes')
    for pl in heroes:
        if name in heroes[pl]:
            raise ValueError(f'hero with this name already exists')
    for char in name:
        if not char.isalpha(): raise ValueError("hero names can only contain letters")
        if not char.islower(): raise ValueError("hero names are only lowercase")
    if not class_exists(hcls): raise ValueError(f"class {hcls} doesn't exist")

    spawn_pos = game_rules['spawn'][player]

    new_hero = _HERO_TEMPLATE.copy()
    new_hero['class'] = hcls
    new_hero['level'] = 1
    new_hero['max_health'] = hcls_stats[hcls]['health']
    new_hero['health'] = new_hero['max_health']
    new_hero['damage'] = hcls_stats[hcls]['damage']
    new_hero['position'] = spawn_pos

    heroes[player][name] = new_hero


import inspect
from functools import wraps
def _exists(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        hero = bound_args.arguments.get("hero")
        player = bound_args.arguments.get("player")
        if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
        return func(*args, **kwargs)
    return wrapper




# --------------------
# GETTERS
# --------------------


@_exists
def get_class(player: str, hero: str) -> str:
    return heroes[player][hero]['class']


@_exists
def get_level(player: str, hero: str) -> str:
    return heroes[player][hero]['level']


@_exists
def get_health(player: str, hero: str) -> int:
    return heroes[player][hero]['health']


@_exists
def get_max_health(player: str, hero: str) -> int:
    return heroes[player][hero]['max_health']


@_exists
def get_damage(player: str, hero: str) -> int:
    return heroes[player][hero]['damage']


@_exists
def get_pos(player: str, hero: str) -> tuple[int, int]:
    return heroes[player][hero]['pos']


@_exists
def get_owned_abilities(player: str, hero: str) -> tuple:
    hcls = get_class(player, hero)
    hlvl = get_level(player, hero)
    hcls_abilities = hcls_get_ab(hcls)
    if hlvl == 1:
        return ()
    elif hlvl == 2:
        return (hcls_abilities[0],)
    else:
        return hcls_abilities




# --------------------
# MANIPULATORS
# --------------------


@_exists
def _move(player: str, hero: str, pos: tuple[int, int]):
    if not is_legal_position(pos): raise ValueError(f'new position for {hero} is outside the map')
    heroes[player][hero]['position'] = pos


@_exists
def relative_move(player: str, hero: str, *, x: int = 0, y: int = 0) -> tuple[int, int]:
    current_pos = heroes[player][hero]['position']
    new_pos = (current_pos[0] + x, current_pos[1] + y)
    _move(player, hero, new_pos)
    return new_pos


@_exists
def level_up(player: str, hero: str):
    heroes[player][hero]['level'] += 1
    heroes[player][hero]['max_health'] = floor(1.4 * heroes[player][hero]['max_health'])
    heroes[player][hero]['damage'] = floor(1.6 * heroes[player][hero]['damage'])


@_exists
def respawn(player: str, hero: str):
    spawn_pos = game_rules['spawn'][player]
    heroes[player][hero]['position'] = spawn_pos
    heroes[player][hero]['health'] = heroes[player][hero]['max_health']


@_exists
def _die(player: str, hero: str):
    ...


@_exists
def hurt(player: str, hero: str, amount: int) -> int:
    if amount < 0: raise ValueError('cannot inflict negative damage')
    new_health = max(0, heroes[player][hero]['health'] - amount)
    heroes[player][hero]['health'] = new_health
    if new_health <= 0:
        _die(player, hero)
    return new_health


@_exists
def heal(player: str, hero: str, amount: int) -> int:
    if amount < 0: raise ValueError('cannot inflict negative healing')
    max_health = heroes[player][hero]['max_health']
    new_health = min(heroes[player][hero]['health'] + amount, max_health)
    heroes[player][hero]['health'] = new_health
    return new_health