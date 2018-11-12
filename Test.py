from Parser.UserParser import UserParser
from Parser.CommandExecuter import CommandExecutor
import Util.RoomUtil


room = Util.RoomUtil.load_room("Test_Room")
cp = CommandExecutor(room)
ar = ["go","west", "", ""]
cp.new_move_function(ar)
print("\n")
cp.move_function(ar)
#print(room)
#up = UserParser(room)
#print(up.simplify_command("l e"))
#Util.RoomUtil.save_room(room)