import time, os, random, sys


def text_speed(text, delay=0.1):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)

class Display():
    clear = lambda: os.system("cls")


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
        items = ["Start a New Game", "Continue", "Exit Game"]
        title = "ANORAB System"

        max_len = max(len(title), max(len(i) for i in items))

        width = max_len + 2
        top = "┌" + "─" * width + "┐"
        mid = "│" + " " * width + "│"
        sep = "├" + "─" * width + "┤"
        bottom = "└" + "─" * width + "┘"

        text_speed("┌" + "─" * width + "┐\n", 0.008)
        text_speed("│" + title.center(width) + "│\n", 0.008)
        text_speed(sep + "\n", 0.008)

        for item in items:
            text_speed("│ " + item.ljust(max_len) + " │\n", 0.008)

        text_speed("└" + "─" * width + "┘\n", 0.008)


        commands = ['s', 'c', 'q']

        while True:
            sys.stdout.write("\r>>> ")
            time.sleep(0.5)
            sys.stdout.write("\r    ")
            time.sleep(0.5)
            
            sys.stdout.write("\r>>> ")
            cmd = input().strip().lower()
            
            if cmd in commands:
                break
            else:
                 print("Error: Start - S, Continue - C, Exit - Q")
                 continue
        return cmd

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
