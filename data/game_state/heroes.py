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
    """
    if len(heroes[player]) >= 4: raise ValueError(f'player {player} already has 4 or more heroes')
    for pl in heroes:
        if name in heroes[pl]:
            raise ValueError(f'hero with this name already exists')
    if not name.isalpha(): raise ValueError("hero names can only contain letters")
    if not name.islower(): raise ValueError("hero names are only lowercase")
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




# --------------------
# GETTERS
# --------------------


# TODO: make a function that deduces who owns a hero with an arbitrary name if one exists
# TODO: make all functions not require player name (since all heroes names are unique in the entire game)
#       ^ it can be specified though, if the player is known
#       (because otherwise all these getter functions are low-key useless)


def get_class(player: str, hero: str) -> str:
    """
    Gets the class of the specified hero.

    Parameters
    ----------
    player: str - name of the player that owns the hero (either 'player_1' or 'player_2')
    hero: str - name of the hero

    Returns
    -------
    str - the class of the hero (either 'barbarian', 'healer', 'mage' or 'rogue')

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
    return heroes[player][hero]['class']


def get_level(player: str, hero: str) -> int:
    """
    Gets the level of the specified hero.

    Parameters
    ----------
    player: str - name of the player that owns the hero (either 'player_1' or 'player_2')
    hero: str - name of the hero

    Returns
    -------
    int - the level of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
    return heroes[player][hero]['level']


def get_health(player: str, hero: str) -> int:
    """
    Gets the current health of the specified hero.

    Parameters
    ----------
    player: str - name of the player that owns the hero (either 'player_1' or 'player_2')
    hero: str - name of the hero

    Returns
    -------
    int - the current health of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
    return heroes[player][hero]['health']


def get_max_health(player: str, hero: str) -> int:
    """
    Gets the max health of the specified hero.

    Parameters
    ----------
    player: str - name of the player that owns the hero (either 'player_1' or 'player_2')
    hero: str - name of the hero

    Returns
    -------
    int - the max health of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
    return heroes[player][hero]['max_health']


def get_damage(player: str, hero: str) -> int:
    """
    Gets the melee damage stat of the specified hero.

    Parameters
    ----------
    player: str - name of the player that owns the hero (either 'player_1' or 'player_2')
    hero: str - name of the hero

    Returns
    -------
    int - the melee damage of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
    return heroes[player][hero]['damage']


def get_pos(player: str, hero: str) -> tuple[int, int]:
    """
    Gets the current position of the specified hero.

    Parameters
    ----------
    player: str - name of the player that owns the hero (either 'player_1' or 'player_2')
    hero: str - name of the hero

    Returns
    -------
    tuple[int, int] - the position of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
    return heroes[player][hero]['position']


def get_owned_abilities(player: str, hero: str) -> tuple:
    """
    Gets the list of abilities available to use by the hero.

    Parameters
    ----------
    player: str - name of the player that owns the hero (either 'player_1' or 'player_2')
    hero: str - name of the hero

    Returns
    -------
    tuple (empty tuple OR tuple[str] OR tuple[str, str]) - list of available abilities for the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
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


# TODO: make _move a proper function, and create a new coordinate delta checker
#       to help check "how much x and y has the player moved?"
#       All of this is supposed to replace relative_move to make things easier

