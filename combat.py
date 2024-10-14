from random import randint as roll
from monsters import *
from classes import *
from utils import *

def random_monster():
    monster_keys_list = list(monsters_dict.keys())
    number_of_monsters = len(monster_keys_list)
    result = roll(0, (number_of_monsters - 1))
    monster = monster_keys_list[result]    
    return monster

def create_monster(monster, monsters_dict:dict):
    stats = monsters_dict[monster]
    monster_name = str(monster).capitalize()
    
    monster_obj = Monster(
        name=monster_name,
        hp=stats['hp'],
        defense=stats['defense'],
        attack=stats['attack'],
        damage=stats['damage']
    )
    return monster_obj

def roll_initiative(combat_results_dict:dict):
    initiative_roll = roll(0, 1)

    if initiative_roll == 0:
        result = 'monster'
    elif initiative_roll == 1:
        result = 'player'
    
    combat_results_dict.update({'goes first': result})

def roll_combat(player:object, monster:object, combat_results_dict:dict):       
    attack_roll = roll(1, 20) + player.attack + monster.defense
    defense_roll = roll(1, 20) + player.defense + monster.attack

    # Attack against monster
    if attack_roll >= 12:
        attack_result = 'success'
        attack_damage = player.damage        
    else:
        attack_result = 'fail'
        attack_damage = 0

    # Defend from monster
    if defense_roll < 12:
        defense_result = 'fail'
        receive_damage = monster.damage
    else:        
        defense_result = 'success'
        receive_damage = 0

    combat_results_dict.update({
        'attack roll': attack_roll,
        'attack result': attack_result,
        'attack damage': attack_damage,
        'defense roll': defense_roll,
        'defense result': defense_result,
        'receive damage': receive_damage,
    })

def reduce_hp(character:object, combat_results_dict:dict):
    # Reduce player's HP
    if hasattr(character, 'game_over'):
        player_obj = character
        damage = combat_results_dict['receive damage']
        player_obj.current_hp -= damage        

    # Reduce monster's HP
    else:
        monster_obj = character
        damage = combat_results_dict['attack damage']
        monster_obj.hp -= damage

def fight(player:object, monster:object, combat_results_dict:dict):   
    roll_initiative(combat_results_dict)
    roll_combat(player, monster, combat_results_dict)
    
    # Player attacks monster 
    
    ######### NEED TO FIX THIS IF LOOP ##############
    
    if combat_results_dict['goes first'] == 'player':
        # On hit
        if combat_results_dict['attack result'] == 'success':
            # Deal damage
            reduce_hp(monster, combat_results_dict)

            typewriter(f'\nYou hit the {monster.name}!')

            if monster.hp <= 0:
                combat_results_dict.update({'who died': 'monster'})

    # Monster attacks player
    elif combat_results_dict['goes first'] == 'monster':     
        # On hit
        if combat_results_dict['defense result'] == 'fail':
            # Deal damage
            reduce_hp(player, combat_results_dict)

            typewriter(f'\nIt hit you, ouch...')
            hp_bar = '#' * player.current_hp
            empty_bar = ' ' * (player.max_hp - player.current_hp)
            print(f'HP: {player.current_hp}/{player.max_hp} [' + f'{hp_bar}' + f'{empty_bar}' + ']')

            if player.current_hp <= 0:
                combat_results_dict.update({'who died': 'player'})

def encounter(player:object, monster:object):
    combat_results_dict = {
        'goes first': None,
        'attack roll': None,
        'attack result': None,
        'attack damage': None,
        'defense roll': None,
        'defense result': None,
        'receive damage': None,
        'who died': None
    }
    while combat_results_dict['who died'] == None:
        print('\nWhat do you want to do?')
        print('   - Fight -   ')
        print('   -  Run  -   ')
        player_input = input('>>> ').lower().strip()

        if player_input == 'fight':
            fight(player, monster, combat_results_dict)
        else:
            typewriter('\nYou escaped, phew.')
            return