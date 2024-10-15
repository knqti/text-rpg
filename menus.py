import sys
from utils import *


# Title Screen
def title_screen():
    clear_screen()

    print('====================')
    print('Welcome to Text RPG!')
    print('====================')
    print('      - Play -      ')
    print('      - Help -      ')
    print('      - Quit -      ')

    title_screen_selections()

# Title Screen Selections
def title_screen_selections():
    while True:
        option = input('>>> ').lower()

        if option == 'play':
            return
        elif option == 'help':
            help_menu()
            continue
        elif option == 'quit':
            sys.exit()
        else:
            print('\nInvalid option.')
            print('Type `play`, `help`, or `quit` and press enter.')
            continue

# Help Menu
def help_menu():
    print('\n=========')
    print('Help Menu')
    print('=========')
    print('- Helpful tip')
    print('- Helpful tip')
    print('- Helpful tip')

# Player Stats
def show_player_sheet(player:object):
    title = 'player sheet'.upper()
    page_width = (len(title) * 3) + 2

    print('\n')
    print('#' * page_width)
    print(' ' * (page_width // 3 - 2) + f'- {title} -' + (' ' * (page_width // 3 - 2)))
    
    print(f'Name: {player.name}')
    print(f'Job: {player.job}')
    print(f'Max HP: {player.max_hp}')
    print(f'Current HP: {player.current_hp}')
    print(f'Defense: {player.defense}')
    print(f'Attack: {player.attack}')
    print(f'Damage: {player.damage}')
    print(f'Head: {player.head}')
    print(f'Torso: {player.torso}')
    print(f'Hand 1: {player.hand_1}')
    print(f'Hand 2: {player.hand_2}')
    print(f'Legs: {player.legs}')

    print('#' * page_width)