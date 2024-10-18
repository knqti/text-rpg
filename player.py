from classes import *
from items import all_items_dict
from utils import clear_screen, typewriter
from menus import display_player_stats


def initialize_player(name, job):
    player_instance = Player(
        name=name,
        job=job,
        max_hp=10,
        current_hp=10,
        defense=0,
        attack=0,
        damage=0,
        head=None,
        torso=None,
        hand_1=None,
        hand_2=None,
        legs=None
    )
    return player_instance

def initialize_item(stats):
    item_instance = Item(
        type = stats['type'],
        defense = stats['defense'],
        attack = stats['attack'],
        damage = stats['damage'],
        slot = stats['slot'],
        description= stats['description']
    )
    return item_instance

def player_setup():
    clear_screen()

    typewriter('\nWhat is your name?')
    input_name = input('>>> ').strip()

    typewriter('\nWhat is your job?')
    # print('Select `warrior`, `cleric`, or `mage`')
    input_job = input('>>> ').capitalize().strip()

    # Initialize the Player object
    player_obj = initialize_player(input_name, input_job)
    # typewriter(f'\nHello, {player_obj.name} the {player_obj.job}!')
    return player_obj

def search_items_dict(item:str, dictionary:dict):
    if item not in dictionary:
        print(f'\n{item} not found. Please try again.')
    else:
        return dictionary[item]

def unequip(player:object, item:str, items_dict:dict):
    # Get the item stats from the dictionary
    item_name = str(item.lower().strip())
    item_stats = search_items_dict(item_name, items_dict)

    # Initialize the Item object
    item_obj = initialize_item(item_stats)

    # Update player stats
    player.defense -= item_obj.defense
    player.attack -= item_obj.attack
    player.damage -= item_obj.damage
    body_part = item_obj.slot
    setattr(player, body_part, None)
    print(f'\n{item_name.capitalize()} discarded')

def equip(player:object, item:str, items_dict:dict):
    # Get the item stats from the dictionary
    item_name = str(item.lower().strip())
    item_stats = search_items_dict(item_name, items_dict)
    
    # Initialize the Item object
    item_obj = initialize_item(item_stats)

    # Check type
    if item_stats['type'] != 'equip':
        print(f'\n{item.capitalize()} cannot be equipped.')
        return

    # Check slot
    body_part = item_obj.slot
    equipped_item = getattr(player, body_part)

    while equipped_item is not None:
        print(f'\nYour {body_part} is occupied')
        print(f'Do you want to discard your {equipped_item.capitalize()}? (y/n)')
        update_slot = input('>>> ').lower().strip()

        if update_slot == 'y':
            unequip(player, equipped_item, items_dict)
            break
        elif update_slot == 'n':
            typewriter(f'\n{item_name.capitalize()} discarded')
            return

    # Update player stats
    player.defense += item_obj.defense
    player.attack += item_obj.attack
    player.damage += item_obj.damage
    setattr(player, body_part, item_name)
    print(f'\n{item_name.capitalize()} equipped')

def consume_item(player:object, item:str, items_dict:dict):
    # Get the item stats from the dictionary
    item_name = str(item.lower().strip())
    item_stats = search_items_dict(item_name, items_dict)

    # Initialize the Item object
    item_obj = initialize_item(item_stats)

    # Check type
    if item_stats['type'] != 'consume':
        print(f'\n{item.capitalize()} cannot be consumed.')
        return
    
    # Update player stats
    player.defense += item_obj.defense
    player.attack += item_obj.attack
    new_hp = player.current_hp + item_obj.damage
    hp_change = new_hp - player.current_hp
    player.current_hp = min(new_hp, player.max_hp)
    