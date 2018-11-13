from Util.RoomUtil import *
from Parser.CommandExecuter import *
from Parser.UserParser import *


start_room = load_room('Test Room')

cp = UserParser(start_room)
ce = CommandExecutor(start_room, None)