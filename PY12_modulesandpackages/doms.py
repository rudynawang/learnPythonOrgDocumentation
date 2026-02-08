import topi
print(topi.__file__)

def play_game():
    return "Game Started"

def main():
    result = play_game()
    topi.topi_game(result)
   

if __name__ == '__main__':
    main()