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
