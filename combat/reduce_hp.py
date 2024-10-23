def reduce_hp(Character_obj:object, combat_results_dict:dict):
    # Reduce player's HP
    if hasattr(Character_obj, 'game_over'):
        Player_obj = Character_obj
        damage = combat_results_dict['receive damage']
        new_hp = Player_obj.current_hp - damage       
        Player_obj.current_hp = max(new_hp, 0)

    # Reduce monster's HP
    else:
        Monster_obj = Character_obj
        damage = combat_results_dict['attack damage']
        Monster_obj.hp -= damage
