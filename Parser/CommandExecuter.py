from Util.RoomUtil import load_room
from Objects.Room import Room


class CommandExecutor:
    room = None
    player = None
    trigger_list = []

    def __init__(self, room, player):
        self.room = room
        self.player = player
        #for x in room.triggers:
        #    self.trigger_list.append(("room", x.trigger_command, x.description))

    def executor(self, parsed_string):
        #print("\n", self.room.room_name)

        triggers = self.room.get_triggers(parsed_string[0])

        if parsed_string[0] == "error":
            print(parsed_string[0],":", parsed_string[1])
        elif parsed_string[0] == "look":
            self.look_function(parsed_string)
        elif parsed_string[0] == "go":
            self.move_function(parsed_string)
        elif parsed_string[0] == "examine":
            self.examine_function(parsed_string)
        elif parsed_string[0] in ["open", "close"]:
            self.open_close_lock_unlock_function(parsed_string)
        elif parsed_string[0] in ["lock", "unlock"]:
            self.open_close_lock_unlock_function(parsed_string)
        elif parsed_string[0] in ["block", "unblock"]:
            self.block_unblock_function(parsed_string)
#        elif parsed_string[0] == "take":
#            self.get_function() TODO add this with items

        # TODO Delete triggers after they are tripped.
        for trigger in triggers:
            trigger.trigger()

    def look_function(self, parsed_string):
        s = ""
        if parsed_string[1] == "":
            s = self.room.description
        else:
            for x in self.room.exits:
                if x.compass_direction == parsed_string[3]:
                    if parsed_string[1] == "exit":
                        s = x.description
                    elif parsed_string[1] == "lock" or parsed_string[1] == "door":
                        s = parsed_string[1] + "s don't have a description."
                    break
            if s == "":
                s = "No description given."
        print(s)

        # TODO Come back to this when objects have been created.
        #for x in self.room.inventory:
         #   print(x)

    def move_function(self, parsed_string):
        is_exit = None
        move = None
        blocked = False
        for e in self.room.exits:
            if e.compass_direction == parsed_string[1]:
                if e.blocked:
                    print("There is something blocking the " + e.compass_direction + " exit of the " + self.room.room_name +
                          ". You cannot enter.")
                elif e.door and not e.door.is_open and e.door.lock and e.door.lock.is_locked:
                    print("The " + self.room.room_name + "'s " + e.compass_direction + " door seems to be locked. "
                                                                                        "You cannot enter.")
                elif e.door and not e.door.is_open and e.door.lock and not e.door.lock.is_locked:
                    print("The", e.compass_direction, "door in the", self.room.room_name, "is closed, but it "
                                                                                           "doesn't seem to be locked."
                                                                                           "You can open the door.")
                elif not e.door or e.door.is_open:
                    move = e
                elif e.door and not e.door.is_open:
                    print("The", e.compass_direction, "door is closed. You can open the door.")
                else:
                    print("The door blocks your path.")
                is_exit = e
                break
        if is_exit is None:
            print("There is no exit in that direction.")
        elif move is not None:
            test_room = load_room(room_file = move.links_to)
            for x in test_room.exits:
                if x.links_to == self.room.room_file:
                    blocked = x.blocked
                    if blocked:
                        print("There is something blocking the " + x.compass_direction + " exit of the " +
                              test_room.room_name + ". You cannot enter.")
                    break
            if move is not None and blocked is False:
                self.room.save()
                self.room.load(move.links_to)
                print("You move to {}.".format(self.room.room_name))

    def examine_function(self, parsed_string):

        examined_item = parsed_string[1]

        if examined_item not in Room.inventory: #and examined_item not in Player.inventory: # TODO bring this back once items/player inventory exist.
            print("That doesn't seem to be here. What are you trying to examine?")

        # TODO bring things below this line in once items are implemented.
        #else:
            #for x in Item.master_inventory:
                #if x == examined_item:
                   # print (Item.item_description)

    def open_close_lock_unlock_function(self, parsed_string):
        worked = False
        change_door = False
        for x in self.room.exits:
            if x.compass_direction == parsed_string[1]:
                if parsed_string[0] == "open":
                    change_door = x.open_door()
                elif parsed_string[0] == "close":
                    change_door = x.close_door()
                elif parsed_string[0] == "lock":
                    change_door = x.lock_door()
                elif parsed_string[0] == "unlock":
                    change_door = x.unlock_door()
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
                        x.door.lock.is_locked = True
                    elif x.door and x.door.lock and parsed_string[0] == "unlock":
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


#   def get_function(self, parsed_string, room):
# should remove item from room inventory and append to player inventory. Should check for all 4 command parts
# i.e. get thing from container