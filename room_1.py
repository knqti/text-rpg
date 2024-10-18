from classes import *
from combat import create_monster, encounter, random_monster
from create_objects import *
from items import consumables_1_dict
from monsters import monsters_1_dict
from player import consume_item, display_player_stats
from rooms import room_1_dict
from utils import display_items, typewriter


def room_1(player:object):
    player_obj = player
    
    # Initialize 2 monsters
    monster_a = random_monster(monsters_1_dict)
    monster_a_obj = create_monster(monster_a, monsters_1_dict)
    monster_b = random_monster(monsters_1_dict)

    # Ensure no duplicate monsters
    while monster_b == monster_a:
        monster_b = random_monster(monsters_1_dict)
    monster_b_obj = create_monster(monster_b, monsters_1_dict)

    typewriter(f'You walk into {room_1_dict["name"].capitalize()}, a dimly-lit crypt.')
    typewriter(f'Stale dust and the smell of mold waft into your nose. You\'re about to the corner when you hear:')
    typewriter(f'{monster_a_obj.description}')

    # Encounter
    typewriter(f'\nA {monster_a_obj.name.capitalize()} appeared!')
    encounter(player_obj, monster_a_obj)

    # Loot
    typewriter(f'\nSome items drop from the {monster_a_obj.name}\'s lifeless form.')
    display_items(consumables_1_dict)
    typewriter('\nPick one to consume.')
    selected_consumable = input('>>> ').lower().strip()
    typewriter(f'\n{consumables_1_dict[selected_consumable]["description"]}')
    consume_item(player_obj, selected_consumable, consumables_1_dict)
    display_player_stats(player_obj)

    # Encounter
    typewriter(f'\nYou barely finish when a {monster_b_obj.name} ambushes you!')
    typewriter(f'{monster_b_obj.description}')
    encounter(player_obj, monster_b_obj)

    # Loot
    typewriter(f'\nSome items drop from the {monster_a_obj.name}\'s lifeless form.')
    display_items(consumables_1_dict)
    typewriter('\nPick one to consume.')
    selected_consumable = input('>>> ').lower().strip()
    typewriter(f'\n{consumables_1_dict[selected_consumable]["description"]}')    