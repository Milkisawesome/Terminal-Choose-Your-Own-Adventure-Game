import Main

##First two Choices
def cargo_hold():
    Main.text_speed("""Two things not meant to be opened

The cargo hold smells of coal and something sweeter, older. A steamer chest sits under a bare bulb, its latch already unclasped. Beside it, a door with no handle is painted over in flat black — except for four stenciled words: DO NOT OPEN. EVER.

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

##Cargo Hold choices

def chest_cargo():
    Main.text_speed("")

def door_cargo():
    Main.text_speed("")

