import os
import platform
import sys
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
        time.sleep(0.05)
    print(flush=False)

def display_items(dictionary:dict):
    sorted_dict = dict(sorted(dictionary.items()))
    displayed_list = []

    for item in sorted_dict.keys():
        print(f'- {item.title()}')
        displayed_list.append(item)
    
    return displayed_list

def display_ascii(file_name, file_suffix):
    # If running in a PyInstaller bundle
    if getattr(sys, '_MEIPASS', False):
        # Set the path to the temporary folder where PyInstaller extracts assets
        directory_path = os.path.join(sys._MEIPASS, 'assets')
    else:
        # Use the local assets folder when running as a normal Python script
        directory_path = './assets/'
    
    full_file_path = os.path.join(directory_path, str(file_name) + file_suffix)

    with open(full_file_path, 'r') as file:
        content = file.read()
    print(content)

def player_input(Player_obj:object, acceptable_list:list):
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
        elif player_typed == 'restart':
            return
        elif player_typed not in acceptable_list:
            print('\nInvalid command. Try again.\n')
            continue
        
        break

    return player_typed
