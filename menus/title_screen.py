def title_screen_selections():
    while True:
        print('\n')
        print('====================')
        print('Welcome to Text RPG!')
        print('====================')
        print('      - Play -      ')
        print('      - Help -      ')
        print('      - Quit -      ')        
        
        option = input('>>> ').lower().strip()

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
