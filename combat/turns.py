from utils import display_ascii, typewriter
from .reduce_hp import reduce_hp


def someone_died(combat_results_dict: dict):
    if combat_results_dict['who died'] == None:
        return False
    else:
        return True

def player_turn(Monster_obj:object, combat_results_dict:dict):
    # Display attack roll
    attack_roll = combat_results_dict['attack roll']
    typewriter('\nAttack roll:')
    display_ascii(attack_roll)
    
    # Player attacks monster
    if combat_results_dict['attack result'] == 'success':
        # Deal damage
        reduce_hp(Monster_obj, combat_results_dict)
        typewriter(f'\nYou hit the {Monster_obj.name} for {combat_results_dict["attack damage"]} damage!')
        
        if Monster_obj.hp <= 0:
            combat_results_dict.update({'who died': 'monster'})
            combat_results_dict.update({'gets loot': True})
            typewriter(f'\nYou have slain the {Monster_obj.name}, huzzah!')
            
    else:
        typewriter('\nYour attack misses.')

def monster_turn(Player_obj:object, combat_results_dict:dict):
    # Display defense roll
    defense_roll = combat_results_dict['defense roll']
    typewriter('\nDefense roll:')
    display_ascii(defense_roll)
    
    # Monster attacks player
    if combat_results_dict['defense result'] == 'fail':
        # Deal damage
        reduce_hp(Player_obj, combat_results_dict)

        typewriter(f'\nIt hits you, ouch...')
        hp_bar = '#' * Player_obj.current_hp
        empty_bar = ' ' * (Player_obj.max_hp - Player_obj.current_hp)
        print(f'HP: {Player_obj.current_hp}/{Player_obj.max_hp} [' + f'{hp_bar}' + f'{empty_bar}' + ']')

        if Player_obj.current_hp <= 0:
            combat_results_dict.update({'who died': 'player'})
    
    else:
        typewriter(f'\nIts attack misses you.')

def turn_order(who_goes_first, Player_obj:object, Monster_obj:object, combat_results_dict:dict):
    if who_goes_first == 'player':
        player_turn(Monster_obj, combat_results_dict)
        if someone_died(combat_results_dict) is True:
            return True
        monster_turn(Player_obj, combat_results_dict)
        if someone_died(combat_results_dict) is True:
            return True

    elif who_goes_first == 'monster':
        monster_turn(Player_obj, combat_results_dict)
        if someone_died(combat_results_dict) is True:
            return True
        player_turn(Monster_obj, combat_results_dict)
        if someone_died(combat_results_dict) is True:
            return True
    
    # Nobody died
    return False
