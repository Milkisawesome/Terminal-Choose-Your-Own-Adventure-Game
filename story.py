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
    Main.text_speed("""
    The dining car is set for a meal no one is eating. At the far table sits a conductor in a coat too long for him, his face lost beneath the brim of his cap. He slides a blank ticket across the table and taps it once.

"Where were you going," he says, "before you got on my train?"

You feel the true answer rise in your throat — and, right behind it, a much easier lie.
""")

    Main.text_speed("[A] Tell him the truth")
    Main.text_speed("[B] Make something up")

    choice = Main.get_choice(['A', 'B'])
    if choice == 'A':
        end_stop()
    else:
        diningcar_lie()


##--------------------------------------------------------------------
##Cargo Hold choices

def chest_cargo():
    Main.text_speed("""
Inside the chest: a brass lantern, unlit, and a photograph gone soft with age. It shows the engine room — and someone standing at the controls, cap low, coat too long. 
The face is turned half away, but you know, with the sick certainty of dreams, that it is yours.

The lantern is warm in your hand, as if it had been waiting.""")

    Main.text_speed("[A] Take the lantern to the engine room")
    Main.text_speed("[B] Put the stuff down and head to the cargo hold")

    choice = Main.get_choice(['A', 'B'])
    if choice == 'A':
        end_conductor()
    else:
        cargo_hold()


def door_cargo():
    Main.text_speed("""
    The black paint flakes away under your fingers. 
    Behind it: a small brass lever in a glass case, and beneath it, engraved — EMERGENCY. The train doesn't feel like it's slowing down.
    It doesn't feel like anything is an emergency about this at all — except that it is the only door on this train that leads somewhere you haven't already been.
    """)
    Main.text_speed("[A] Pull the lever")
    Main.text_speed("[B] Reconsider and go check to the cargo hold")

    choice = Main.get_choice(['A', 'B'])
    if choice == 'A':
        end_rails()
    else:
        cargo_hold()

##-----------------------------------------------------------------------------------
##dining car scenario

def diningcar_lie():
    Main.text_speed("""The lie leaves your mouth and the train answers it.
     The lanterns gutter. The floor tilts, just slightly, like something underneath has shrugged. 
     The conductor doesn't move, doesn't blink — just watches you with the patience of a man who has heard ten thousand lies exactly like yours.
    
You could run for the back of the train while the lights are still low, or stay very still and wait for whatever happens next.""")

    Main.text_speed("[A] Run for the back of the train")
    Main.text_speed("[B] Stay still and wait")

    choice = Main.get_choice(['A', 'B'])
    if choice == 'A':
        cargo_hold()
    else:
        end_loop()



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
    Main.text_speed("""
    Nothing happens, which is worse than anything happening

The train doesn't stop. The window doesn't lighten.
Somewhere behind you — or maybe ahead of you — a door you don't remember opens onto Car No. 4, empty, waiting, the same brass plate on the wall.
    """)

    Main.text_speed("[A] Restart")
    Main.text_speed("[B] Quit")

    choice = Main.get_choice(['A', 'B'])
    if choice == 'A':
        Main.start_game()
    else:
        sys.exit()


def end_rails():
    Main.text_speed("""
     The whole train screams

The lever comes down harder than you expect, and the whole train screams — metal, brakes, the sound of a decision being made whether it wants to be or not. 
When it finally stops, the black windows have gone green with morning, and the door hangs open on a field you don't recognize, in a country you can't name.

It isn't the platform you were promised. It's better, or it's worse — but it's yours to walk into.
    """)

    Main.text_speed("[A] Restart")
    Main.text_speed("[B] Quit")

    choice = Main.get_choice(['A', 'B'])
    if choice == 'A':
        Main.start_game()
    else:
        sys.exit()

def end_stop():
    Main.text_speed("""The truth costs you nothing you didn't already owe

The conductor's mouth — you can see it now, beneath the brim — curls into something almost kind. 
He punches the ticket once, hands it back, and the far doors of the dining car slide open onto a platform lit gold with ordinary morning.

You don't look back at the train. You've heard that's how you stay gotten-off.
    """)

    Main.text_speed("[A] Restart")
    Main.text_speed("[B] Quit")

    choice = Main.get_choice(['A', 'B'])
    if choice == 'A':
        Main.start_game()
    else:
        sys.exit()
