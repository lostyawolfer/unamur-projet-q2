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
            "position": (**int, X**, **int, Y**),
            "turns_on_spur": **int**,
            "effects": **list[str]**
        },
        ... (4 heroes total)
    },
    "player_2": {
        ... (same thing)
    }
}
"""
from math import ceil
from copy import deepcopy

from pygments.formatters import get_formatter_for_filename

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
    'position': (0, 0),
    'turns_on_spur': 0,
    'effects': []
}


def create(player: str, name: str, hcls: str):
    """
    Creates a new hero owned by the specified player.
    All other stats are derived automatically from initial game rules and specified hero class.

    Parameters
    ----------
    player: str - player name (either 'player_1' or 'player_2')
    name: str - name of the new hero (must be unique across both players) (must only be lowercase letters)
    hcls: str - the class of the new player (either 'barbarian', 'healer', 'mage' or 'rogue')

    Raises
    ------
    ValueError: player already has 4 or more heroes - players mustn't have any more heros than 4
    ValueError: hero already exists - if a hero with the same name already exists in any of the players
    ValueError: hero names can only contain letters - if the name contains numbers, spaces or special characters
    ValueError: hero names are only lowercase - if the name contains uppercase letters
    ValueError: class doesn't exist - if specified hero class is invalid

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    if len(heroes[player]) >= 4: raise ValueError(f'player {player} already has 4 or more heroes')
    for pl in heroes:
        if name in heroes[pl]:
            raise ValueError(f'hero with this name already exists')
    if not name.isalpha(): raise ValueError("hero names can only contain letters")
    if not name.islower(): raise ValueError("hero names are only lowercase")
    if not class_exists(hcls): raise ValueError(f"class {hcls} doesn't exist")

    spawn_pos = game_rules['spawn'][player]

    new_hero = deepcopy(_HERO_TEMPLATE)
    new_hero['class'] = hcls
    new_hero['level'] = 1
    new_hero['max_health'] = hcls_stats[hcls]['health']
    new_hero['health'] = new_hero['max_health']
    new_hero['damage'] = hcls_stats[hcls]['damage']
    new_hero['position'] = spawn_pos

    heroes[player][name] = new_hero




# --------------------
# GETTERS
# --------------------


def get_player(hero: str) -> str | None:
    """
    Gets the player who owns the specified hero.

    Parameters
    ----------
    hero: str - name of the hero

    Returns
    -------
    !! either
    str - the player who owns the hero (either 'player_1' or 'player_2')
    None - if there isn't a single player who owns that hero

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    for player in heroes:
        if hero in heroes[player]:
            return player
    return None


def _verify_hero(hero: str, player: str = None) -> str:
    """
    INTERNAL FUNCTION THAT ISN'T SUPPOSED TO BE IMPORTED ANYWHERE,
    AND IS INSTEAD ONLY USED IN THIS FILE.

    Makes sure the hero's player is specified correctly,
    or gets the player that hero owns, while properly raising
    errors if such player or hero doesn't exist.

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    if not player:
        player = get_player(hero)
        if not player: raise ValueError(f'hero {hero} doesn\'t exist')
    if not player in heroes: raise ValueError(f'player {player} doesn\'t exist')
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't own a hero called {hero}")
    return player


def get_class(hero: str, player: str = None) -> str:
    """
    Gets the class of the specified hero.

    Parameters
    ----------
    hero: str - name of the hero
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Returns
    -------
    str - the class of the hero (either 'barbarian', 'healer', 'mage' or 'rogue')

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    return heroes[player][hero]['class']


def get_level(hero: str, player: str = None) -> int:
    """
    Gets the level of the specified hero.

    Parameters
    ----------
    hero: str - name of the hero
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Returns
    -------
    int - the level of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    return heroes[player][hero]['level']


def get_health(hero: str, player: str = None) -> int:
    """
    Gets the current health of the specified hero.

    Parameters
    ----------
    hero: str - name of the hero
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Returns
    -------
    int - the current health of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    return heroes[player][hero]['health']


def get_max_health(hero: str, player: str = None) -> int:
    """
    Gets the max health of the specified hero.

    Parameters
    ----------
    hero: str - name of the hero
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Returns
    -------
    int - the max health of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    return heroes[player][hero]['max_health']


def get_damage(hero: str, player: str = None) -> int:
    """
    Gets the melee damage stat of the specified hero.

    Parameters
    ----------
    hero: str - name of the hero
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Returns
    -------
    int - the melee damage of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    return heroes[player][hero]['damage']


def get_pos(hero: str, player: str = None) -> tuple[int, int]:
    """
    Gets the current position of the specified hero.

    Parameters
    ----------
    hero: str - name of the hero
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Returns
    -------
    tuple[int, int] - the position of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    return heroes[player][hero]['position']


