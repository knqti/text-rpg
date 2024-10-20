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
    
    for item in sorted_dict.keys():
        print(f'- {item.capitalize()}')

def display_ascii(file_name):
    directory_path = './assets/'
    file_suffix = '_standard.txt'
    full_file_path = directory_path + str(file_name) + file_suffix

    with open(full_file_path, 'r') as file:
        content = file.read()
        print(content)

# def create_room(room, rooms_dict:dict):
#     stats = rooms_dict[room]

#     room_obj = Room(
#         name=stats['name'],
#         monster_a=stats['monster_a'],
#         monster_b=stats['monster_b'],
#         monster_c=stats['monster_c'],
#         item_a=stats['item_a'],
#         item_b=stats['item_b'],
#         item_c=stats['item_c'],
#         description=stats['description']
#     )
#     return room_obj