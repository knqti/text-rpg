from .fight import fight
from .roll_initiative import roll_initiative


def encounter(player:object, monster:object):
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
    roll_initiative(combat_results_dict, monster)
    fight(player, monster, combat_results_dict)
