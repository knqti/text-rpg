from game_play import room_1
from menus import player_setup, title_screen
from utils import typewriter, player_input


def game_loop():
    title_screen()
    Player_obj = player_setup()

    room_1(Player_obj)

if __name__ == '__main__':
    game_loop()