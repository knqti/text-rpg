from game_play import room_1, room_2
from menus import player_setup, title_screen
from utils import display_ascii, player_input, typewriter


def game_loop():
    while True:
        title_screen()
        Player_obj = player_setup()

        # Room 1
        while Player_obj.game_over == False:
            room_1(Player_obj)
            break
        
        # Room 2
        while Player_obj.game_over == False:        
            room_2(Player_obj)
            break

        if Player_obj.game_over == True:
            display_ascii('game_over', '_standard.txt')
        else:
            typewriter(f'\n{Player_obj.name} emerges triumphant from the dungeon!')
            display_ascii('you_win', '_standard.txt')

        print('\nType `restart` to play again, `stats` for your final stats, or `quit` to end.')
        player_input(Player_obj, ['restart', 'stats', 'quit'])

if __name__ == '__main__':
    game_loop()