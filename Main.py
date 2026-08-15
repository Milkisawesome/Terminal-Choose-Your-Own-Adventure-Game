import sys
import time
import story


##Typewriter Effect
def text_speed(text,delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

##Gets choices and validates the users input
def get_choice(options):
        while True:
            choice = input("\nWhat do you want to do: ").strip().upper()
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
   text_speed('''\nYou wake to the clatter of wheels

The car is empty, the windows black with a night that has no stars in it. 
A brass plate by the door reads CAR NO. 4. You don't remember boarding. 
You don't remember why you're afraid to ask why.

Two aisles lead away from you: one toward the front of the train, where a lantern swings behind frosted glass, and one toward the back, where the corridor narrows into shadow''')
   text_speed("[A] Head Towards the lantern, at the front")
   text_speed("[B] Head into the shadow, at the back")

   choice = get_choice(['A', 'B'])
   if choice == 'A':
       story.dining_car()
   elif choice == 'B':
       story.cargo_hold()



if __name__ == "__main__":
    game_menu()