from utils import player_input
from menus import help_menu, quit_game


def title_screen():
    while True:
        print('\n')
        print('====================')
        print('Welcome to Text RPG!')
        print('====================')
        print('      - Play -      ')
        print('      - Help -      ')
        print('      - Quit -      ')        
        
        option = input('\n>>> ')

        if option == 'play':
            return
        elif option == 'help':
            help_menu()
        elif option == 'quit':
            quit_game()
        else:
            print('\nInvalid option.')
            print('Type `play`, `help`, or `quit` and press enter.')
