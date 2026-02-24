"""
temporary file to make some very
very
interesting experiments
no they wont go darker than dark i promise the darkness wont cut deep
"""


from data.game_state import *


def raises(func, *args, **kwargs):
    flag = False
    try:
        func(*args, **kwargs)
    except Exception as e:
        print(f'  * <{func.__module__}.{func.__name__}> raised "{e}" (expected)')
        flag = True
        pass
    assert flag, 'expected raise, function passed'


print()
print('! map creation')
create_game_rules((10, 10), 10, (2, 2), (8, 8), [(5, 5), (6, 5), (4, 5), (5, 6), (5, 4)])
raises(create_game_rules, (20, 12), 15, (2, 2), (8, 8), [(5, 5), (6, 5), (4, 5), (5, 6), (5, 4)])


print()
print('! hero creation')
heroes.create('player_1', 'lostya', 'healer')
heroes.create('player_2', 'findya', 'mage')
heroes.create('player_1', 'bluebarbarian', 'barbarian')
heroes.create('player_2', 'redrogue', 'rogue')
raises(heroes.create, 'player_2', 'findya', 'mage') # existing hero
raises(heroes.create, 'player_2', 'lostya', 'mage') # existing hero from other player
raises(heroes.create, 'player_2', 'coolguy123', 'mage') # numbers in name
raises(heroes.create, 'player_2', 'coolguy', 'verynicenonexistentclass') # bad class
heroes.create('player_2', 'testinghero', 'rogue')
heroes.create('player_2', 'testingherotwice', 'rogue')
raises(heroes.create,'player_2', 'testingherothrice', 'rogue') # more than 4 heroes per player


print()
print('! creature creation')
creatures.create('coolguy', (3, 5), 10, 3, 4)
creatures.create('badguy', (4, 10), 5, 8, 3)
raises(creatures.create, 'coolguy', (6, 9), 10, 3, 20) # existing creature
raises(creatures.create, 'coolguyss', (6, 999), 10, 3, 20) # bad position


print()
print('! hero data getting')
assert heroes.get_player('lostya') == 'player_1'
assert heroes.get_player('findya') == 'player_2'
assert heroes.get_level('lostya') == 1
assert heroes.get_pos('lostya') == (2, 2)
assert heroes.get_pos('findya') == (8, 8)
raises(heroes.get_health, 'fbdshikaa') # nonexistent hero
raises(heroes.get_health, 'lostya', player='player_2') # player 2 doesnt own lostya
assert heroes.get_health('lostya') == 10
assert heroes.get_health('bluebarbarian') == 15
assert heroes.get_damage('lostya') == 2
assert heroes.get_damage('redrogue') == 3
assert heroes.get_max_health('lostya') == heroes.get_health('lostya')
assert heroes.get_class('lostya') == 'healer'
assert heroes.get_effects('lostya') == []
assert heroes.get_owned_abilities('lostya') == []
assert heroes.get_turns_on_spur('lostya') == 0


print()
print('! creature data getting')
assert creatures.get_damage('coolguy') == 3
assert creatures.get_range('badguy') == 3
assert creatures.get_effects('coolguy') == []
assert creatures.get_pos('coolguy') == (3, 5)
assert creatures.get_damage('coolguy') == 3\


print()
print('! hero data manipulation')
heroes.increment_turns_on_spur('lostya', player='player_1')
heroes.increment_turns_on_spur('lostya')
assert heroes.get_turns_on_spur('lostya') == 2
heroes.reset_turns_on_spur('lostya')
assert heroes.get_turns_on_spur('lostya') == 0
raises(heroes.move, 'lostya', (3, 716892)) # bad position
heroes.move('lostya', (3, 9))
assert heroes.get_pos('lostya') == (3, 9)
raises(heroes.move, 'lostya', (2, 2), player='player_2') # player 2 doesnt own lostya
assert heroes.get_pos('lostya') == (3, 9)
heroes.level_up('lostya')
assert heroes.get_level('lostya') == 2
assert heroes.get_damage('lostya') == 4
assert heroes.get_max_health('lostya') == 14
assert heroes.get_health('lostya') != 14
assert heroes.get_owned_abilities('lostya') == ['invigorate']
heroes.level_up('lostya')
assert heroes.get_level('lostya') == 3
assert heroes.get_owned_abilities('lostya') == ['invigorate', 'immunise']
heroes.level_up('lostya')
assert heroes.get_level('lostya') == 4
assert heroes.get_owned_abilities('lostya') == ['invigorate', 'immunise']
heroes.hurt('lostya', 3)
assert heroes.get_health('lostya') == 7
heroes.hurt('lostya', 999)
assert heroes.get_health('lostya') == 0
heroes.heal('lostya', 999)
assert heroes.get_health('lostya') == 28
raises(heroes.heal, 'lostya', -3) # negative heal
raises(heroes.hurt, 'lostya', -3) # negative damage
heroes.apply_effect('lostya', 'stun')
assert heroes.get_effects('lostya') == ['stun']
heroes.apply_effect('lostya', 'ovibus')
heroes.apply_effect('lostya', 'invincible')
assert heroes.get_effects('lostya') == ['stun', 'ovibus', 'invincible']
heroes.remove_effect('lostya', 'ovibus')
assert heroes.get_effects('lostya') == ['stun', 'invincible']
heroes.reset_effects('lostya')
assert heroes.get_effects('lostya') == []
heroes.apply_effect('lostya', 'stun')
heroes.apply_effect('lostya', 'ovibus')
heroes.apply_effect('lostya', 'invincible')
heroes.apply_effect('findya', 'ovibus')
raises(heroes.apply_effect, 'lostya', 'ovibus')
raises(heroes.remove_effect, 'lostya', 'effecttheydonthave')


print()
print('! creature data manipulation')
creatures.hurt('coolguy', 5)
assert creatures.get_health('coolguy') == 5
creatures.hurt('coolguy', 50)
assert creatures.get_health('coolguy') == 0
raises(creatures.hurt, 'coolguy', -3) # negative damage
creatures.apply_effect('coolguy', 'stun')
assert creatures.get_effects('coolguy') == ['stun']
creatures.apply_effect('coolguy', 'ovibus')
creatures.apply_effect('coolguy', 'invincible')
assert creatures.get_effects('coolguy') == ['stun', 'ovibus', 'invincible']
creatures.remove_effect('coolguy', 'ovibus')
assert creatures.get_effects('coolguy') == ['stun', 'invincible']
creatures.reset_effects('coolguy')
assert creatures.get_effects('coolguy') == []
creatures.apply_effect('coolguy', 'stun')
creatures.apply_effect('coolguy', 'ovibus')
creatures.apply_effect('coolguy', 'invincible')
creatures.apply_effect('badguy', 'ovibus')
raises(creatures.apply_effect, 'coolguy', 'ovibus')
raises(creatures.remove_effect, 'coolguy', 'effectitdoesnthave')


print()
print('! global entity data')

clear_effect('ovibus')
assert 'ovibus' not in creatures.get_effects('coolguy')
assert 'ovibus' not in creatures.get_effects('badguy')
assert 'ovibus' not in heroes.get_effects('lostya')
assert 'ovibus' not in heroes.get_effects('findya')

print(get_all_entity_positions())
print(get_entities_at((2, 2)))
print(get_entities_at((8, 8)))
empty_list = get_entities_at((10, 10))
print(empty_list)
assert empty_list == {"creatures": {}, "heroes": {"player_1": {}, "player_2": {}}}

print()
print('gg')