def _move(player: str, hero: str, pos: tuple[int, int]):
    """
    INTERNAL FUNCTION THAT ISN'T SUPPOSED TO BE IMPORTED ANYWHERE,
    AND IS INSTEAD ONLY USED IN THIS FILE.

    Moves the hero to the specified position.
    Raises if hero doesn't exist or if the new position is invalid.
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
    if not is_legal_position(pos): raise ValueError(f'new position for {hero} is outside the map')
    heroes[player][hero]['position'] = pos


def relative_move(player: str, hero: str, *, x: int = 0, y: int = 0) -> tuple[int, int]:
    """
    Moves the hero relatively to their absolute coordinates.

    Parameters
    ----------
    player: str - name of the player that owns the hero (either 'player_1' or 'player_2')
    hero: str - name of the hero
    *** KEYWORD-ONLY ARGUMENTS BELOW - they can only be specified with keywords (ex. x=3, y=-5; NOT 3, -5)
    x: int = 0 - delta of movement between columns; use positive values to move right, and negative values to move left
    y: int = 0 - delta of movement between rows; use positive values to move down, and negative values to move up

    Returns
    -------
    tuple[int, int] - new absolute position of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    ValueError: new position is outside the map - if new position after the relative movement is invalid
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
    current_pos = heroes[player][hero]['position']
    new_pos = (current_pos[0] + x, current_pos[1] + y)
    _move(player, hero, new_pos)
    return new_pos


def level_up(player: str, hero: str):
    """
    Levels up the hero.
    Leveling up upgrades your max health and melee damage,
    along with unlocking new abilities on levels 2 and 3.

    Parameters
    ----------
    player: str - name of the player that owns the hero (either 'player_1' or 'player_2')
    hero: str - name of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
    heroes[player][hero]['level'] += 1
    heroes[player][hero]['max_health'] = floor(1.4 * heroes[player][hero]['max_health'])
    heroes[player][hero]['damage'] = floor(1.6 * heroes[player][hero]['damage'])


def respawn(player: str, hero: str):
    """
    Moves the hero back to their spawn spot, and resets their health.
    To be used for respawning a dead hero after death.

    Parameters
    ----------
    player: str - name of the player that owns the hero (either 'player_1' or 'player_2')
    hero: str - name of the hero

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
    spawn_pos = game_rules['spawn'][player]
    heroes[player][hero]['position'] = spawn_pos
    heroes[player][hero]['health'] = heroes[player][hero]['max_health']


def _die(player: str, hero: str):
    """
    INTERNAL FUNCTION THAT ISN'T SUPPOSED TO BE IMPORTED ANYWHERE,
    AND IS INSTEAD ONLY USED IN THIS FILE.

    Processes the hero's death, if upon hurting it its health becomes 0.
    Currently, literally does nothing.

    !!! Might not be needed or become an importable function
    !!! in the future, since it's supposed to only be cleaned up
    !!! in a different phase after damage is inflicted, not immediately.
    """
    ...


def hurt(player: str, hero: str, amount: int) -> int:
    """
    Damages the hero by a specified amount.

    Parameters
    ----------
    player: str - name of the player that owns the hero (either 'player_1' or 'player_2')
    hero: str - name of the hero
    amount: int - the amount of damage to deal to the named hero (must be positive or 0)

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    ValueError: cannot inflict negative damage - if amount is negative
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
    if amount < 0: raise ValueError('cannot inflict negative damage')
    new_health = max(0, heroes[player][hero]['health'] - amount)
    heroes[player][hero]['health'] = new_health
    if new_health <= 0:
        _die(player, hero)
    return new_health


def heal(player: str, hero: str, amount: int) -> int:
    """
    Heals the hero by a specified amount. Caps at the hero's max_health.

    Parameters
    ----------
    player: str - name of the player that owns the hero (either 'player_1' or 'player_2')
    hero: str - name of the hero
    amount: int - the amount of healing to do to the named hero (must be positive or 0)

    Raises
    ------
    ValueError: player doesn't have the hero - if no hero of that name owned by specified player found
    ValueError: cannot inflict negative healing - if amount is negative
    """
    if hero not in heroes[player]: raise ValueError(f"player {player} doesn't have a hero called {hero}")
    if amount < 0: raise ValueError('cannot inflict negative healing')
    max_health = heroes[player][hero]['max_health']
    new_health = min(heroes[player][hero]['health'] + amount, max_health)
    heroes[player][hero]['health'] = new_health
    return new_health