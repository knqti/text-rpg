# Level 1
weapons_1_dict = {
    'femur': {'defense': 0, 'attack': 2, 'damage': 2, 'slot': 'hand_1', 'type': 'equip'},
    'umbrella': {'defense': 0, 'attack': 3, 'damage': 1, 'slot': 'hand_1', 'type': 'equip'}, 
    'shiv': {'defense': 0, 'attack': 1, 'damage': 3, 'slot': 'hand_1', 'type': 'equip'}
}

armors_1_dict = {
    'hoodie': {'defense': 1, 'attack': 0, 'damage': 0,'slot': 'torso', 'type': 'equip'},
    'strap-on': {'defense': 0, 'attack': 2, 'damage': 0,'slot': 'legs', 'type': 'equip'},
    'bike helmet': {'defense': 2, 'attack': 0, 'damage': 0,'slot': 'head', 'type': 'equip'}
}

# Level 2
# weapons_2_dict = {
#     'warhammer': {'defense': 0, 'attack': 2, 'damage': 2, 'slot': 'hand_1', 'type': 'equip'},
#     'spear': {'defense': 0, 'attack': 3, 'damage': 1, 'slot': 'hand_1', 'type': 'equip'}, 
#     'machete': {'defense': 0, 'attack': 1, 'damage': 3, 'slot': 'hand_1', 'type': 'equip'}
# }

# armors_2_dict = {
#     'shirt': {'defense': 2, 'attack': 0, 'damage': 0,'slot': 'torso', 'type': 'equip'},
#     'pants': {'defense': 1, 'attack': 0, 'damage': 0,'slot': 'legs', 'type': 'equip'},
#     'helmet': {'defense': 2, 'attack': 0, 'damage': 0,'slot': 'head', 'type': 'equip'},
#     'shield': {'defense': 1, 'attack': 0, 'damage': 0,'slot': 'hand_2', 'type': 'equip'}    
# }

all_items_dict = {**weapons_1_dict, **armors_1_dict}