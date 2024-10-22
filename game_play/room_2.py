from combat import encounter, random_monster
from dictionaries import monsters_2_dict
from initialize import init_monster
from utils import typewriter


def room_2(Player_obj:object):
    monster = random_monster(monsters_2_dict)
    Monster_obj = init_monster(monster, monsters_2_dict)

    typewriter('\nThe darkness begins to lift as you ascend the staircase.')
    typewriter('You reach the top and freedom is within your grasp-')
    typewriter(f'\nA {Monster_obj.name} appeared!')
    typewriter(f'{Monster_obj.description}')

    # Encounter C
    combat_results_dict = encounter(Player_obj, Monster_obj)