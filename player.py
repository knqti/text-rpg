from classes import *
from items import all_items_dict
from utils import clear_screen, typewriter


def player_setup():
    clear_screen()

    question_name = '\nWhat is your name?\n'
    typewriter(question_name)
    input_name = input('>>> ')

    question_job = '\nWhat is your job?\n'
    typewriter(question_job)
    print('Select `warrior`, `cleric`, or `mage`.')
    input_job = input('>>> ').capitalize()

    # Initialize the Player object
    player_obj = Player(
        name=input_name,
        job=input_job,
        max_hp=10,
        current_hp=10,
        defense=0,
        attack=0,
        damage=0,
        head=1,
        torso=1,
        hand=2,
        legs=1
    )
    print(f'\nHello, {player_obj.name} the {player_obj.job}!')
    return player_obj

def search_items_dict(item:str, dictionary:dict):
    if item not in dictionary:
        print(f'\n{item} not found. Please try again.')
    else:
        return dictionary[item]

def equip(player:object, item:str, items_dict:dict):
    # Get the item from the dictionary
    item_attributes = search_items_dict(item, items_dict)
    
    # Check type
    if item_attributes['type'] is not 'equip':
        print(f'\n{item} cannot be equipped.')
    
    # Check requires

    # Check slot

    # Initialize the Item object
    item_obj = Item(
        type = item_attributes['type'],
        defense = item_attributes['defense'],
        attack = item_attributes['attack'],
        damage = item_attributes['damage'],
        slot_name = item_attributes['slot name'],
        slot_value = item_attributes['slot value']
    )
    # Update player stats
    player.defense += item_obj.defense
    player.attack += item_obj.attack
    player.damage += item_obj.damage
    item_slot_name = item_obj.slot_name
    item_slot_value = item_obj.slot_value
    player_slot_value = getattr(player, item_slot_name)
    setattr(player, item_slot_name, player_slot_value - item_slot_value)



##### TEST RUN #####
player_obj = player_setup()

for attr, value in vars(player_obj).items():
    print(f'{attr}: {value}')

item = 'mace'
equip(player_obj, item, all_items_dict)

print('Equipped!')
for attr, value in vars(player_obj).items():
    print(f'{attr}: {value}')

