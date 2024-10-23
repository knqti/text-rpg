from initialize import init_item


def consume_item(Player_obj:object, item:str, items_dict:dict):
    # Initialize the Item object
    Item_obj = init_item(item, items_dict)

    # Check type
    if Item_obj.type != 'consume':
        print(f'\n{Item_obj.name} cannot be consumed.')
        return
    
    # Update player stats
    Player_obj.defense += Item_obj.defense
    Player_obj.attack += Item_obj.attack
    new_hp = Player_obj.current_hp + Item_obj.damage
    Player_obj.current_hp = min(new_hp, Player_obj.max_hp)
    