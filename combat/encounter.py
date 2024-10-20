from .fight import fight
from .roll_initiative import roll_initiative


def encounter(Player_obj:object, Monster_obj:object):
    combat_results_dict = {
        'goes first': None,
        'attack roll': None,
        'attack result': None,
        'attack damage': None,
        'defense roll': None,
        'defense result': None,
        'receive damage': None,
        'who died': None
    }
    roll_initiative(combat_results_dict, Monster_obj)
    fight(Player_obj, Monster_obj, combat_results_dict)
