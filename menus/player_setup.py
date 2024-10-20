from initialize import init_player
from utils import clear_screen, typewriter


def player_setup():
    clear_screen()

    typewriter('\nWhat is your name?')
    input_name = input('>>> ').strip()

    typewriter('\nWhat is your job?')
    input_job = input('>>> ').capitalize().strip()

    # Initialize the Player object
    Player_obj = init_player(input_name, input_job)
    return Player_obj
