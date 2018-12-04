from Util.RoomUtil import *
from Objects.Room import Room
from Objects.Trigger import WinTrigger


class CommandExecutor:
    room = None
    player = None
    trigger_list = []

    def __init__(self, room, player):
        self.room = room
        self.player = player

        # If the room hasn't been visited, then print the room name and details.
        print("\n" + self.room.room_name)
        if not room.visited:
            self.room.visited = True
            self.look_function(["look", "", "", ""])
        # Newline for readability.
        print()

    def executor(self, parsed_string):
        triggers = self.room.get_triggers(parsed_string[0])

        user_scripts = self.room.get_user_scripts(parsed_string[0])
        instead = False
        for user_script in user_scripts:
            if user_script.before:
                exec(user_script.before)
            if user_script.instead:
                instead = True
                exec(user_script.instead)

        # When leaving a room, triggers need to occur before the new room is loaded.
        triggered = False
        if parsed_string[0] == 'go':
            triggered = True
            for trigger in triggers:
                trigger.trigger()

        # A user script may forcefully skip typical command execution if it has an 'instead' value.
        if not instead:
            if parsed_string[0] not in ["go", "inventory"]:
                print("\n" + self.room.room_name)

            if parsed_string[0] == "error":
                print(parsed_string[0], ":", parsed_string[1])
                if parsed_string[2] != "":
                    print("You may try to " + parsed_string[2] + ":")
                    print(parsed_string[3])
            elif parsed_string[0] == "look":
                self.look_function(parsed_string)
            elif parsed_string[0] == "go":
                self.move_function(parsed_string)
    #        elif parsed_string[0] == "examine":
    #            self.examine_function(parsed_string)
            elif parsed_string[0] in ["open", "close"]:
                self.open_close_lock_unlock_function(parsed_string)
            elif parsed_string[0] in ["lock", "unlock"]:
                self.open_close_lock_unlock_function(parsed_string)
            elif parsed_string[0] in ["block", "unblock"]:
                self.block_unblock_function(parsed_string)
            elif parsed_string[0] == "get":
                self.take_function(parsed_string)
            elif parsed_string[0] == "drop":
                self.drop_function(parsed_string)
            elif parsed_string[0] == "inventory":
                print("inventory:")
                if self.player.inventory:
                    for x in self.player.inventory:
                        print(x.quantity, x.item_name)
        self.room.save()
