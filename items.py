# Level 1
weapons_1_dict = {
    'femur': {'defense': 0, 'attack': 2, 'damage': 2, 'slot': 'hand_1', 'type': 'equip', 'description': 'did someone drop this?'},
    'umbrella': {'defense': 0, 'attack': 3, 'damage': 1, 'slot': 'hand_1', 'type': 'equip', 'description': 'it is a bit damp in here...'}, 
    'shiv': {'defense': 0, 'attack': 1, 'damage': 3, 'slot': 'hand_1', 'type': 'equip', 'description': 'perfect for any occasion'}
}

armors_1_dict = {
    'hoodie': {'defense': 1, 'attack': 0, 'damage': 0, 'slot': 'torso', 'type': 'equip', 'description': 'warm and cozy'},
    'strap-on': {'defense': 0, 'attack': 2, 'damage': 0, 'slot': 'legs', 'type': 'equip', 'description': 'oh look, it vibrates'},
    'bike helmet': {'defense': 2, 'attack': 0, 'damage': 0, 'slot': 'head', 'type': 'equip', 'description': 'safety first'}
}

consumables_1_dict = {
    'rotten peach': {'defense': 0, 'attack': 0, 'damage': -1, 'slot': None, 'type': 'consume', 'description': 'it is rotten (-1 HP)'},
    'stale bread': {'defense': 0, 'attack': 0, 'damage': 2, 'slot': None, 'type': 'consume', 'description': 'mold is fiber right? (+2 HP)'},
    'donut': {'defense': 0, 'attack': 0, 'damage': 3, 'slot': None, 'type': 'consume', 'description': 'mmm donut (+3 HP)'}
}

all_items_1_dict = {
    **weapons_1_dict, 
    **armors_1_dict,
    **consumables_1_dict
}