from Util.RoomUtil import *
from Parser.CommandExecuter import *
from Parser.UserParser import *

PROJECT_DIR = os.path.abspath(os.path.join(__file__, os.pardir))
os.chdir(PROJECT_DIR)
start_room = load_room('Test Room')

cp = UserParser(start_room)
ce = CommandExecutor(start_room, None)