weapons_dict = {
    'club': {'defense': 0, 'attack': 1, 'damage': 2, 'slot': 'hand_1', 'type': 'equip'},
    'staff': {'defense': 0, 'attack': 3, 'damage': 1, 'slot': 'hand_1', 'type': 'equip'}, 
    'sword': {'defense': 0, 'attack': 2, 'damage': 3, 'slot': 'hand_1', 'type': 'equip'},
    'wand': {'defense': 0, 'attack': 0, 'damage': 0, 'slot': 'hand_1', 'type': 'equip'}
}

armor_dict = {
    'armor (leather)': {'defense': 2, 'attack': 0, 'damage': 0,'slot': 'torso', 'type': 'equip'},
    'armor (steel)': {'defense': 3, 'attack': 0, 'damage': 0,'slot': 'torso', 'type': 'equip'},
    'greaves (leather)': {'defense': 1, 'attack': 0, 'damage': 0,'slot': 'legs', 'type': 'equip'},
    'greaves (steel)': {'defense': 2, 'attack': 0, 'damage': 0,'slot': 'legs', 'type': 'equip'},
    'helmet (leather)': {'defense': 1, 'attack': 0, 'damage': 0,'slot': 'head', 'type': 'equip'},
    'helmet (steel)': {'defense': 2, 'attack': 0, 'damage': 0,'slot': 'head', 'type': 'equip'},
    'shield': {'defense': 1, 'attack': 0, 'damage': 0,'slot': 'hand_2', 'type': 'equip'}    
}

all_items_dict = {**weapons_dict, **armor_dict}