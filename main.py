# Libs


# Game libs
from face import Display as d
from terminal_cockpit import GameMonitor as gm
from terminal_cockpit import Texts as t
import messages as mess

def test():
    text = mess.game_start # "Here's an example of the glitch effect!"
    t.text_glitch_effect(text, 0.002, 0.001)

def game():
    d.clear()
    d.loading_screen_animation(5, 0.1, 2, 5)
    
    d.clear()
    main_menu = d.render_menu()
    if main_menu != 'q':
        t.intro(mess.game_start)
    else:
        pass

    d.clear()
    d.exiting_screen_animation(5, 0.1, 2, 5)
    d.clear()


if __name__ == "__main__":
    d.clear()
    test()
    #game()
else:
    print("Something went wrong...")
