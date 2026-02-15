# Game libs
import face as f
import messages as mess
import builder as b

def test():
    #text = mess.game_start  #"Here's an example of the glitch effect!"
    items = ["Start a New Game", "Continue", "Exit Game"]
    titel = "ANORAB System"
    #b.Build.build_table(titel, items)
    #f.Display.render_menu()
    #f.Display.new_game_configuration(1, '', '', 1)


def game():
    mess.clear()
    f.Display.loading_screen_animation(5, 0.1, 2, 5)
    #f.GameMonitor.generate_main_table()
    
    mess.clear()
    main_menu = f.Display.render_menu()
    if main_menu == 's':
        mess.clear()
        f.Display.new_game_configuration()
    elif main_menu == 'c':
        pass
    else:
        pass

    mess.clear()
    f.Display.exiting_screen_animation(5, 0.1, 2, 5)
    mess.clear()


if __name__ == "__main__":
    mess.clear()
    #test()
    game()
else:
    print("Something went wrong...")
