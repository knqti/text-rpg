from dictionaries import armors_1_dict, weapons_1_dict
from initialize import init_player
from player_actions import equip
from utils import clear_screen, display_items, player_input, typewriter


def player_setup():
    clear_screen()

    typewriter('\nWhat is your name?')
    input_name = input('>>> ').lower().strip()

    # Initialize the Player object
    Player_obj = init_player(name = input_name)

    # Pick armor
    typewriter('\nPick an armor.')
    armor_list = display_items(armors_1_dict)
    input_armor = player_input(Player_obj)

    while input_armor not in armor_list:
        print('Invalid choice. Try again.')
        input_armor = player_input(Player_obj)
    
    equip(Player_obj, input_armor, armors_1_dict)
    
    # Pick weapon
    typewriter('\nPick a weapon.')
    weapon_list = display_items(weapons_1_dict)
    input_weapon = player_input(Player_obj)
    
    while input_weapon not in weapon_list:
        print('Invalid choice. Try again.')
        input_weapon = player_input(Player_obj)
        
    equip(Player_obj, input_weapon, weapons_1_dict)

    typewriter(f'\n{Player_obj.name}, wearing a {input_armor.capitalize()} and wielding a {input_weapon.capitalize()}, begins their adventure...')
    return Player_obj
