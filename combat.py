from random import randint as roll
from monsters import *
from classes import *


def random_monster():
    monster_keys_list = list(monsters_dict.keys())
    result = roll(0, 2)
    monster = monster_keys_list[result]    
    return monster

def create_monster(monster, monsters_dict:dict):
    stats = monsters_dict[monster]
    monster_name = str(monster).capitalize()
    
    monster_obj = Monster(
        name=monster_name,
        hp=stats['hp'],
        defense=stats['defense'],
        damage=stats['damage']
    )
    return monster_obj

def roll_combat(player:object, monster:object):
    attack_roll = roll(1, 20) + player.attack
    defense_roll = roll(1, 20) + player.defense + monster.defense

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

    results_dict = {
        'attack roll': attack_roll,
        'attack result': attack_result,
        'attack damage': attack_damage,
        'defense roll': defense_roll,
        'defense result': defense_result,
        'receive damage': receive_damage
    }
    return results_dict

def reduce_hp(player:object, results:dict):
    receive_damage = results['receive damage']
    player.current_hp -= receive_damage

def fight(player:object, monster:object):   
    combat_results_dict = {}
    combat_results_dict = roll_combat(player, monster)
    
    if combat_results_dict['defense result'] == 'fail':
        reduce_hp(player, combat_results_dict)

    return combat_results_dict

        # print(f'Your HP is {player_obj.current_hp}')
        # print(f'You took {combat_results_dict['receive damage']} damage')
        # hp_bar = '#' * player_obj.current_hp
        # empty_bar = ' ' * (player_obj.max_hp - player_obj.current_hp)
        # print(f'HP: {player_obj.current_hp}/{player_obj.max_hp} [' + f'{hp_bar}' + f'{empty_bar}' + ']')

    # Temporary player
    # player_obj = Player(
    #     name='',
    #     job='',
    #     max_hp=10,
    #     current_hp=10,
    #     defense=2,
    #     attack=0,
    #     damage=1,
    #     head_count='',
    #     torso_count='',
    #     arms_count='',
    #     legs_count=''
    # )