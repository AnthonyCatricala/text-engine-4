import Parser.UserParser
import Parser.CommandExecuter
import Util.RoomUtil
from Objects.Character import Player

import argparse
import os

# TODO The project should run from any directory.
PROJECT_DIR = os.path.abspath(os.path.join(__file__, os.pardir))
os.chdir(PROJECT_DIR)

parser = argparse.ArgumentParser()
parser.add_argument('--character_file', help='Path to the player file you are trying to start as.')
parser.add_argument('--character_name', help='The name of the character you are trying to load.')
parser.add_argument('--room_file', help='Path to the room file you are trying to start in.')
parser.add_argument('--room_name', help='Path to the player file you are trying to start as.')


def play(parser):
    args = parser.parse_args()
    character_file = args.character_file
    character_name = args.character_name
    room_file = args.room_file
    room_name = args.room_name

    if character_name:
        character_file = "./Players/{}.player".format(character_name.replace(" ", "_"))
    if room_name:
        room_file = "./Rooms/{}.room".format(room_name.replace(" ", "_"))

    player = None
    room = None
    if character_file:
        player = Player.load(character_file)

    if player:
        room = Util.RoomUtil.load_room(room_file=player.current_room_file)
    elif room_file:
        room = Util.RoomUtil.load_room(room_file=room_file)
        player = Player("Default", [], "Player Description", None)
        player.save(room.room_file)

    if room and player:
        cp = Parser.UserParser.UserParser(room, player)
        ce = Parser.CommandExecuter.CommandExecutor(room, player)

        while True:
            user_command = input()
            if user_command == 'q':
                break
            parsed_command = cp.simplify_command(user_command)
            ce.executor(parsed_command)
    else:
        parser.print_help()


if __name__ == "__main__":
    play(parser)
