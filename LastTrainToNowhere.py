import sys
import time


##Typewriter Effect
def text_speed(text,delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
        print()

##Gets choices and validates the users input
    def get_choice(option):
        while True
            choice = input("/What do you want to do").strip().lower()
            if choice in option:
                return choice
            print("Invalid choice. Please try again.")


def game_start)():
