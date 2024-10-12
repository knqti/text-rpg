import cmd
import textwrap
import sys
import os
import time
import random


screen_width = 100

########## Player setup
class player:
    def __init__(self):
        self.name = ''
        self.hp = 10
        self.player_class = ''
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False

my_player = player()

########## Title screen options
def title_screen_selections():
    while True:
        option = input('\n>>> ').lower()

        if option == 'play':
            setup_game()
        elif option == 'help':
            help_menu()
        elif option == 'quit':
            sys.exit()

        while option not in ['play', 'help', 'quit']:
            print('\nPlease enter a valid command.')
            break
    
        continue

########## Title screen
def title_screen():
    os.system('clear')

    print('####################')
    print('Welcome to Text RPG!')
    print('####################')
    print('      - Play -      ')
    print('      - Help -      ')
    print('      - Quit -      ')

    title_screen_selections()

########## Help menu
def help_menu():
    print('\n- Use up, down, left, right to move.')
    print('- Type your commands to do them.')
    print('- Use `examine` to inspect something.')
    print('- Good luck and have fun!')

    title_screen_selections()

########## Map
'''
----------
|a1|a2|a3|
|b1|b2|b3|
|c1|c2|c3|
----------
'''

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = ('up', 'north')
DOWN = ('down', 'south')
LEFT = ('left', 'west')
RIGHT = ('right', 'east')

solved_places = {
    'a1':False, 'a2':False, 'a3': False,
    'b1':False, 'b2':False, 'a4': False
}

zone_map = {
    'a1':{
        ZONENAME:'Town Market',
        DESCRIPTION:'description',
        EXAMINATION:'examine',
        SOLVED:False,
        UP:'void',
        DOWN:'b2',
        LEFT:'void',
        RIGHT:'a2'
    },
    'a2':{
        ZONENAME:'Town Entrance',
        DESCRIPTION:'description',
        EXAMINATION:'examine',
        SOLVED:False,
        UP:'void',
        DOWN:'b2',
        LEFT:'a1',
        RIGHT:'a3'
    },
    'a3':{
        ZONENAME:'Town Square',
        DESCRIPTION:'description',
        EXAMINATION:'examine',
        SOLVED:False,
        UP:'void',
        DOWN:'b3',
        LEFT:'a2',
        RIGHT:'void'
    },
    'b1':{
        ZONENAME:'West Forest Edge',
        DESCRIPTION:'description',
        EXAMINATION:'examine',
        SOLVED:False,
        UP:'a1',
        DOWN:'c1',
        LEFT:'void',
        RIGHT:'b2'
    },
    'b2':{
        ZONENAME:'Home',
        DESCRIPTION:'This is your home!',
        EXAMINATION:'Your home looks the same - nothing has changed.',
        SOLVED:False,
        UP:'a2',
        DOWN:'c2',
        LEFT:'b1',
        RIGHT:'b3'
    },
    'b3':{
        ZONENAME:'Shoreline',
        DESCRIPTION:'description',
        EXAMINATION:'examine',
        SOLVED:False,
        UP:'a3',
        DOWN:'c3',
        LEFT:'b2',
        RIGHT:'void'
    },
    'c1':{
        ZONENAME:'Forest',
        DESCRIPTION:'description',
        EXAMINATION:'examine',
        SOLVED:False,
        UP:'b1',
        DOWN:'void',
        LEFT:'void',
        RIGHT:'c2'
    },
    'c2':{
        ZONENAME:'South Forest Edge',
        DESCRIPTION:'This is your home!',
        EXAMINATION:'Your home looks the same - nothing has changed.',
        SOLVED:False,
        UP:'b2',
        DOWN:'void',
        LEFT:'c1',
        RIGHT:'c3'
    },
    'c3':{
        ZONENAME:'Ocean',
        DESCRIPTION:'description',
        EXAMINATION:'examine',
        SOLVED:False,
        UP:'b3',
        DOWN:'void',
        LEFT:'c2',
        RIGHT:'void'
    }    
}

########## Game interactivity
def print_location():
    current_location_name = zone_map[my_player.location][ZONENAME]
    current_location_desc = zone_map[my_player.location][DESCRIPTION]

    print('\n' + ('#' * len(current_location_desc)))
    print('#' + current_location_name + '#')
    print('#' + current_location_desc + '#')
    print('\n' + ('#' * len(current_location_desc)))

def prompt():
    while True:
        print('\nWhat would you like to do?')
        action = input('>>> ').lower()

        movement_actions = ['move', 'go', 'travel', 'walk']
        examine_actions = ['examine', 'inspect', 'interact']
        look_actions = ['look', 'look around']

        if action not in movement_actions and action not in examine_actions and action not in look_actions:
            print('\nPlease enter a valid command.')
                
        if action == 'quit':
            title_screen()    

        elif action in movement_actions:
            player_move()

        elif action in examine_actions:
            player_examine(action)
            
        elif action in look_actions:
            player_look()
       
def player_move():
    print('\nWhich direction?')
    direction = input('>>> ').lower()

    if direction in UP:
        destination = zone_map[my_player.location][UP]
        movement_handler(destination)
    elif direction in DOWN:
        destination = zone_map[my_player.location][DOWN]
        movement_handler(destination)
    elif direction in LEFT:
        destination = zone_map[my_player.location][LEFT]
        movement_handler(destination)
    elif direction in RIGHT:
        destination = zone_map[my_player.location][RIGHT]
        movement_handler(destination)        

def movement_handler(zone_id):
    print(f'\nYou have moved to {zone_map[zone_id][ZONENAME]}.')
    my_player.location = zone_id

def player_look():
    print('\nYou examine the surroundings.')
    print(zone_map[my_player.location][DESCRIPTION])

def player_examine(action):
    print('trigger puzzle here')

########## Game setup
def setup_game():
    os.system('clear')

    question_name = 'Hello, what is your name?'
    for letter in question_name:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)

    player_name = input('\n>>> ')
    my_player.name = player_name

    print(f'\nOk then, {player_name}, your adventure awaits!')

    main_game()

########## Main game loop
def main_game():
    while my_player.game_over == False:
        prompt()


title_screen()