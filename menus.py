import sys
from utils import *


def title_screen():
    clear_screen()
    title_screen_selections()

def title_screen_selections():
    while True:
        print('\n')
        print('====================')
        print('Welcome to Text RPG!')
        print('====================')
        print('      - Play -      ')
        print('      - Help -      ')
        print('      - Quit -      ')        
        
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

def help_menu():
    title = '- HELP MENU -'
    page_width = (len(title) * 3)
    empty_padding = ' ' * (page_width // 3)

    print('\n')
    print('#' * page_width)
    print(empty_padding + title + empty_padding)
    print('\n== Commands ==')
    print('Whenever there is an input prompt, you can type the following commands.')
    print('- `help`: Displays this Help Menu')
    print('- `stats`: Displays your player stats')
    print('- `quit`: Exits the game')

    print('\n== Combat ==')
    print('At the beginning of combat, two twenty-sided dice ("2d20") are rolled for attack and defense.')
    print('\nResults of 12 or better are good. Results below 12 are bad.\n')
    print('Good attacks mean you hit the opponent and deal damage. Bad attacks mean you miss. Dishonor.')
    print('Good defenses mean the opponent miss their attack. Bad defenses mean you get ouchies.')

    print('\n== Weapons ==')
    print('Weapons modify your attack and damage stats.')

    print('\n== Armors ==')
    print('Armors modify your defense stat.')

    print('#' * page_width)

    input('\nPress enter to continue')

def display_player_stats(player:object):
    typewriter('\nDisplay your player stats? (y/n)')
    display_sheet = input('>>> ').lower().strip()
    
    if display_sheet == 'y':
        title = '- PLAYER STATS -'
        page_width = (len(title) * 3)
        empty_padding = ' ' * (page_width // 3)

        print('\n')
        print('#' * page_width)
        print(empty_padding + title + empty_padding)
        print(empty_padding + f'Name: {player.name}')
        print(empty_padding + f'Job: {player.job}')
        print(empty_padding + f'HP: {player.current_hp}/{player.max_hp}')
        print(empty_padding + f'Defense: {player.defense}')
        print(empty_padding + f'Attack: {player.attack}')
        print(empty_padding + f'Damage: {player.damage}')
        print(empty_padding + f'Head: {player.head}')
        print(empty_padding + f'Torso: {player.torso}')
        print(empty_padding + f'Hand 1: {player.hand_1}')
        print(empty_padding + f'Hand 2: {player.hand_2}')
        print(empty_padding + f'Legs: {player.legs}')
        print('#' * page_width)

        input('\nPress enter to continue')