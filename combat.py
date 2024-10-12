from random import randint as roll
from monsters import *
from classes import *


def random_monster():
    monster_keys_list = list(monsters_dict.keys())
    rolled = roll(0, 2)
    
    monster = monster_keys_list[rolled]
    monster_name = monster.capitalize()
    return monster, monster_name

def create_monster(monster, monster_name):
    stats = monsters_dict[monster]
    
    monster_obj = Monster(
        name=monster_name,
        hp=stats['hp'],
        defense=stats['defense'],
        damage=stats['damage']
    )

    return monster_obj

monster, monster_name = random_monster()
print(f'A wild {monster_name} appeared!')
monster_obj = create_monster(monster, monster_name)
print(f'HP: {monster_obj.hp}')
print(f'Defense: {monster_obj.defense}')
print(f'Damage: {monster_obj.damage}')