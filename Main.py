import sys
import time
import numpy as np
import story

##Sound Setup

##Ensures app runs with or without sound
try:
    import pygame
    pygame.mixer.init()
    SOUND_ENABLED = True
except Exception as e:
    SOUND_ENABLED = False

def make_click_sound():
    sample_rate = 44100
    duration = 0.03 #30ms is short so to not overlapt at high typing speed
    frequency = 900

    t = np.linspace(0,duration,int(duration*sample_rate), False)
    wave = np.sin(frequency * t * 2 * np.pi)
    envelope = np.exp(-t * 45)
    wave = envelope * wave

    audio = (wave * 32767).astype(np.int16)
    stereo = np.column_stack((audio, audio))
    return pygame.sndarray.make_sound(stereo)

click_sound = make_click_sound() if SOUND_ENABLED else None

##Plays typewriter click sound effect once per character
def play_key_sound():
    if SOUND_ENABLED and click_sound is not None:
        try: click_sound.play()
        except Exception:
            pass

##Typewriter Effect
def text_speed(text,delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if not char.isspace():
            play_key_sound()
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



if __name__ == '__main__':
    game_menu()