#        elif parsed_string[0] == "take":
#            self.get_function() TODO add this with items

        if not triggered:
            for trigger in triggers:
                trigger.trigger()

        for user_script in user_scripts:
            if user_script.after:
                exec(user_script.after)

        # New line for readability.
        print()

    def is_bright(self, li):
        for x in li:
            if x.illuminated:
                return True
        return False

    def look_check(self, parsed_string, li):
        s = ""
        for x in li:
            if x.item_name.replace(" ", "_") == parsed_string[3]:
                if parsed_string[1] == parsed_string[2] and not x.visible:
                    s = "You can't see that item."
                    break
                elif parsed_string[1] == parsed_string[2]:
                    s = x.description
                elif parsed_string[1] == "lock" or parsed_string[1] == "door":
                    s = parsed_string[1] + "s don't have a description."
                break
        if s == "":
            s = "No description given."
        return s



    def look_function(self, parsed_string):
        s = ""
        if not self.is_bright([self.room]) and not (self.player.inventory and self.is_bright(self.player.inventory)) \
                and not (self.is_bright(self.room.inventory and self.room.inventory)):
            s = "It's too dark!"
        elif parsed_string[1] == "":
            s = self.room.description
        elif parsed_string[2] == "exit":
            for x in self.room.exits:
                if x.compass_direction.replace(" ", "_") == parsed_string[3]:
                    if parsed_string[1] == "exit":
                        s = x.description
                    elif parsed_string[1] == "lock" or parsed_string[1] == "door":
                        s = parsed_string[1] + "s don't have a description."
                    break
            if s == "":
                s = "No description given."
        elif parsed_string[2] == "room_item" and self.room.inventory:
            s = self.look_check(parsed_string, self.room.inventory)
        elif parsed_string[2] == "player_item" and self.player.inventory:
            s = self.look_check(parsed_string, self.player.inventory)
        print(s)
        # TODO Come back to this when objects have been created.
        #for x in self.room.inventory:
         #   print(x)

    def move_function(self, parsed_string):
        is_exit = None
        move = None
        second_fail = False
        for e in self.room.exits:
            if e.compass_direction == parsed_string[1]:
                if e.blocked:
                    print("\n" + self.room.room_name)
                    print("There is something blocking the {} exit of the {}. You cannot enter"
                          .format(e.compass_direction, self.room.room_name))
                elif e.door and not e.door.is_open and e.door.lock and e.door.lock.is_locked:
                    print("\n" + self.room.room_name)
                    print("The {}'s {} door seems to be locked. You cannot enter."
                          .format(self.room.room_name, e.compass_direction))
                elif e.door and not e.door.is_open:
                    print("\n" + self.room.room_name)
                    print("The {} door is closed. You can try to open the door.".format(e.compass_direction))
                elif not e.door or e.door.is_open:
                    move = e
                else:
                    print("\n" + self.room.room_name)
                    print("The door blocks your path.")
                is_exit = e
                break
        if is_exit is None:
            print("\n" + self.room.room_name)
            print("There is no exit in that direction.")
        elif move is not None:
            test_room = load_room(room_file = move.links_to)
            for x in test_room.exits:
                if x.links_to == self.room.room_file:
                    if x.blocked:
                        second_fail = True
                        print("\n" + self.room.room_name)
                        print("There is something blocking the {} exit of the {}. You cannot enter."
                              .format(x.compass_direction, test_room.room_name))
                    elif x.door and not x.door.is_open:
                        second_fail = True
                        print("\n" + self.room.room_name)
                        print("The door is closed on the other side. You cannot enter.")
                    elif x.door and not x.door.is_open and x.door.lock and x.door.lock.is_locked:
                        second_fail = True
                        print("\n" + self.room.room_name)
                        print("The door is locked on the other side. You cannot enter.")
                    break
            if move is not None and second_fail is False:
                self.room.save()
                self.room.load(move.links_to)

                print("\n" + self.room.room_name)
                if not self.room.visited:
                    self.room.visited = True
                    print(self.room.description)

                # Trigger all events that happen when you enter a room.
                for trigger in self.room.get_triggers("enter"):
                    print()
                    trigger.trigger()

                for user_script in self.room.get_user_scripts("enter"):
                    print()
                    exec(user_script.before)
                    exec(user_script.instead)
                    exec(user_script.after)

                #print("You move to {}.".format(self.room.room_name))

    #def examine_function(self, parsed_string):
