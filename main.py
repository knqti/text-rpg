import os
import time
from classes import *
from menus import *
from utils import *
from combat import *


def player_setup():
    clear_screen()

    question_name = '\nWhat is your name?\n'
    typewriter(question_name)
    input_name = input('>>> ')

    question_job = '\nWhat is your job?\n'
    typewriter(question_job)
    print('Select `warrior`, `cleric`, or `mage`.')
    input_job = input('>>> ').capitalize()

    # Initialize the player object
    player_obj = Player(
        name=input_name,
        job=input_job,
        max_hp=10,
        current_hp=10,
        defense=0,
        attack=0,
        damage=0,
        head_count='',
        torso_count='',
        arms_count='',
        legs_count=''
    )
    print(f'\nHello, {player_obj.name} the {player_obj.job}!')
    return player_obj

title_screen()

player_obj = player_setup()

# for attr, value in vars(player_obj).items():
#     print(f'{attr}: {value}')

# some encounter
monster = random_monster()
monster_obj = create_monster(monster, monsters_dict)
print(f'\nA {monster_obj.name} appeared')

results = fight(player_obj, monster_obj)

if results['defense result'] == 'fail':
    print(f'Your HP is {player_obj.current_hp}')
    print(f'You took {results['receive damage']} damage')
    hp_bar = '#' * player_obj.current_hp
    empty_bar = ' ' * (player_obj.max_hp - player_obj.current_hp)
    print(f'HP: {player_obj.current_hp}/{player_obj.max_hp} [' + f'{hp_bar}' + f'{empty_bar}' + ']')
else:
    print('nothing happened')