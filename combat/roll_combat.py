from random import randint as roll


def roll_combat(Player_obj:object, Monster_obj:object, combat_results_dict:dict):
    attack_roll = roll(1, 20) + Player_obj.attack + Monster_obj.defense
    defense_roll = roll(1, 20) + Player_obj.defense + Monster_obj.attack

    # Attack against monster
    if attack_roll >= 20:
        attack_result = 'success'
        attack_damage = Player_obj.damage * 2
    elif attack_roll >= 12:
        attack_result = 'success'
        attack_damage = Player_obj.damage
    else:
        attack_result = 'fail'
        attack_damage = 0

    # Defend from monster
    if defense_roll <= 1:
        defense_result = 'fail'
        receive_damage = Monster_obj.damage * 2
    elif defense_roll < 12:
        defense_result = 'fail'
        receive_damage = Monster_obj.damage
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
