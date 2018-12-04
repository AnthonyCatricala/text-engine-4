
class HelpMenu:

    def help(self):
        return "Please enter a command after help for further assistance with specific commands"

    def help_move(self):
        move = [
                "Go, "
                "go, "
                "Move, "
                "move, "
                "Walk, "
                "walk, "
                "Run, "
                "run"
        ]
        direction = [
            "N, "
            "n, "
            "North, "
            "north, "
            "S, "
            "s, "
            "South, "
            "south, "
            "E, "
            "e, "
            "East, "
            "east, "
            "W, "
            "w, "
            "West, "
            "west"
        ]
        use = "[move] [direction]"
        usable_move = " ".join(move)
        usable_direction = " ".join(direction)
        desc = """\nUse one of the move commands and follow it up with a compass direction to attempt 
        to move to a new room in the chosen direction. For example, typing 'move north' will move you 
        to the room north of you, if possible."""
        return "use: " + use + "\nusable move: " + usable_move + "\nusable direction: " + usable_direction + \
               "\ndescription: " + desc

    def help_look(self):
        use = "look"
        desc = "\nUse the look command to look at the surroundings of the room you are in as well as its contents.\n"
        return use, desc

    def help_use(self):
        use = "[use] [item]"
        desc = """\nUse the use command to use an item that is in the inventory of the player. Most items will be 
        consumable, meaning the item is removed from the players inventory on use but not all items will work 
        like that. An example would be an item such as a key being used to unlock a door."""
        return "use: " + use + "\ndescription: " + desc

    def help_get(self):
        use = "[get] [item]"
        desc = """\nUse the get command to put an item into your inventory. This command will not work for all items. 
        An example would be using the get command on a bookcase and expecting it to be in your inventory."""
        return "use: " + use + "\ndescription" + desc

    def help_examine(self):
        use = "[examine] [item]"
        desc = """\nuse the examine command to examine a specific item that is in the room the player is in. It will give the 
        user a more detailed description of the item that is being targeted."""
        return "use: " + use + "\ndescription" + desc

    def help_unlock(self):
        use = "[unlock][*valid exit*]"
        desc = """\nUse the unlock command to unlock doors."""
        return "use: " + use + "\ndescription: " + desc

    def help_lock(self):
        use = "[lock][*valid exit*]"
        desc = """\nUse the lock command to lock doors."""
        return "use: " + use + "\ndescription: " + desc

    def help_open(self):
        use = "[open][*valid exit*]"
        desc = """\nUse the open command to open doors."""
        return "use: " + use + "\ndescription: " + desc

    def help_close(self):
        use = "[close][*valid exit*]"
        desc = """\nUse the close command to close doors."""
        return "use: " + use + "\ndescription: " + desc

    def help_block(self):
        use = "[block][*valid exit*]"
        desc = """\nUse the block command to block a door."""
        return "use: " + use + "\ndescription: " + desc

    def help_command(self, command):
        s = ""
        if command == "go":
            s = self.help_move()
        elif command == "look":
            s = self.help_look()
        elif command == "drop":    # TODO
            s= "drop help hasn't been created yet."
        # elif command == "help user":
        #    self.help_use()
        elif command == "get":
            s = self.help.get()
        # elif command == "help_examine":
        #    self.help_examine()
        elif command == "unlock":
            s = self.help_unlock()
        elif command == "lock":
            s = self.help_lock()
        elif command == "open":
            s = self.help_open()
        elif command == "close":
            s = self.help_close()
        elif command == "block":
            s = self.help_block()
        elif command == "unblock": # TODO
            s = "help unblock hasn't been created yet"
        else:
            s = self.help()
        return s


