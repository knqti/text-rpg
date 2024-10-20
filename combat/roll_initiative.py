def roll_initiative(combat_results_dict:dict, monster:object):
    initiative_roll = roll(0, 1)

    if initiative_roll == 0:
        result = 'monster'
        typewriter(f'\nThe {monster.name} is faster than you.')
    elif initiative_roll == 1:
        result = 'player'
        typewriter(f'\nYou are faster than the {monster.name}.')
    combat_results_dict.update({'goes first': result})
