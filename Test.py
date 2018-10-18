from venv import create

from Parser.UserParser import UserParser
from Util.RoomUtil import *
#up = UserParser("Example")

#print(up.simplify_command("bwaha    HaHa"))


room = create_room("test_name", "its an empty room, like pats soul.")
r_exit = create_room_exit("north", room.room_file, "description of exit")

print(r_exit)