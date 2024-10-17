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