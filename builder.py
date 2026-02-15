import sys, time


class Basics():
    title_main = 'ANORAB System'
    items_main = ['Start a New Game', 'Continue', 'Exit Game']

    helpy_tip = ['Use command line to configure, wanna look for an example?']

    ideologies = ["Anarchy", "Rebelians", 'Democracy',
                  'Fascism', 'Communism', 'Liberalism',
                  'Theocracy', 'Military Group']

    def text_speed(text, delay=0.1):
            """Blinking text for the print"""
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
    
    def command_line(commands:list):
        while True:
            for _ in range(2):
                sys.stdout.write("\r>>> ")
                time.sleep(0.2)
                sys.stdout.write("\r    ")
                time.sleep(0.2)

            sys.stdout.write("\r>>> ")
            cmd = input().strip().lower()
            
            if cmd in commands:
                break
            else:
                print("Error")
                continue
        return cmd

class Build():
    def build_table(title: str, items: list):
        """Function to build every basic table"""
        max_len = max(len(title), max(len(i) for i in items))

        width = max_len + 2
        top = "┌" + "─" * width + "┐"
        mid = "│" + " " * width + "│"
        sep = "├" + "─" * width + "┤"
        bottom = "└" + "─" * width + "┘"
        
        Basics.text_speed("┌" + "─" * width + "┐\n", 0.008)
        Basics.text_speed("│" + title.center(width) + "│\n", 0.008)
        Basics.text_speed(sep + "\n", 0.008)

        for item in items:
            Basics.text_speed("│ " + item.ljust(max_len) + " │\n", 0.008)

        Basics.text_speed("└" + "─" * width + "┘\n", 0.008)
