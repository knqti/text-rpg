from combat import *
from menus import *
from player import *


title_screen()
player_obj = player_setup()

# get items
typewriter('\nPick a piece of armor.')
print('Select `armor (leather)`, `helmet (steel)`, or `shield`')
selected_armor = input('>>> ')
equip(player_obj, selected_armor, all_items_dict)
typewriter(f'\n{selected_armor.capitalize()} equipped!')

typewriter('\nChoose your weapon.')
print('Select `club`, `staff`, or `sword`')
selected_weapon = input('>>> ')
equip(player_obj, selected_weapon, all_items_dict)
typewriter(f'\n{selected_weapon.capitalize()} equipped!')


# some encounter

while True:
    monster = random_monster()
    monster_obj = create_monster(monster, monsters_dict)
    typewriter(f'\nYou wander around when a {monster_obj.name} appears.')

    results_dict = fight(player_obj, monster_obj)

    if results_dict['defense result'] == 'fail':
        typewriter(f'\nIt hit you, ouch...')
        print(f'Received {results_dict['receive damage']} of damage.')
        hp_bar = '#' * player_obj.current_hp
        empty_bar = ' ' * (player_obj.max_hp - player_obj.current_hp)
        print(f'HP: {player_obj.current_hp}/{player_obj.max_hp}')
        print(f'{player_obj.current_hp}/{player_obj.max_hp} [' + f'{hp_bar}' + f'{empty_bar}' + ']')
        
        if player_obj.current_hp <= 0:
            typewriter('\nYou died :(')
            break

        print('\nContinue? (y/n)')
        user_input = input('>>> ')
        if user_input == 'n':
            break
    else:
        typewriter('\nYou escaped, phew...')
        print('\nContinue? (y/n)')
        user_input = input('>>> ')
        if user_input == 'n':
            break