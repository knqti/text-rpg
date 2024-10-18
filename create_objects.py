from classes import *

def create_room(room, rooms_dict:dict):
    stats = rooms_dict[room]

    room_obj = Room(
        name=stats['name'],
        monster_a=stats['monster_a'],
        monster_b=stats['monster_b'],
        monster_c=stats['monster_c'],
        item_a=stats['item_a'],
        item_b=stats['item_b'],
        item_c=stats['item_c'],
        description=stats['description']
    )
    return room_obj