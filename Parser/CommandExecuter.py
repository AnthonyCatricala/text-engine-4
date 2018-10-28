from Parser.UserParser import UserParser
from Objects.Room import Room
from Objects.Exit import Exit


class CommandExecutor:

    parsed_string = UserParser.user_parser

    def __init__(self, room, player):
        self.room = room
        self.player = player

    def executor(self, parsed_string):

        if parsed_string[0] == "Look":
            self.look_function(self.room)
        elif parsed_string[0] == "Move":
            self.move_function(self.parsed_string, self.room)
        elif parsed_string[0] == "Examine":
            self.examine_function(self.parsed_string, self.room)
#        elif parsed_string[0] == "Get":
#            self.get_function() TODO add this with items

    def look_function(self, room):

        print(room.description)
        for x in room.inventory:
            print(x)

    def move_function(self, parsed_string, room):

        Exit.compass_direction = parsed_string[1]

        if Exit.compass_direction in room.exits:
                if Exit.compass_direction.blocked:
                    print("There is something in the way.")
                    if Exit.door:
                        print("A door blocks the path.")
                else:
                    Room.room_file = Exit.links_to
                    print("You move to " +Room.room_name+ ".")
        else:
            print("There is no exit in that direction.")

    def examine_function(self, parsed_string, room):

        examined_item = parsed_string[1]

        if examined_item not in Room.inventory: #and examined_item not in Player.inventory: # TODO bring this back once items/player inventory exist.
            print("That doesn't seem to be here. What are you trying to examine?")

        # TODO bring things below this line in once items are implemented.
        #else:
            #for x in Item.master_inventory:
                #if x == examined_item:
                   # print (Item.item_description)

#   def get_function(self, parsed_string, room):
# should remove item from room inventory and append to player inventory. Should check for all 4 command parts
# i.e. get thing from container