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
        self.movement = ["go", "walk", "run", "move", "exit"]

    def parse_command(self, command):
        command_parts = command.split(" ")
        if len(command_parts) >= 1:
            major_command = command_parts[0]

            # Singular argument commands.
            if len(command_parts) == 1:
                if major_command == "look":
                    self.look_command()
                elif major_command == "inventory":
                    self.check_inventory_command()
                else:
                    print(self.__general_error)

            # Multi argument commands.
            elif major_command == "sleep":
                self.parse_sleep_command(command_parts)
            elif major_command == "read":
                self.parse_read_command(command_parts)
            elif major_command == "take":
                self.parse_take_command(command_parts)
            elif major_command == "drop":
                self.parse_drop_command(command_parts)
            elif major_command in self.movement:
                self.parse_movement_command(command_parts)
            elif major_command == "open":
                self.parse_open_command(command_parts)
            elif major_command == "eat":
                self.parse_eat_command(command_parts)
            elif major_command == "unlock":
                self.parse_unlock_command(command_parts)
            else:
                print(self.__general_error)
            self.save_state()

    @staticmethod
    def check_item_trigger(item):
        # ##
        # Checks if the command you are issuing has a triggers
        #
        # @return true/false
        # @author Dakotah Jones
        # ##
        out = False
        for key, value in item.items():
            if "triggers" in key:
                out = True
                break
        return out

    def parse_unlock_command(self, command_list):
        directions = [
            "north",
            "south",
            "east",
            "west",
            "up",
            "down"
        ]
        equivalent = {
            "northern": "north",
            "southern": "south",
            "eastern": "east",
            "western": "west"
        }
        # unlock [direction] door with [key name]
        num_parts = len(command_list)

        # Partially formed commands
        if num_parts == 3:
            direction = command_list[1]

            if direction in equivalent.keys():
                direction = equivalent[direction]

            if direction in directions:
                print("Unlock {} {} with what?".format(direction, command_list[2]))
            else:
                print(self.__general_error)
        elif num_parts == 5:
            direction = command_list[1]

            # TODO Add unlocking of things other than doors. (Chests, Windows, etc.)
            locked_object = command_list[2]
            preposition = command_list[3]
            key_name = command_list[4]

            if direction in equivalent.keys():
                direction = equivalent[direction]

            room_items = self.room.inventory
            player_items = self.player.inventory

            if direction in directions and preposition == "with":
                if direction in self.room.go.keys():
                    if key_name in room_items.keys():
                        self.room.go[direction]["locked"] = False
                        print("You unlock the {} with the {}".format(locked_object, key_name))
                        del room_items[key_name]
                    elif key_name in player_items.keys():
                        self.room.go[direction]["locked"] = False
                        print("You unlock the {} with the {}".format(locked_object, key_name))
                        del player_items[key_name]
                    else:
                        print("A key b that name doesn't exist.")
                else:
                    print("There is no {} in that direction.".format(locked_object))
            else:
                print(self.__general_error)

    def parse_open_command(self, command_list):
        directions = [
            "north",
            "south",
            "east",
            "west",
            "up",
            "down"
        ]
        equivalent = {
            "northern": "north",
            "southern": "south",
            "eastern": "east",
            "western": "west"
        }

        num_parts = len(command_list)

        if num_parts >= 2:
            command_direction = command_list[1]
            if command_direction in equivalent.keys():
                command_direction = equivalent[command_direction]
            if command_direction in directions:
                if num_parts == 3:
                    door_part = command_list[2]
                    if door_part == "door":
                        exits = self.room.get_exits()
                        if command_direction in exits.keys():

                            door = exits[command_direction]
                            if not door["open"]:

                                if door["locked"]:
                                    print(door["locked_description"])
                                else:
                                    door["open"] = True
                                    print(door["open_description"])

                                    if self.check_item_trigger(door):
                                        triggers = door["triggers"]["open"]
                                        self.parse_trigger(triggers)

                                    self.room.save_room()
                            else:
                                print("That door is already open.")

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

                    if self.check_item_trigger(inventory_item):
                        triggers = inventory_item["triggers"]["eat"]
                        self.parse_trigger(triggers)

                    eat_statement = inventory_item["eat"]
                    del self.room.inventory[command_item]
                else:
                    eat_statement = "{} could not be eaten.".format(command_item)
            elif command_item in self.player.inventory.keys():
                inventory_item = self.player.inventory[command_item]
                if "eat" in inventory_item.keys():

                    if self.check_item_trigger(inventory_item):
                        triggers = inventory_item["triggers"]["eat"]
                        self.parse_trigger(triggers)

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

        directions = [
            "north",
            "south",
            "east",
            "west",
            "up",
            "down"
        ]
        equivalent = {
            "northern": "north",
            "southern": "south",
            "eastern": "east",
            "western": "west"
        }

        if len(command_list) == 1:
            print("Move in which direction?")
        elif len(command_list) == 2:
            direction = command_list[1]

            if direction in equivalent.keys():
                direction = equivalent[direction]

            if direction in self.room.go.keys():
                room_exit = self.room.go[direction]
                if room_exit["open"]:

                    if not room_exit["locked"]:
                        self.room.room_name = room_exit["room_name"]
                        self.room.check_save()
                    else:
                        print("That door is locked")

                else:
                    print("That door is not currently.")

            else:
                print("You cannot go in that direction.")

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
            item_name = command_list[1]
            if item_name in room_items:

                # Proper take command.
                take_statement = self.room.inventory[item_name]["take"]
                item = self.room.inventory[item_name]

                # Check if taking the the item triggers a change.
                if self.check_item_trigger(item):
                    triggers = item["triggers"]["take"]
                    self.parse_trigger(triggers)

                self.player.inventory[item_name] = self.room.inventory[item_name]
                del self.room.inventory[item_name]

            else:
                take_statement = "Could not take '{}'. No such object was found in the room.".format(item_name)
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

    def parse_trigger(self, triggers):

        for trigger_type in triggers.keys():
            if trigger_type == "look-change":
                for key, val in triggers[trigger_type].items():
                    self.room.look[key] = val
            elif trigger_type == "add-to-room":
                for key, val in triggers[trigger_type].items():
                    self.room.inventory[key] = val
            elif trigger_type == "remove-from-room":
                for key, val in triggers[trigger_type].items():
                    item = dict()
                    item[key] = val
                    if item in self.room.inventory:
                        del self.room.inventory[key]
            elif trigger_type == "player-death":
                self.player.alive = False
            elif trigger_type == "player-win":
                self.player.win = True
        del triggers

    def check_room_trigger(self):
        out = False
        for key, val in self.room.triggers.items():
            out = True
            break
        return out

    def look_command(self):
        look = self.room.look
        for key, val in look.items():
            if val:
                print(key)
        if self.check_room_trigger():
            if "look" in self.room.triggers.keys():
                self.parse_trigger(self.room.triggers["look"])

    def check_inventory_command(self):
        print("Inventory:")
        for item in self.player.inventory.keys():
            print(item)
        print()

    def save_state(self):
        self.room.save_room()
        self.player.save_player()
