from Util.RoomUtil import *
from Parser.CommandExecuter import *
from Parser.UserParser import *


start_room = load_room("Example")
up = UserParser(start_room)
print(start_room.inventory)
if start_room.inventory:
    print(start_room.inventory.keys())
#print(start_room.exits[0].links_to[8:len(start_room.exits[0].links_to) - 5])
#load_room(room_file= start_room.exits[0].links_to)
#cp = UserParser(start_room)
#eh = "go exit 1".split()
#exit_name = "exit_1"
#3ce = CommandExecutor(start_room, None)
#load_room(start_room.exit[1].links_to)
#print((start_room.exits[1].links_to)[8:len(start_room.exits[1].links_to)-5])
#ce.move_function(["go", exit_name, "", ""])
#ce.new_move_function(["go", "exit_5", "", ""])
#ce.newest_move_function(["go", exit_name, "", ""])