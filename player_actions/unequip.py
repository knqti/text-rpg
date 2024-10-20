from initialize import init_item


def unequip(Player_obj:object, item:str, items_dict:dict):
    # Initialize the Item object
    Item_To_Unequip_obj = init_item(item, items_dict)

    # Update player stats
    Player_obj.defense -= Item_To_Unequip_obj.defense
    Player_obj.attack -= Item_To_Unequip_obj.attack
    Player_obj.damage -= Item_To_Unequip_obj.damage
    body_part = Item_To_Unequip_obj.slot
    setattr(Player_obj, body_part, None)
    print(f'\n{Item_To_Unequip_obj.name} discarded')
