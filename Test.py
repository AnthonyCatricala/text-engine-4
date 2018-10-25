from Parser.UserParser import UserParser
import Util.RoomUtil


room = Util.RoomUtil.load_room("Example")
up = UserParser(room)
#up.testing_method("go compass direction")
print(up.simplify_command("look compass directon lock"))
