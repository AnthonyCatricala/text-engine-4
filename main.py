from Parser.CommandExecuter import *
from Parser.UserParser import *

import os

# TODO The project should run from any directory.
PROJECT_DIR = os.path.abspath(os.path.join(__file__, os.pardir))
os.chdir(PROJECT_DIR)


def play():
    start_room = load_room('Test Room')

    cp = UserParser(start_room)
    ce = CommandExecutor(start_room, None)

    while True:
        user_command = input()
        parsed_command = cp.simplify_command(user_command)
        ce.executor(parsed_command)


if __name__ == "__main__":
    play()