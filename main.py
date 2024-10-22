from game_play import room_1, room_2
from menus import player_setup, title_screen


def game_loop():
    title_screen()
    Player_obj = player_setup()

    room_1(Player_obj)
    room_2(Player_obj)

if __name__ == '__main__':
    game_loop()