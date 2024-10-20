from classes import Player


def init_player(name, job):
    player_instance  =  Player(
        name = name,
        job = job,
        max_hp = 10,
        current_hp = 10,
        defense = 0,
        attack = 0,
        damage = 0,
        head = None,
        torso = None,
        hand_1 = None,
        hand_2 = None,
        legs = None
    )
    return player_instance
