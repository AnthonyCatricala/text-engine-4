from Parser.UserParser import UserParser
import Util.RoomUtil


room = Util.RoomUtil.load_room("Example")
#print(room)
up = UserParser(room)
#up.testing_method("go compass direction")
print(up.simplify_command("run compass direction"))
#Util.RoomUtil.save_room(room)