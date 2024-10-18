from random import randint as roll
from monsters import *
from classes import *
from utils import *

def random_monster(dictionary:dict):
    monster_keys_list = list(dictionary.keys())
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
        damage=stats['damage'],
        description=stats['description']
    )
    return monster_obj

def roll_initiative(combat_results_dict:dict, monster:object):
    initiative_roll = roll(0, 1)

    if initiative_roll == 0:
        result = 'monster'
        typewriter(f'\nThe {monster.name} is faster than you.')
    elif initiative_roll == 1:
        result = 'player'
        typewriter(f'\nYou are faster than the {monster.name}.')
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

def player_turn(monster:object, combat_results_dict:dict):
    # Display attack roll
    attack_roll = combat_results_dict['attack roll']
    typewriter('\nAttack roll:')
    display_ascii(attack_roll)
    
    # Player attacks monster
    if combat_results_dict['attack result'] == 'success':
        # Deal damage
        reduce_hp(monster, combat_results_dict)
        typewriter(f'\nYou hit the {monster.name} for {combat_results_dict["attack damage"]} damage!')
        
        if monster.hp <= 0:
            combat_results_dict.update({'who died': 'monster'})
            typewriter(f'\nYou have slain the {monster.name}, huzzah!')
            
    else:
        typewriter('\nYour attack misses.')

def monster_turn(player:object, combat_results_dict:dict):
    # Display defense roll
    defense_roll = combat_results_dict['defense roll']
    typewriter('\nDefense roll:')
    display_ascii(defense_roll)
    
    # Monster attacks player
    if combat_results_dict['defense result'] == 'fail':
        # Deal damage
        reduce_hp(player, combat_results_dict)

        typewriter(f'\nIt hits you, ouch...')
        hp_bar = '#' * player.current_hp
        empty_bar = ' ' * (player.max_hp - player.current_hp)
        print(f'HP: {player.current_hp}/{player.max_hp} [' + f'{hp_bar}' + f'{empty_bar}' + ']')

        if player.current_hp <= 0:
            combat_results_dict.update({'who died': 'player'})
            typewriter('\nYou died :(')
    
    else:
        typewriter(f'\nIts attack misses you.')

def someone_died(combat_results_dict: dict):
    if combat_results_dict['who died'] == None:
        return False
    else:
        return True

def turn_order(who_goes_first, player:object, monster:object, combat_results_dict:dict):
    if who_goes_first == 'player':
        player_turn(monster, combat_results_dict)
        if someone_died(combat_results_dict) is True:
            return True
        monster_turn(player, combat_results_dict)
        if someone_died(combat_results_dict) is True:
            return True

    elif who_goes_first == 'monster':
        monster_turn(player, combat_results_dict)
        if someone_died(combat_results_dict) is True:
            return True
        player_turn(monster, combat_results_dict)
        if someone_died(combat_results_dict) is True:
            return True
    
    # Nobody died
    return False

def fight(player:object, monster:object, combat_results_dict:dict):       
    death_occurred = False
    
    while death_occurred is False:
        print('\nWhat do you want to do?')
        print('   -  Attack  -   ')
        print('   -   Run    -   ')
        player_input = input('>>> ').lower().strip()

        if player_input == 'attack':
            roll_combat(player, monster, combat_results_dict)
        elif player_input == 'run':
            typewriter('\nYou escaped, phew.')
            return
        
        who_goes_first = combat_results_dict['goes first']
        death_occurred = turn_order(who_goes_first, player, monster, combat_results_dict)

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
    roll_initiative(combat_results_dict, monster)
    fight(player, monster, combat_results_dict)
