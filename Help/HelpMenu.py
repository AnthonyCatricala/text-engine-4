

def help_move():
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

def help_use():
    use = "[use] [item]"
    desc = "\nUse the use command to use an item that is in the inventory of the player. Most items will be " +
    "consumable, meaning the item is removed from the players inventory on use but not all items will work " +
    "like that. An example would be an item such as a key being used to unlock a door."
    print(use)
    print(desc)

def help_get():
    use = "[get] [item]"
    desc = "\nUse the get command to put an item into your inventory. This command will not work for all items." +
    " An example would be using the get command on a bookcase and expecting it to be in your inventory."
    print(use)
    print(desc)

def help_examine():
    use = "[examine] [item]"
    desc = "\nuse the examine command to examine a specific item that is in the room the player is in. It will give the " +
    "user a more detailed description of the item that is being targeted."
    print(use)
    print(desc)
