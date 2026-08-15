import Main
import sys

##First two Choices
def cargo_hold():
    Main.text_speed("""
The cargo hold smells of coal and something sweeter, older. A steamer chest sits under a bare bulb, its latch already unclasped. 
Beside it, a door with no handle is painted over in flat black — except for four stenciled words: DO NOT OPEN. EVER.

Curiosity, or something like it, pulls at you from both directions.""")

    Main.text_speed("[A] Open the chest")
    Main.text_speed("[B] Open the door")

    choice = Main.get_choice(['A', 'B'])

    if choice == 'A':
        chest_cargo()
    elif choice == 'B':
        door_cargo()


def dining_car():
    Main.text_speed("")
##--------------------------------------------------------------------
##Cargo Hold choices

def chest_cargo():
    Main.text_speed("""
Inside the chest: a brass lantern, unlit, and a photograph gone soft with age. It shows the engine room — and someone standing at the controls, cap low, coat too long. 
The face is turned half away, but you know, with the sick certainty of dreams, that it is yours.

The lantern is warm in your hand, as if it had been waiting.""")

    Main.text_Speed("[A] Take the lantern to the engine room")
    Main.text_speed("[B] Put the stuff down and head to the cargo door instead")

    choice = Main.get_choice(['A', 'B'])
    if choice == 'A':
        end_conductor()
    else:
        door_cargo()


def door_cargo():
    Main.text_speed("""
    The black paint flakes away under your fingers. 
    Behind it: a small brass lever in a glass case, and beneath it, engraved — EMERGENCY. The train doesn't feel like it's slowing down.
    It doesn't feel like anything is an emergency about this at all — except that it is the only door on this train that leads somewhere you haven't already been.
    """)
    Main.text_speed("[A] Pull the lever")
    Main.text_speed("[B] Reconsider and go check out the chest")

    choice = Main.get_choice(['A', 'B'])
    if choice == 'A':


#---------------------------------------------------------------------------
##Game End Scenarios

def end_conductor():
    Main.text_speed("""The old conductor is gone — was never really there, was only ever the shape you hadn't grown into yet. Someone has to keep this train running for the next person who wakes up in Car No. 4, not remembering how they got on.

You light the lantern. You take the long coat off its hook.""")
    Main.text_speed("""--- THE END ---""")

    Main.text_speed("[A] Restart")
    Main.text_speed("[B] Quit")

    choice = Main.get_choice(['A', 'B'])
    if choice == 'A':
        Main.start_game()
    else:
        sys.exit()

def end_loop():


def end_rails():


def end_stop():