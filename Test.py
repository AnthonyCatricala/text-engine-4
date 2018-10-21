from Parser.UserParser import UserParser
import Util.RoomUtil


room = Util.RoomUtil.load_room("Example")
up = UserParser(room)
up.testing_method("look at the dog")
#print(up.simplify_command("look at the dog"))
