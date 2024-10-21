from combat import encounter, random_monster
from dictionaries import all_items_dict, armors_2_dict, consumables_1_dict, monsters_1_dict, weapons_2_dict
from initialize import init_monster
from player_actions import consume_item, equip
from utils import display_items, typewriter, player_input


def room_1(Player_obj:object):
    # Encounter A
    monster_a = random_monster(monsters_1_dict)
    Monster_obj = init_monster(monster_a, monsters_1_dict)

    typewriter(f'\nYou walk into a dimly-lit dungeon.')
    typewriter(f'Stale dust and the smell of mold waft into your nose. Just as you\'re about to turn the corner, you hear:')
    typewriter(f'{Monster_obj.description}')
    typewriter(f'\nA {Monster_obj.name} appeared!')
    
    combat_results_dict = encounter(Player_obj, Monster_obj)

    # Loot
    if combat_results_dict['gets loot']:
        typewriter(f'\nSome items drop from the {Monster_obj.name}\'s lifeless form.')
        display_items(consumables_1_dict)

        typewriter('\nPick one to consume.')
        item_to_eat = player_input(Player_obj)

        typewriter(f'\n{consumables_1_dict[item_to_eat]["description"]}')
        consume_item(Player_obj, item_to_eat, consumables_1_dict)

    # Encounter B
    monster_b = monster_a
    while monster_b == monster_a:
        monster_b = random_monster(monsters_1_dict)
    
    Monster_obj = init_monster(monster_b, monsters_1_dict)

    typewriter(f'\nYou barely finish your last battle when a {Monster_obj.name} ambushes you!')
    typewriter(f'{Monster_obj.description}')
    
    encounter(Player_obj, Monster_obj)

    # Upgrade items
    typewriter(f'\nYou realize the {Monster_obj.name} was guarding a crate. You open it and find:')

    # Pick armor
    display_items(armors_2_dict)
    typewriter('\nPick one.')
    selected_armor = player_input(Player_obj)
    equip(Player_obj, selected_armor, all_items_dict)

    # Pick weapon
    typewriter('\nRummaging further, you also see:')
    display_items(weapons_2_dict)
    typewriter('\nPick one.')
    selected_weapon = player_input(Player_obj)
    equip(Player_obj, selected_weapon, all_items_dict)
    
    # Rest
    typewriter('\nYou make your way to a staircase. A small shrine sits at the bottom.')
    typewriter('Take a short rest? (y/n)')
    rest_choice = player_input(Player_obj)

    if rest_choice == 'y':
        Player_obj.current_hp = Player_obj.max_hp
        hp_bar = '#' * Player_obj.current_hp
        empty_bar = ' ' * (Player_obj.max_hp - Player_obj.current_hp)
        print(f'HP: {Player_obj.current_hp}/{Player_obj.max_hp} [' + f'{hp_bar}' + f'{empty_bar}' + ']')

