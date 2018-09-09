class CommandParser:
    # ##
    # Purpose of the CommandParser is to manipulate the player and room.
    # It will add and delete elements from the saved json files.
    # ##

    room = None
    player = None

    movement = None

    __general_error = "Could not understand statement."

    def __init__(self, room, player):
        self.room = room
        self.player = player
        self.movement = ["go", "walk", "run", "move"]

    def parse_command(self, command):
        command_parts = command.split(" ")

        # Singular argument commands.
        if len(command_parts) == 1:
            if command == "look":
                self.look_command()
            elif command == "inventory":
                self.check_inventory_command()
            else:
                print(self.__general_error)

        # Multi argument commands.
        elif command_parts[0] == "sleep":
            self.parse_sleep_command(command_parts)
        elif command_parts[0] == "read":
            self.parse_read_command(command_parts)
        elif command_parts[0] == "take":
            self.parse_take_command(command_parts)
        elif command_parts[0] == "drop":
            self.parse_drop_command(command_parts)
        elif command_parts[0] in self.movement:
            self.parse_movement_command(command_parts)
        elif command_parts[0] == "open":
            self.parse_open_command(command_parts)
        elif command_parts[0] == "eat":
            self.parse_eat_command(command_parts)
        else:
            print(self.__general_error)
        self.save_state()

    def check_for_trigger(self, item):
        # ##
        # Checks if the command you are issuing has a triggers
        #
        # @return true/false
        # @author Dakotah Jones
        # ##

        for key, value in item.items():
            if "trigger" in key:
                out = True
        return out

    def parse_open_command(self, command_list):
        directions = [
            "north",
            "south",
            "east",
            "west",
            "up",
            "down"
        ]
        equivelent = {
            "northern": "north",
            "southern": "south",
            "eastern": "east",
            "western": "west"
        }

        num_parts = len(command_list)

        if num_parts >= 2:
            command_direction = command_list[1]
            if command_direction in equivelent.keys():
                command_direction = equivelent[command_direction]
            if command_direction in directions:
                if num_parts == 3:
                    door_part = command_list[2]
                    if door_part == "door":
                        exits = self.room.get_exits()
                        if command_direction in exits.keys():
                            door = exits[command_direction]
                            if door["locked"]:
                                print(door["locked_description"])
                            else:
                                door["open"] = True
                                print("open_description")
                                self.room.save_room()
                        else:
                            print("Door does not exist.")


                else:
                    print(self.__general_error)
            else:
                print("Open which door?")

    def parse_eat_command(self, command_list):
        # ##
        # Function responsible for eat commands.
        #
        # It will attempt to eat an item within the environment or within the player inventory..
        # @author Dakotah Jones
        # ##

        if len(command_list) == 1:
            eat_statement = "Eat what?"
        elif len(command_list) == 2:
            command_item = command_list[1]
            if command_item in self.room.inventory.keys():
                inventory_item = self.room.inventory[command_item]
                if "eat" in inventory_item.keys():
                    eat_statement = inventory_item["eat"]
                    del self.room.inventory[command_item]
                else:
                    eat_statement = "{} could not be eaten.".format(command_item)
            elif command_item in self.player.inventory.keys():
                inventory_item = self.player.inventory[command_item]
                if "eat" in inventory_item.keys():
                    eat_statement = inventory_item["eat"]
                    del self.player.inventory[command_item]
                else:
                    eat_statement = "{} could not be eaten.".format(command_item)
            else:
                eat_statement = "Could not eat '{}'. No such object was found in your inventory.".format(command_item)
        else:
            eat_statement = self.__general_error
        print(eat_statement)

    def parse_movement_command(self, command_list):
        # ##
        # Function responsible for movement commands.
        #
        # It will attempt to move your character in a compass direction if there is an entrance or exit available.
        # @author Dakotah Jones
        # ##

        if len(command_list) == 1:
            print("Move in which compass direction?")
        elif len(command_list) == 2 and command_list[1] in self.direction:
            next_room = self.room.g
            self.room.load_room()
        else:
            print("Movement command was not understood.")

    def parse_drop_command(self, command_list):
        # ##
        # Function responsible for 'drop' commands.
        #
        # It will attempt to remove an object from the players inventory and place it in the environment.
        # @author Dakotah Jones
        # ##
        player_items = self.player.inventory

        if len(command_list) == 2:
            item = command_list[1]
            if item in player_items:
                take_statement = self.player.inventory[item]["drop"]
                self.room.inventory[item] = self.player.inventory[item]
                del self.player.inventory[item]

            else:
                take_statement = "Could not drop '{}'. No such object was found in your inventory.".format(item)
        elif len(command_list) == 1:
            take_statement = "Take what?"
        else:
            take_statement = self.__general_error

        print(take_statement)

    def parse_take_command(self, command_list):
        # ##
        # Function responsible for take commands.
        #
        # It will attempt to take an object from the environment and place it into the players inventory.
        # @author Dakotah Jones
        # ##
        room_items = self.room.inventory

        if len(command_list) == 2:
            item = command_list[1]
            if item in room_items:
                take_statement = self.room.inventory[item]["take"]
                self.player.inventory[item] = self.room.inventory[item]
                del self.room.inventory[item]

            else:
                take_statement = "Could not take '{}'. No such object was found in the room.".format(item)
        elif len(command_list) == 1:
            take_statement = "Take what?"
        else:
            take_statement = self.__general_error

        print(take_statement)

    def parse_read_command(self, command_list):
        # ##
        # Function responsible for read commands.
        #
        # It will attempt to read an item in the environment or players inventory
        # @author Dakotah Jones
        # ##

        room_items = self.room.inventory
        player_items = self.player.inventory

        if len(command_list) == 2:
            item = command_list[1]
            if item in room_items:
                read_statement = self.room.inventory[item]["read"]
            elif item in player_items:
                read_statement = self.player.inventory[item]["read"]
            else:
                read_statement = "Could not read '{}'. No such object was found".format(item)
        elif len(command_list) == 1:
            read_statement = "Read what?"
        else:
            read_statement = self.__general_error

        print(read_statement)

    def parse_sleep_command(self, command_list):
        # ##
        # Function responsible for 'sleep' commands.
        #
        # It will try to sleep on a piece of furniture in the environment.
        # @author Dakotah Jones
        # ##
        allowed_proposition = ["in", "on"]
        allowed_furniture = []

        for furniture in self.room.sleep.keys():
            allowed_furniture.append(furniture)

        sleep_statement = None

        if len(command_list) == 1:
            sleep_statement = "Sleep on what?"
        elif len(command_list) == 2:
            preposition = command_list[1]
            if preposition in allowed_proposition:
                sleep_statement = "Sleep {} what?".format(preposition)
        elif len(command_list) == 3 :
            preposition = command_list[1]
            furniture = command_list[2]
            if preposition in allowed_proposition and furniture in allowed_furniture:
                sleep_statement = self.room.sleep[furniture]

        if sleep_statement is None:
            sleep_statement = self.__general_error

        print(sleep_statement)

    def look_command(self):
        look = self.room.look
        for key, val in look.items():
            if val:
                print(key)

    def check_inventory_command(self):
        print("Inventory:")
        for item in self.player.inventory.keys():
            print(item)
        print()

    def save_state(self):
        self.room.save_room()
        self.player.save_player()
