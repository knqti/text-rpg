from combat import encounter, random_monster
from dictionaries import all_weapons_dict, all_armors_dict, monsters_1_dict
from initialize import init_monster
from menus import player_setup, title_screen
from player_actions import equip
from utils import player_input, typewriter


def game_loop():
    title_screen()

    Player_obj = player_setup()
    weapon = 'shiv'
    armor = 'hoodie'

    equip(Player_obj, weapon, all_weapons_dict)
    equip(Player_obj, armor, all_armors_dict)

    monster = random_monster(monsters_1_dict)
    Monster_obj = init_monster(monster, monsters_1_dict)

    #encounter(Player_obj, Monster_obj)
    typewriter('select a weapon: ')
    new_weapon = player_input(Player_obj)
    equip(Player_obj, new_weapon, all_weapons_dict)
    typewriter('now what?')
    player_input(Player_obj)

    # **NEED TO FIGURE OUT player_input() "LISTENING" LOOP**

game_loop()