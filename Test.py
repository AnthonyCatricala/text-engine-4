from Parser.UserParser import UserParser
from Parser.CommandExecuter import CommandExecutor
import Util.RoomUtil


room = Util.RoomUtil.load_room("Test_Room")
cp = CommandExecutor(room)
cp.executor("go north")
#print(room)
#up = UserParser(room)
#up.testing_method("go compass direction")
#print(up.simplify_command("l e"))
#Util.RoomUtil.save_room(room)