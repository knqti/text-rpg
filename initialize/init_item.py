from classes import Item


def init_item(item, items_dict:dict):
    stats = items_dict[item.lower()]
    item_name = item.title()

    item_instance = Item(
        name = item_name,
        type = stats['type'],
        defense = stats['defense'],
        attack = stats['attack'],
        damage = stats['damage'],
        slot = stats['slot'],
        description= stats['description']
    )
    return item_instance
