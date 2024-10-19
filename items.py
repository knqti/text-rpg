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
    'rotten peach': {'defense': 0, 'attack': 0, 'damage': -1, 'slot': None, 'type': 'consume', 'description': 'yup still rotten (-1 HP)'},
    'stale bread': {'defense': 0, 'attack': 0, 'damage': 2, 'slot': None, 'type': 'consume', 'description': 'mold has fiber right? (+2 HP)'},
    'donut': {'defense': 0, 'attack': 0, 'damage': 3, 'slot': None, 'type': 'consume', 'description': 'mmm donut (+3 HP)'}
}

weapons_2_dict = {
    'hammer': {'defense': 0, 'attack': 2, 'damage': 3, 'slot': 'hand_1', 'type': 'equip', 'description': 'can\'t touch this'},
    'hoe': {'defense': 0, 'attack': 3, 'damage': 2, 'slot': 'hand_1', 'type': 'equip', 'description': 'ditch that, hoe'}, 
    'ho': {'defense': 0, 'attack': 2, 'damage': 1, 'slot': 'hand_2', 'type': 'equip', 'description': 'oh my god i\'m saved!'}
}

armors_2_dict = {
    'straitjacket': {'defense': 4, 'attack': -2, 'damage': 0, 'slot': 'torso', 'type': 'equip', 'description': 'extremely snug'},
    'leather pants': {'defense': 2, 'attack': 0, 'damage': 0, 'slot': 'legs', 'type': 'equip', 'description': 'makes your butt look big'},
    'shield': {'defense': 2, 'attack': 0, 'damage': 0, 'slot': 'hand_2', 'type': 'equip', 'description': 'wuss'}
}

all_items_dict = {
    **weapons_1_dict, 
    **armors_1_dict,
    **consumables_1_dict,
    **weapons_2_dict,
    **armors_2_dict
}