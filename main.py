import Parser.UserParser
import Parser.CommandExecuter
import Util.RoomUtil

import os

# TODO The project should run from any directory.
PROJECT_DIR = os.path.abspath(os.path.join(__file__, os.pardir))
os.chdir(PROJECT_DIR)


def play():
    start_room = Util.RoomUtil.load_room('Missing Flag Room')

    cp = Parser.UserParser.UserParser(start_room)
    ce = Parser.CommandExecuter.CommandExecutor(start_room, None)

    while True:
        #print("q to quit.\n")
        user_command = input()
        if user_command == 'q':
            break
        parsed_command = cp.simplify_command(user_command)
        ce.executor(parsed_command)


if __name__ == "__main__":
    play()