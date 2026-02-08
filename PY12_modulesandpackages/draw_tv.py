choice = input("Enter the mode you want ['y' for visual mode and 'n' for textual mode] :")

visual_mode = (choice.lower() == "y")

if visual_mode:
    import draw_visual as draw
else:
    import draw_textual as draw


def drawn_game():
    return "Game Drawn!"

def main():
    arg = drawn_game()

    draw.draw_game(arg)


if __name__ == '__main__':
    main()

