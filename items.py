weapons_dict = {
    'mace': {'defense': 0, 'attack': 1, 'damage': 3, 'slot name': 'hand', 'slot value': 1,'requires': 'martial', 'type': 'equip'},
    'staff': {'defense': 0, 'attack': 3, 'damage': 1, 'slot name': 'hand', 'slot value': 2,'requires': 'common', 'type': 'equip'}, 
    'sword': {'defense': 0, 'attack': 2, 'damage': 3, 'slot name': 'hand', 'slot value': 1,'requires': 'martial', 'type': 'equip'},
    'wand': {'defense': 0, 'attack': 0, 'damage': 0, 'slot name': 'hand', 'slot value': 1,'requires': 'common', 'type': 'equip'}
}

armor_dict = {
    'armor (leather)': {'defense': 2, 'attack': 0, 'damage': 0,'slot name': 'torso', 'slot value': 1,'requires': 'common', 'type': 'equip'},
    'armor (steel)': {'defense': 3, 'attack': 0, 'damage': 0,'slot name': 'torso', 'slot value': 1,'requires': 'martial', 'type': 'equip'},
    'greaves (leather)': {'defense': 1, 'attack': 0, 'damage': 0,'slot name': 'legs', 'slot value': 1,'requires': 'common', 'type': 'equip'},
    'greaves (steel)': {'defense': 2, 'attack': 0, 'damage': 0,'slot name': 'legs', 'slot value': 1,'requires': 'martial', 'type': 'equip'},
    'helmet (leather)': {'defense': 1, 'attack': 0, 'damage': 0,'slot name': 'head', 'slot value': 1,'requires': 'common', 'type': 'equip'},
    'helmet (steel)': {'defense': 2, 'attack': 0, 'damage': 0,'slot name': 'head', 'slot value': 1,'requires': 'martial', 'type': 'equip'},
    'shield': {'defense': 1, 'attack': 0, 'damage': 0,'slot name': 'hand', 'slot value': 1,'requires': 'common', 'type': 'equip'}    
}

all_items_dict = {**weapons_dict, **armor_dict}