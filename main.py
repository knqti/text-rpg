from combat import *
from menus import *
from player import *



title_screen()

player_obj = player_setup()

# for attr, value in vars(player_obj).items():
#     print(f'{attr}: {value}')

# some encounter
monster = random_monster()
monster_obj = create_monster(monster, monsters_dict)
print(f'\nA {monster_obj.name} appeared')

results = fight(player_obj, monster_obj)

if results['defense result'] == 'fail':
    print(f'Your HP is {player_obj.current_hp}')
    print(f'You took {results['receive damage']} damage')
    hp_bar = '#' * player_obj.current_hp
    empty_bar = ' ' * (player_obj.max_hp - player_obj.current_hp)
    print(f'HP: {player_obj.current_hp}/{player_obj.max_hp} [' + f'{hp_bar}' + f'{empty_bar}' + ']')
else:
    print('nothing happened')