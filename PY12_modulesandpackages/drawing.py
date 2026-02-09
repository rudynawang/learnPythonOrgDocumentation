class Screen:
    def __init__(self):
        print("Screen initialized")

    def clear(self):
        print("Screen Cleared")

    def drawing(self):
        print("Drawing game objects")


def clearing_screen(screen):
    screen.clear()

def drawing_game():
    clearing_screen(main_screen)
    main_screen.drawing()

main_screen = Screen()

