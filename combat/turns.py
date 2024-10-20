def someone_died(combat_results_dict: dict):
    if combat_results_dict['who died'] == None:
        return False
    else:
        return True

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
