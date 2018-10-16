import sys

def help_main():
    move = [
            "Go"
            "go"
            "Move"
            "move"
            "Walk"
            "walk"
            "Run"
            "run"
    ]
    direction = [
        "N"
        "n"
        "North"
        "north"
        "S"
        "s"
        "South"
        "south"
        "E"
        "e"
        "East"
        "east"
        "W"
        "w"
        "West"
        "west"
    ]
    use = "[move] [direction]"
    usable_move = " ".join(move)
    usable_direction = " ".join(direction)
    desc = "\nUse one of the move commands and follow it up with a compass direction to attempt " +
    "to move to a new room in the chosen direction. For example, typing 'move north' will move you " +
    "to the room north of you, if possible."
    print(use)
    print(usable_move)
    print(usable_direction)
    print(desc)

def help_look():
    use = "look"
    desc = "\nUse the look command to look at the surroundings of the room you are in as well as its contents.\n"
    print(use)
    print(desc)
    