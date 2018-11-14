from Util.RoomUtil import *
from Parser.CommandExecuter import *
from Parser.UserParser import *


start_room = load_room("RoomTester")

cp = UserParser(start_room)
ce = CommandExecutor(start_room, None)
ce.executor(['unlock', 'exit_3', '', ''])