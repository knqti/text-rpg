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