def get_owned_abilities(hero: str, player: str = None) -> tuple:
    """
    Gets the list of abilities available to use by the hero.

    Parameters
    ----------
    hero: str - name of the hero
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Returns
    -------
    tuple (() OR tuple[str] OR tuple[str, str]) - list of available abilities for the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    hcls = get_class(hero, player=player)
    hlvl = get_level(hero, player=player)
    hcls_abilities = hcls_get_ab(hcls)
    if hlvl == 1:
        return ()
    elif hlvl == 2:
        return (hcls_abilities[0],)
    else:
        return hcls_abilities


def get_effects(hero: str, player: str = None) -> list[str]:
    """
    Gets the list of all effects that currently affect the hero.

    Returns
    -------
    list[str] - list of names of effects the hero has

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 20 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    return heroes[player][hero]['effects']


# --------------------
# MANIPULATORS
# --------------------


def move(hero: str, pos: tuple[int, int], player: str = None):
    """
    Moves the hero to the specified position.

    Parameters
    ----------
    hero: str - name of the hero
    pos: tuple[int, int] - the new position
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    ValueError: new position for hero is outside the map - if the new position is illegal

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    if not is_legal_position(pos): raise ValueError(f'new position for {hero} is outside the map')
    heroes[player][hero]['position'] = pos


def level_up(hero: str, player: str = None):
    """
    Levels up the hero.
    Leveling up upgrades your max health and melee damage,
    along with unlocking new abilities on levels 2 and 3.

    Parameters
    ----------
    hero: str - name of the hero
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    heroes[player][hero]['level'] += 1
    heroes[player][hero]['max_health'] = ceil(1.4 * heroes[player][hero]['max_health'])
    heroes[player][hero]['damage'] = ceil(1.6 * heroes[player][hero]['damage'])


def respawn(hero: str, player: str = None):
    """
    Moves the hero back to their spawn spot, and resets their health.
    To be used for respawning a dead hero after death.

    Parameters
    ----------
    hero: str - name of the hero
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    spawn_pos = game_rules['spawn'][player]
    heroes[player][hero]['position'] = spawn_pos
    heroes[player][hero]['health'] = heroes[player][hero]['max_health']


def _die(hero: str, player: str = None):
    """
    INTERNAL FUNCTION THAT ISN'T SUPPOSED TO BE IMPORTED ANYWHERE,
    AND IS INSTEAD ONLY USED IN THIS FILE.

    Processes the hero's death, if upon hurting it its health becomes 0.
    Currently, literally does nothing.

    !!! Might not be needed or become an importable function
    !!! in the future, since it's supposed to only be cleaned up
    !!! in a different phase after damage is inflicted, not immediately.

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    ...


def hurt(hero: str, amount: int, player: str = None) -> int:
    """
    Damages the hero by a specified amount.

    Parameters
    ----------
    hero: str - name of the hero
    amount: int - the amount of damage to deal to the named hero (must be positive or 0)
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    ValueError: cannot inflict negative damage - if amount is negative

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    if amount < 0: raise ValueError('cannot inflict negative damage')
    new_health = max(0, heroes[player][hero]['health'] - amount)
    heroes[player][hero]['health'] = new_health
    if new_health <= 0:
        _die(hero, player=player)
    return new_health


def heal(hero: str, amount: int, player: str = None) -> int:
    """
    Heals the hero by a specified amount. Caps at the hero's max_health.

    Parameters
    ----------
    hero: str - name of the hero
    amount: int - the amount of healing to do to the named hero (must be positive or 0)
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    ValueError: cannot inflict negative healing - if amount is negative

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 19 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    if amount < 0: raise ValueError('cannot inflict negative healing')
    max_health = heroes[player][hero]['max_health']
    new_health = min(heroes[player][hero]['health'] + amount, max_health)
    heroes[player][hero]['health'] = new_health
    return new_health


def apply_effect(hero: str, effect_name: str, player: str = None) -> list[str]:
    """
    Adds the specified effect to the effect list of the hero.

    Parameters
    ----------
    hero: str - name of the hero
    effect_name: str - name of the effect to apply
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 20 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    heroes[player][hero]['effects'] += effect_name
    return heroes[player][hero]['effects']


def reset_effects(hero: str, player: str = None):
    """
    Resets the effect list of the hero.

    Parameters
    ----------
    hero: str - name of the hero
    player: str = None - name of the player that owns the hero
        (if None, finds the owning player automatically;
        if str, only works if specified hero is owned by the player)

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found

    Version
    -------
    specification: VOLKOV Kostiantyn (v. 1, 20 fév. 2026)
    """
    player = _verify_hero(hero, player=player)
    heroes[player][hero]['effects'] = []