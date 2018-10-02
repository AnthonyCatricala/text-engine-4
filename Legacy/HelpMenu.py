import sys


def help_move():
    move = [
        "Go",
        "Move",
        "Walk",
        "Run",
        "N",
        "S",
        "E",
        "W"
    ]

    compass_directions = [
        "North",
        "N",
        "South",
        "S",
        "East",
        "E",
        "West",
        "W",
    ]

    usage = "Usage: [move] [compass direction]"

    applicable_move_commands = "Applicable Move Commands: "
    applicable_move_commands += " ".join(move)
    applicable_compass_directions = "Applicable Compass Directions: "
    applicable_compass_directions += " ".join(compass_directions)

    desc = "Description: Follow up an applicable move command with a compass direction to " \
           "attempt to move into a new room.\n"

    print(usage)
    print(applicable_move_commands)
    print(applicable_compass_directions)
    print(desc)


def help_look():
    usage = "Usage: Look"
    desc = "Description: When you use the look command you will be given a " \
           "description of the room that you are in and what objects you can see.\n"

    print(usage)
    print(desc)


def help_pickup():
    usage = "Usage: Pickup [object]"
    desc = "Description: When you use the pickup command you will attempt to " \
           "pickup an object from the room and place it in the players inventory.\n"
    print(usage)
    print(desc)


def help_inventory():
    usage = "Usage: Inventory"
    desc = "Description: When you use the inventory command, you will be given a " \
           "description of items in your possession.\n"

    print(usage)
    print(desc)


def help_sleep_on():
    usage = "Usage: Sleep in/on [bed name]"
    desc = "Description: When you use the sleep in/on command, you will attempt to rest on the designated item.\n"

    print(usage)
    print(desc)


def help_examine():
    usage = "Usage: Examine [object]"
    desc = "When you use the examine command, you will take a closer look at a " \
           "specific item in the room or within your environment.\n"

    print(usage)
    print(desc)


def help_read():
    usage = "Usage: Read [object]"
    desc = "Description: When you use the read command, you will attempt to read " \
           "any writing on the object you specified.\n"

    print(usage)
    print(desc)


def help_take():
    usage = "Usage: Take [object]"
    desc = "Description: When you use the take command, you will attempt to pick up " \
           "the specific item and add it to your inventory.\n"

    print(usage)
    print(desc)


def help_drop():
    usage = "Usage: Drop [object]"
    desc = "Description: When you use the drop command, you will attempt to remove an " \
           "item from your inventory and leave it in the room you are in.\n"

    print(usage)
    print(desc)


def help_unlock_door():
    usage = "Usage: Unlock [compass direction] door with [key name]"
    desc = "Description: When you use the unlock command, you will attempt to unlock a " \
           "specified door. This command will only work if the key is in your inventory " \
           "or within the room you are currently in."

    print(usage)
    print(desc)


def help_open_door():
    usage = "Usage: Open [compass direction] door"
    desc = "Description: When you use the open command, you will attempt to open the " \
           "door in the direction specified. This command will not work if the door is locked.\n"

    print(usage)
    print(desc)


def help_kanye():
    print("I love you like kanye loves kanye")


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        print("If you need help using a command type 'help *command*.'")
    else:
        command_list = []
        for i in range(len(args)-1):
            command_list.append(args[i+1])
        help_with = " ".join(command_list)
        if help_with == "move" or help_with == "go" or help_with == "run" or help_with == "walk":
            help_move()
        elif help_with == "look":
            help_look()
        elif help_with == "pickup" or help_with == "pick up":
            help_pickup()
        elif help_with == "inventory":
            help_inventory()
        elif help_with == "sleep":
            help_sleep_on()
        elif help_with == "examine":
            help_examine()
        elif help_with == "read":
            help_read()
        elif help_with == "take":
            help_take()
        elif help_with == "drop":
            help_drop()
        elif help_with == "unlock door" or help_with == "unlock":
            help_unlock_door()
        elif help_with == "open door" or help_with == "open":
            help_open_door()
        elif help_with == "kanye":
            help_kanye()