#
#        examined_item = parsed_string[1]
#
#        if examined_item not in Room.inventory: #and examined_item not in Player.inventory: # TODO bring this back once items/player inventory exist.
#            print("That doesn't seem to be here. What are you trying to examine?")

        # TODO bring things below this line in once items are implemented.
        #else:
            #for x in Item.master_inventory:
                #if x == examined_item:
                   # print (Item.item_description)

    def oclu_check(self, parsed_string, li, player_inv):
        for x in li:
            if x.item_name.replace(" ", "_") == parsed_string[1]:
                if not x.door:
                    print("There is no door.")
                elif parsed_string[0] == "open":
                    print(x.door.open())
                elif parsed_string[0] == "close":
                    print(x.door.close())
                elif parsed_string[0] == "lock":
                    print(x.door.lock_door(player_inv))
                elif parsed_string[0] == "unlock":
                    print(x.door.unlock_door(player_inv))
                break

    def open_close_lock_unlock_function(self, parsed_string):
        player_inv = []
        for x in self.player.inventory:
            player_inv.append(x.item_name.replace(" ", "_"))
        if parsed_string[2] == "room_item":
            self.oclu_check(parsed_string, self.room.inventory, player_inv)
        elif parsed_string[2] == "player_item":
            self.oclu_check(parsed_string, self.player.inventory, player_inv)
        elif parsed_string[2] == "exit":
            worked = False
            change_door = False
            for x in self.room.exits:
                if x.compass_direction == parsed_string[1]:
                    if parsed_string[0] == "open":
                        change_door = x.open_door()
                    elif parsed_string[0] == "close":
                        change_door = x.close_door()
                    elif parsed_string[0] == "lock":
                        change_door = x.lock_door(player_inv)
                    elif parsed_string[0] == "unlock":
                        change_door = x.unlock_door(player_inv)
                    exit_used = x
                    worked = True
                    break
            if not worked:
                print("That is not a valid exit.")
            elif change_door:
                test_room = load_room(room_file = exit_used.links_to)
                for x in test_room.exits:
                    if x.links_to == self.room.room_file:
                        if exit_used.door and parsed_string[0] == "open":
                            x.door.is_open = True
                        elif x.door and parsed_string[0] == "close":
                            x.door.is_open = False
                        elif x.door and x.door.lock and parsed_string[0] == "lock":
                            if not x.door.lock.key or (x.door.lock.key.replace(" ", "_") in player_inv):
                                x.door.lock.is_locked = True
                        elif x.door and x.door.lock and parsed_string[0] == "unlock":
                            if not x.door.lock.key or (x.door.lock.key.replace(" ", "_") in player_inv):
                                x.door.lock.is_locked = False
                        test_room.save()
                        break

    def block_unblock_function(self, parsed_string):
        worked = False
        for x in self.room.exits:
            if x.compass_direction == parsed_string[1]:
                if parsed_string[0] == "block":
                    x.block()
                else:
                    x.unblock()
                worked = True
                break
        if not worked:
            print("That is not a valid exit.")

    def take_function(self, parsed_string):
        room_check = False
        player_check = False
        room_item = None

        for x in self.room.inventory:
            if (x.item_name.replace(" ", "_") == parsed_string[1]) and x.obtainable:
                x.quantity = x.quantity - 1
                room_check = True
                room_item = x
                if x.quantity == 0:
                    self.room.inventory.remove(x)
                break
        if room_check:
            print("took " + room_item.item_name.upper())
            for x in self.player.inventory:
                if x.item_name.replace(" ", "_") == parsed_string[1]:
                    x.quantity = x.quantity + 1
                    player_check = True
                    break
        if room_check and not player_check:
            self.player.inventory.append(Item(room_item.item_name, room_item.description, room_item.alias, 1,
                                              room_item.visible, room_item.illuminated, room_item.obtainable,
                                              room_item.inventory, room_item.door, room_item.triggers,
                                              room_item.user_scripts))
        if not room_check:
            print(parsed_string[1].replace("_"," ") + " is not obtainable!")

    def drop_function(self, parsed_string):
        room_check = False
        player_check = False
        player_item = None

        for x in self.player.inventory:
            if x.item_name.replace(" ", "_") == parsed_string[1]:
                x.quantity = x.quantity - 1
                player_check = True
                player_item = x
                if x.quantity == 0:
                    self.player.inventory.remove(x)
                break
        if player_check:
            print("dropped " + player_item.item_name.upper())
            for x in self.room.inventory:
                if x.item_name.replace(" ", "_") == parsed_string[1]:
                    x.quantity = x.quantity + 1
                    room_check = True
                    break
        if player_check and not room_check:
            self.room.inventory.append(Item(player_item.item_name, player_item.description, player_item.alias, 1,
                                            player_item.visible, player_item.illuminated, player_item.obtainable,
                                            player_item.inventory, player_item.door, player_item.triggers,
                                            player_item.user_scripts))

    def save(self):
        self.room.save()
        self.player.save(self.room.room_file)
