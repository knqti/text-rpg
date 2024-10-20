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