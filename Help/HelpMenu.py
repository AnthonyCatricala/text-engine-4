
class HelpMenu:

    @staticmethod
    def help():
        return "Please enter a command after help for further assistance with specific commands"

    @staticmethod
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
        desc = """\nUse one of the move commands and follow it up with a compass direction to attempt 
        to move to a new room in the chosen direction. For example, typing 'move north' will move you 
        to the room north of you, if possible."""
        return use, usable_move, usable_direction, desc

    @staticmethod
    def help_look():
        use = "look"
        desc = "\nUse the look command to look at the surroundings of the room you are in as well as its contents.\n"
        return use, desc

    @staticmethod
    def help_use():
        use = "[use] [item]"
        desc = """\nUse the use command to use an item that is in the inventory of the player. Most items will be 
        consumable, meaning the item is removed from the players inventory on use but not all items will work 
        like that. An example would be an item such as a key being used to unlock a door."""
        return use, desc

    @staticmethod
    def help_get():
        use = "[get] [item]"
        desc = """\nUse the get command to put an item into your inventory. This command will not work for all items. 
        An example would be using the get command on a bookcase and expecting it to be in your inventory."""
        return use, desc

    @staticmethod
    def help_examine():
        use = "[examine] [item]"
        desc = """\nuse the examine command to examine a specific item that is in the room the player is in. It will give the 
        user a more detailed description of the item that is being targeted."""
        return use, desc

    @staticmethod
    def help_unlock():
        use = "[unlock][*valid exit*]"
        desc = """\nUse the unlock command to unlock doors."""
        return use, desc

    @staticmethod
    def help_lock():
        use = "[lock][*valid exit*]"
        desc = """\nUse the lock command to lock doors."""
        return use, desc

    @staticmethod
    def help_open():
        use = "[open][*valid exit*]"
        desc = """\nUse the open command to open doors."""
        return use, desc

    @staticmethod
    def help_close():
        use = "[close][*valid exit*]"
        desc = """\nUse the close command to close doors."""
        return use, desc

    @staticmethod
    def help_block():
        use = "[block][*valid exit*]"
        desc = """\nUse the block command to block a door."""
        return use, desc

    def help_command(self, command):
        if command == "help move":
            self.help_move()
        elif command == "help look":
            self.help_look()
        elif command == "help user":
            self.help_use()
        elif command == "help get":
            self.help.get()
        elif command == "help_examine":
            self.help_examine()
        elif command == "help unlock":
            self.help_unlock()
        elif command == "help lock":
            self.help_lock()
        elif command == "help open":
            self.help_open()
        elif command == "help close":
            self.help_close()
        elif command == "help block":
            self.help_block()
        else:
            self.help()
        return


