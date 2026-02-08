import time, random, sys

from face import Display as d
global game_start

class Texts():
    def text_glitch_effect(text: str, glitch_speed: int, text_speed: int):
        """Generates a glitch effect when the text appears on the screen"""
        
        glitch_sprites = ['@', '#', '$', '%', '^', '&', '*', '+']  # 8 sprites total
        
        for step in text:

            glitch = random.choice(glitch_sprites)

            for glitch in glitch_sprites:
                print(f"\b{glitch}", end="", flush=True)
                time.sleep(glitch_speed)

            print(f"\b{step}", end=" ", flush=True)

            time.sleep(text_speed)

    def intro(lyric:list):
        d.clear()
        for _ in lyric:
            Texts.text_glitch_effect(_, 0.001, 0.001)
        time.sleep(3)
        input("\n>>> Press ENTER to continue: ")






class GameMonitor():
    """This class contains everything what imitates a terminal of the real 80s machine"""
    
    

    def screen_display():
        pass
