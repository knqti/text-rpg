import os
import platform
import time


def clear_screen():
    if platform.system() == 'Windows':
        # Windows system
        os.system('cls')
    else:
        # Unix system
        os.system('clear')

def typewriter(prompt:str):
    for letter in prompt:
        print(letter, end='', flush=True)
        time.sleep(0.03)
    print(flush=False)

def display_items(dictionary:dict):
    sorted_dict = dict(sorted(dictionary.items()))
    displayed_list = []

    for item in sorted_dict.keys():
        print(f'- {item.capitalize()}')
        displayed_list.append(item)
    
    return displayed_list

def display_ascii(file_name):
    directory_path = './assets/'
    file_suffix = '_standard.txt'
    full_file_path = directory_path + str(file_name) + file_suffix

    with open(full_file_path, 'r') as file:
        content = file.read()
        print(content)

def player_input(Player_obj:object):
    from menus import help_menu, quit_game, display_player_stats

    while True:
        player_typed = input('>>> ').lower().strip()

        if player_typed == 'help':
            help_menu()
            continue
        elif player_typed == 'quit':
            quit_game()
        elif player_typed == 'stats':
            display_player_stats(Player_obj)
            continue
        
        break

    return player_typed
