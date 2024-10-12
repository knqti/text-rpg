import os
import time
from classes import *
from menus import *
from utils import *


def player_setup():
    player_obj = Player()
    clear_screen()

    question_name = '\nWhat is your name?\n'
    typewriter(question_name)
    input_name = input('>>> ')
    player_obj.name = input_name

    question_job = '\nWhat is your job?\n'
    typewriter(question_job)
    print('Select `warrior`, `cleric`, or `mage`.')
    input_job = input('>>> ').capitalize()
    player_obj.job = input_job

    print(f'\nHello, {player_obj.name} the {player_obj.job}!')

title_screen()
player_setup()
