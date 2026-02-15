import time, os, random, sys
import messages as mess
import builder as b

# class Basics():
#     def text_speed(text, delay=0.1):
#             """Blinking text for the print"""
#             for char in text:
#                 sys.stdout.write(char)
#                 sys.stdout.flush()
#                 time.sleep(delay)

class Display():

    def loading_screen_animation(duration, delay, almost, secret_chance):
        """Animation when the game starts"""

        # Animation process
        frames = ["|", "/", "—", "\\"]
        end_time = time.time() + duration

        print(f">>> the system is starting... ", end=" ", flush=True)

        while time.time() < end_time:
            for frame in frames:
                print(f"\b{frame}", end="", flush=True)
                time.sleep(delay)
        print(f"\n>>> connection terminated", end="", flush=True)
        time.sleep(almost)

        # Secret message
        secret_message = random.randint(0, secret_chance)
        if secret_message == 0:
            print("\nYou think this is funny?")
        elif secret_message == 1:
            print("\nNo remorse.")
        elif secret_message == 2:
            print("\nTurn around.")
        time.sleep(0.05)

    def render_menu():
        """Loading the main menu of the game"""
        b.Build.build_table('ANORAB', b.Basics.items_main)
        move = ['s', 'c', 'q']
        cmd = b.Basics.command_line(move)
        return cmd

    def new_game_configuration():
        """Configure the game at the start"""
        b.Build.build_table('Configuration of the game', b.Basics.helpy_tip)
        time.sleep(0.5)
        generate_formula = input(">>> Write your game formula to start: ")
        return generate_formula


        

    def exiting_screen_animation(duration, delay, almost, secret_chance):
        """Animation when the game ends"""

        # Animation process
        frames = ["|", "/", "—", "\\"]
        end_time = time.time() + duration

        print(f">>> shutting down the servers... ", end=" ", flush=True)

        while time.time() < end_time:
            for frame in frames:
                print(f"\b{frame}", end="", flush=True)
                time.sleep(delay)
        print(f"\n>>> system deactivated", end="", flush=True)
        time.sleep(almost)

        # Secret message
        secret_message = random.randint(0, secret_chance)
        if secret_message == 0:
            print("\nYou will not survive.")
        elif secret_message == 1:
            print("\n«His own iniquities shall take the wicked himself, and he shall be holden with the cords of his sins»  5:22")
        elif secret_message == 2:
            print("\nThe Cost of Revenge is always highest.")
        time.sleep(0.2)

class GameMonitor():


    def generate_main_table(current_data, mailbox, news, statictics, end: bool):
        while end:
            pass
    


