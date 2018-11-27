from Parser.CommandExecuter import *
from Parser.UserParser import *
from Objects.Character import Player
import Objects.Door
import Objects.Lock

room = load_room(room_file="./Tests/Rooms/RoomTester.room")   # blocked on one side
player = Player("player", [],"Player description", None)
ce = CommandExecutor(room, player)
cp = UserParser(room, player)
room_trans = load_room(room_file="./Tests/Rooms/RoomTesterTransverse.room") # Exit leads to a room on the other side
room.exits[0].links_to = "./Tests/Rooms/RoomTesterTransverse.room"
room_trans.exits[0].links_to = "./Tests/Rooms/RoomTester.room"
room_trans.exits[0].door.lock.is_locked = False
room.exits[0].door.lock.is_locked = False
room_trans.exits[0].door.is_open = True
room.exits[0].door.is_open = True
room.exits[0].blocked = False
room_trans.exits[0].blocked = False
room.exits[0].blocked = False
room_trans.exits[0].blocked = True
ce.executor(['go', 'exit_1', 'exit', ''])