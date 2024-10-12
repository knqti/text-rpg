import sys
from utils import *


##### Title Screen
def title_screen():
    clear_screen()

    print('====================')
    print('Welcome to Text RPG!')
    print('====================')
    print('      - Play -      ')
    print('      - Help -      ')
    print('      - Quit -      ')

    title_screen_selections()

##### Title Screen Selections
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

##### Help Menu
def help_menu():
    print('\n=========')
    print('Help Menu')
    print('=========')
    print('- Helpful tip')
    print('- Helpful tip')
    print('- Helpful tip')