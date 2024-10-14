from classes import *
from items import all_items_dict
from utils import clear_screen, typewriter


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
        slot = stats['slot']
    )
    return item_instance

def player_setup():
    clear_screen()

    question_name = '\nWhat is your name?\n'
    typewriter(question_name)
    input_name = input('>>> ').strip()

    question_job = '\nWhat is your job?\n'
    typewriter(question_job)
    print('Select `warrior`, `cleric`, or `mage`.')
    input_job = input('>>> ').capitalize().strip()

    # Initialize the Player object
    player_obj = initialize_player(input_name, input_job)
    print(f'\nHello, {player_obj.name} the {player_obj.job}!')
    return player_obj

def search_items_dict(item:str, dictionary:dict):
    if item not in dictionary:
        print(f'\n{item} not found. Please try again.')
    else:
        return dictionary[item]

def equip(player:object, item:str, items_dict:dict):
    # Get the item stats from the dictionary
    item_name = str(item.lower().strip())
    item_stats = search_items_dict(item_name, items_dict)
    
    # Initialize the Item object
    item_obj = initialize_item(item_stats)

    # Check type
    if item_stats['type'] is not 'equip':
        print(f'\n{item.capitalize()} cannot be equipped.')
        return

    # Check slot
    body_part = item_obj.slot
    player_slot = getattr(player, body_part)

    if player_slot is not None:
        print(f'\nYour {player_slot} is occupied. {item.capitalize()} cannot be equipped.')

    # Update player stats
    player.defense += item_obj.defense
    player.attack += item_obj.attack
    player.damage += item_obj.damage
    setattr(player, body_part, item_name)

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



##### TEST RUN #####
# player_obj = player_setup()

# for attr, value in vars(player_obj).items():
#     print(f'{attr}: {value}')

# item = 'staff'

# equip(player_obj, item, all_items_dict)

# print('\nEquipped!')
# for attr, value in vars(player_obj).items():
#     print(f'{attr}: {value}')

# unequip(player_obj, item, all_items_dict)

# print('\nUnquipped!')
# for attr, value in vars(player_obj).items():
#     print(f'{attr}: {value}')