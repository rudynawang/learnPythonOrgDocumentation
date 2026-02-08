from draw import *

def play_game():
    return "Game started!"

def stop_game():
    return "Game Stopped!"

def main():
   start = play_game()
   draw_game(start)

   stop = stop_game()
   undraw_game(stop)


if __name__ == '__main__':
    main()