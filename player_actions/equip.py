from initialize import init_item
from utils import typewriter
from .unequip import unequip


def equip(Player_obj:object, item:str, items_dict:dict):
    # Initialize the Item object
    Item_To_Equip_obj = init_item(item, items_dict)

    # Check type
    if Item_To_Equip_obj.type != 'equip':
        print(f'\n{Item_To_Equip_obj.name} cannot be equipped.')
        return

    # Check slot
    body_part = Item_To_Equip_obj.slot
    equipped_item = getattr(Player_obj, body_part)

    while equipped_item is not None:
        print(f'\nYour {body_part} is occupied')
        print(f'Do you want to discard your {equipped_item}? (y/n)')
        update_slot = input('>>> ').lower().strip()

        if update_slot == 'y':
            unequip(Player_obj, equipped_item, items_dict)
            break
        elif update_slot == 'n':
            typewriter(f'\n{Item_To_Equip_obj.name} discarded')
            return

    # Update player stats
    Player_obj.defense += Item_To_Equip_obj.defense
    Player_obj.attack += Item_To_Equip_obj.attack
    Player_obj.damage += Item_To_Equip_obj.damage
    setattr(Player_obj, body_part, Item_To_Equip_obj.name)
    print(f'\n{Item_To_Equip_obj.name} equipped')
    typewriter(f'{Item_To_Equip_obj.description}')
