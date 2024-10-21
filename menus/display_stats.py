def display_player_stats(Player_obj:object):
    title = '- PLAYER STATS -'
    page_width = (len(title) * 3)
    empty_padding = ' ' * (page_width // 3)

    print('\n')
    print('#' * page_width)
    print(empty_padding + title + empty_padding)
    print(empty_padding + f'Name: {Player_obj.name}')
    # print(empty_padding + f'Job: {Player_obj.job}')
    print(empty_padding + f'HP: {Player_obj.current_hp}/{Player_obj.max_hp}')
    print(empty_padding + f'Defense: {Player_obj.defense}')
    print(empty_padding + f'Attack: {Player_obj.attack}')
    print(empty_padding + f'Damage: {Player_obj.damage}')
    print(empty_padding + f'Head: {Player_obj.head}')
    print(empty_padding + f'Torso: {Player_obj.torso}')
    print(empty_padding + f'Hand 1: {Player_obj.hand_1}')
    print(empty_padding + f'Hand 2: {Player_obj.hand_2}')
    print(empty_padding + f'Legs: {Player_obj.legs}')
    print('#' * page_width)

    input('\nPress enter to continue')