from classes import *
from combat import create_monster, encounter, random_monster
from create_objects import *
from items import *
from monsters import monsters_1_dict
from player import consume_item, display_player_stats, equip
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
    typewriter(f'Stale dust and the smell of mold waft into your nose. Just as you\'re about to turn the corner, you hear:')
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
    typewriter(f'\nYou barely finish your {selected_consumable.capitalize()} when a {monster_b_obj.name} ambushes you!')
    typewriter(f'{monster_b_obj.description}')
    encounter(player_obj, monster_b_obj)

    # Upgrade items
    typewriter(f'\nYou realize the {monster_b_obj.name} was guarding a crate. Open it? (y/n)')
    open_crate = input('>>> ').lower().strip()

    if open_crate == 'y':
        # Pick armor
        typewriter('\nYou find:')
        display_items(armors_2_dict)
        typewriter('\nPick one.')
        selected_armor = input('>>> ').lower().strip()
        equip(player_obj, selected_armor, all_items_dict)

        # Pick weapon
        typewriter('\nRummaging further, you also see:')
        display_items(weapons_2_dict)
        typewriter('\nPick one.')
        selected_weapon = input('>>> ').lower().strip()
        equip(player_obj, selected_weapon, all_items_dict)
    
    # Rest
    typewriter('\nYou make your way to a staircase. A small shrine sits at the bottom.')
    typewriter('Pray at the shrine? (y/n)')
    rest = input('>>> ').lower().strip()

    if rest == 'y':
        player_obj.current_hp = player_obj.max_hp
        hp_bar = '#' * player.current_hp
        empty_bar = ' ' * (player.max_hp - player.current_hp)
        print(f'HP: {player.current_hp}/{player.max_hp} [' + f'{hp_bar}' + f'{empty_bar}' + ']')


    display_player_stats(player_obj)