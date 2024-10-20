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
