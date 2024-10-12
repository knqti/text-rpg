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

def typewriter(prompt):
    for letter in prompt:
        print(letter, end='', flush=True)
        time.sleep(0.03)