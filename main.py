from Parser.CommandExecuter import *
from Parser.UserParser import *


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