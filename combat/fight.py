from random import randint as roll
from utils import player_input, typewriter
from .roll_combat import roll_combat
from .turns import turn_order


def fight(Player_obj:object, Monster_obj:object, combat_results_dict:dict):       
    death_occurred = False
    
    while death_occurred is False:
        print('\nWhat do you want to do?')
        print('   -  Attack  -   ')
        print('   -   Run    -   ')
        
        option = player_input(Player_obj)

        if option == 'attack':
            roll_combat(Player_obj, Monster_obj, combat_results_dict)
        elif option == 'run':
            run_away = roll(0, 1)
            
            if run_away == 0:
                typewriter('\nYou failed to run away. Slowpoke.')
                roll_combat(Player_obj, Monster_obj, combat_results_dict)
            elif run_away == 1:
                typewriter('\nYou escaped, phew.')
                return
            
        who_goes_first = combat_results_dict['goes first']
        death_occurred = turn_order(who_goes_first, Player_obj, Monster_obj, combat_results_dict)
