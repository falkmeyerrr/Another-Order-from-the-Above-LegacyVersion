# Libs


# Game libs
from face import Display as d
from terminal_cockpit import Monitor as m

# def loading_screen_animation(duration, delay, almost):
#     """Animation when the game starts"""
#     frames = ["|", "/", "—", "\\"]
#     end_time = time.time() + duration  # 5 - Duration

#     print(f"the system is starting... ", end=" ", flush=True)

#     while time.time() < end_time:
#         for frame in frames:
#             print(f"\b{frame}", end="", flush=True)
#             time.sleep(delay)
#     print(f"\nconnection terminated", end="", flush=True)
#     time.sleep(almost)


def game():
    d.clear()
    d.loading_screen_animation(5, 0.1, 2)
    
    d.clear()
    d.render_menu()

    d.clear()
    d.exiting_screen_animation(5, 0.1, 2)
    d.clear()


if __name__ == "__main__":
    game()
else:
    print("Something went wrong...")
