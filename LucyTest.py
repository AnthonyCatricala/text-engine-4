from Util.RoomUtil import *
from Parser.CommandExecuter import *
from Parser.UserParser import *


start_room = load_room("RoomTester")

cp = UserParser(start_room)
#eh = "go exit 1".split()
exit_name = "exit_1"
ce = CommandExecutor(start_room, None)
print((start_room.exits[1].links_to)[8:len(start_room.exits[1].links_to)-5])
#ce.move_function(["go", exit_name, "", ""])
#ce.new_move_function(["go", "exit_5", "", ""])
#ce.newest_move_function(["go", exit_name, "", ""])