from random import randint as roll
from utils import typewriter


def roll_initiative(combat_results_dict:dict, Monster_obj:object):
    initiative_roll = roll(0, 1)

    if initiative_roll == 0:
        result = 'monster'
        typewriter(f'\nThe {Monster_obj.name} is faster than you.')
    elif initiative_roll == 1:
        result = 'player'
        typewriter(f'\nYou are faster than the {Monster_obj.name}.')
    combat_results_dict.update({'goes first': result})
