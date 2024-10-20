from random import randint as roll


def random_monster(dictionary:dict):
    monster_keys_list = list(dictionary.keys())
    number_of_monsters = len(monster_keys_list)
    result = roll(0, (number_of_monsters - 1))
    monster = monster_keys_list[result]    
    return monster
