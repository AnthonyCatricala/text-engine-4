from Util.RoomUtil import *
from Parser.CommandExecuter import *
from Parser.UserParser import *


start_room = load_room("RoomTester")

cp = UserParser(start_room)
#eh = "go exit 1".split()
print("look" + " north")
print(cp.simplify_command("look north"))