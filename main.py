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
typewriter(armors_1_dict[selected_armor]['description'])

# Pick weapon
typewriter('\nChoose your weapon.')
display_items(weapons_1_dict)
selected_weapon = input('>>> ')
equip(player_obj, selected_weapon, all_items_dict)
typewriter(weapons_1_dict[selected_weapon]['description'])

# Player sheet
display_player_sheet(player_obj)

# Narration
typewriter(f'\nAnd so {player_obj.name}, the {player_obj.job}, donning a {selected_armor.capitalize()} and wielding a {selected_weapon.capitalize()}, begin their adventure!')

# Some encounter
monster = random_monster()
monster_obj = create_monster(monster, monsters_1_dict)
typewriter(f'\nYou wander around when a {monster_obj.name} appears.')
typewriter(monster_obj.description)
encounter(player_obj, monster_obj)

# Eat something
typewriter('\nYou look around and find some stuff:')
display_items(consumables_1_dict)
typewriter('\nPick one to consume.')
selected_consumable = input('>>> ')
typewriter(f'\n{consumables_1_dict[selected_consumable]["description"]}')
consume_item(player_obj, selected_consumable, consumables_1_dict)
display_player_sheet(player_obj)


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