"""
The Game State module is the module that is responsible for the entirety of data management.


HOW TO USE
----------
When you "import game_state", you get some of "core", more general functions,
then 2 submodules - creatures and heroes.
(game_state.heroes, game_state.creatures OR just do from game_state import heroes, creatures).

An "entity" is either a hero or a creature.

To get a grasp of data structures, you may go through the creatures.py and heroes.py files yourself.
The docstrings there will show you the skeleton of the data structure used.

From now on, the functionality list will imply that you imported
the module as `from game_state import *`.


GENERAL FUNCTIONS
-----------------
- create_game_rules() is to be used strictly at the start of the game.
  It creates the game_rules dictionary.
- get_entities_at() gets you a list of all entities placed at the specified position.
  May be useful to deal damage or apply area effects.
- get_all_entity_positions() gets you a comprehensive list of all entities on the map.
  May be useful for game board rendering.
- is_legal_position() verifies if the position is inside the map or not.
  May be useful for verifying movement or attack destinations.
- reset_all_effects() resets ALL effects across all entities.
  May be useful for code responsible for ending turns to make sure nothing carries over.
- clear_effect() removes a certain effect across all entities.
  May be useful for certain cleanup phases. More granular than reset_all_effects().
- You may also directly access the data variables of entities using names
  hero_dict and creature_dict, as well as game_rules.
  NOTE: This is NOT RECOMMENDED and you should instead use related functions inside the respective entity module.


CREATURE FUNCTIONS
------------------
- creatures.create() creates a new creature with the specified stats.
- creatures.get_*() where * is a name of a stat
  is a set of functions the sole purpose of which is to easily get the desired stat.
  Functions exist for health, pos (position), damage, range and effects.
- creatures.hurt() deals damage to the creature.
- creatures.apply_effect() adds a new effect to the creature,
  and creatures.reset_effects() removes all effects from it.

HERO FUNCTIONS
--------------
- heroes.create() creates a new hero.
  Note that it only gets the hero's class instead of all stats like creatures.create() does.
  Instead, it derives all stats from the specified class.
- heroes.get_*() where * is a name of a stat
  is a set of functions to get the desired stat, as with creatures.
  Functions exist for health, max_health, class, level, pos (position), turns_on_spur, and effects.
  The exceptions to this are:
    - heroes.get_player() which returns the owner of the hero
      (since the hero names are unique in the entire game, not per-player)
    - heroes.get_owned_abilities() which returns the list of abilities the hero can use
      (derived on the hero's level and their class)
- heroes.move() moves the hero to the new spot.
- heroes.level_up() adds a level and increases damage and max health as per game rules.
- heroes.respawn() resets the hero's health to max health and position to spawn_position of hero's owner.
- heroes.hurt() deals damage to the hero.
- heroes.heal() heals the hero (maxes out at max_health).
- heroes.apply_effect() adds a new effect to the hero,
  and heroes.reset_effects() removes all effects from them.
- heroes.increment_turns_on_spur() adds 1 to turns on spur of the hero, and
  heroes.reset_turns_on_spur() sets it to 0.
"""


from copy import deepcopy # TODO: get rid of deepcopy
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


def reset_all_effects():
    # TODO: write specs
    for creature in creature_dict:
        creatures.reset_effects(creature)
    for player in hero_dict:
        for hero in hero_dict[player]:
            heroes.reset_effects(hero, player=player)


def clear_effect(effect: str):
    # TODO: write specs
    for creature in creature_dict:
        if effect in creatures.get_effects(creature): creatures.remove_effect(creature, effect)
    for player in hero_dict:
        for hero in hero_dict[player]:
            if effect in heroes.get_effects(hero, player=player): heroes.remove_effect(hero, effect, player=player)