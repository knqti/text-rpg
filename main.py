from combat import *
from items import *
from menus import *
from player import *


title_screen()
player_obj = player_setup()

# Pick armor
typewriter('\nPick a piece of armor.\n')
display_items(armors_1_dict)
selected_armor = input('>>> ')
equip(player_obj, selected_armor, all_items_dict)

# Pick weapon
typewriter('\nChoose your weapon.')
display_items(weapons_1_dict)
selected_weapon = input('>>> ')
equip(player_obj, selected_weapon, all_items_dict)

# Player sheet
typewriter('\nDisplay your player sheet? (Yes/No)')
display_sheet = input('>>> ').lower().strip()
if display_sheet == 'yes':
    show_player_sheet(player_obj)
    input('\nPress enter to continue')

# Narration
typewriter(f'\nAnd so {player_obj.name}, the {player_obj.job}, clothed in a {selected_armor.capitalize()} and wielding a {selected_weapon.capitalize()}, set out on their adventure!')

# Some encounter
while True:
    monster = random_monster()
    monster_obj = create_monster(monster, monsters_dict)
    typewriter(f'\nYou wander around when a {monster_obj.name} appears.')

    encounter(player_obj, monster_obj)

    print('\nContinue? (y/n)')
    user_input = input('>>> ')
    if user_input == 'n':
        break

    # results_dict = fight(player_obj, monster_obj)

    # if results_dict['defense result'] == 'fail':
    #     typewriter(f'\nIt hit you, ouch...')
    #     print(f'Received {results_dict['receive damage']} of damage.')
    #     hp_bar = '#' * player_obj.current_hp
    #     empty_bar = ' ' * (player_obj.max_hp - player_obj.current_hp)
    #     print(f'HP: {player_obj.current_hp}/{player_obj.max_hp}')
    #     print(f'{player_obj.current_hp}/{player_obj.max_hp} [' + f'{hp_bar}' + f'{empty_bar}' + ']')
        
    #     if player_obj.current_hp <= 0:
    #         typewriter('\nYou died :(')
    #         break

    #     print('\nContinue? (y/n)')
    #     user_input = input('>>> ')
    #     if user_input == 'n':
    #         break
    # else:
    #     typewriter('\nYou escaped, phew...')
    #     print('\nContinue? (y/n)')
    #     user_input = input('>>> ')
    #     if user_input == 'n':
    #         break