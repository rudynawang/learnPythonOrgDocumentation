# Module in python is the piece of software that has a specific functionality.
# In python, modules are the python files with a ".py" extension.
# Modules are imported 

import draw
print(draw.__file__)

def play_game():
    return "Game Started"

def main():
    result = play_game()
    draw.draw_game(result)
   

if __name__ == '__main__':
    main()