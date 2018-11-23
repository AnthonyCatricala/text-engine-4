from Util.RoomUtil import *
from Parser.CommandExecuter import *
from Parser.UserParser import *
from Objects.Character import Player


start_room = load_room("RoomTester")
player = Player("name", [], "Player description", None)
cp = UserParser(start_room, player)
ce = CommandExecutor(start_room, player)
com = cp.simplify_command("get storage room key")
print(com)
ce.executor(com)
com = cp.simplify_command("drop storage room key")
ce.executor(com)
#eh = "go exit 1".split()
#exit_name = "exit_1"
#ce = CommandExecutor(start_room, None)
#print((start_room.exits[1].links_to)[8:len(start_room.exits[1].links_to)-5])
#ce.move_function(["go", exit_name, "", ""])
#ce.new_move_function(["go", "exit_5", "", ""])
#ce.newest_move_function(["go", exit_name, "", ""])