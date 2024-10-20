from utils import typewriter
from .roll_combat import roll_combat
from .turns import turn_order


def fight(player:object, monster:object, combat_results_dict:dict):       
    death_occurred = False
    
    while death_occurred is False:
        print('\nWhat do you want to do?')
        print('   -  Attack  -   ')
        print('   -   Run    -   ')
        player_input = input('>>> ').lower().strip()

        if player_input == 'attack':
            roll_combat(player, monster, combat_results_dict)
        elif player_input == 'run':
            typewriter('\nYou escaped, phew.')
            return
        
        who_goes_first = combat_results_dict['goes first']
        death_occurred = turn_order(who_goes_first, player, monster, combat_results_dict)
