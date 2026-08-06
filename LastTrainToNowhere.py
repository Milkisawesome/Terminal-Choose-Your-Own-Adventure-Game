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
def get_choice(options):
        while True:
            choice = input("\nWhat do you want to do").strip().upper()
            if choice in options:
                return choice
            print("Invalid choice. Please try again.")


def game_menu():
    text_speed("---- THE LAST TRAIN TO NOWHERE ----")
    text_speed("[A] Start Game")
    text_speed("[B] Quit")

    choice = get_choice(['A', 'B'])
    if choice == 'A':
        start_game()
    else:
        text_speed("Quitting... Thank you for playing!")
        sys.exit()


def start_game():
    print("Welcome to Last Train To Nowhere")


if __name__ == "__main__":
    game_menu()