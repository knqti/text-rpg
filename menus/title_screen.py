from menus import help_menu, quit_game
from utils import display_ascii


def title_screen():
    while True:        
        print('####################')
        print('#     TEXT RPG     #')
        print('####################')
        print('      - Play -      ')
        print('      - Help -      ')
        print('      - Quit -      ')        
        
        option = input('\nType here >>> ').lower().strip()

        if option == 'play':
            return
        elif option == 'help':
            help_menu()
        elif option == 'quit':
            quit_game()
        else:
            print('\nInvalid option.')
            print('Type `play`, `help`, or `quit` and press enter.')
