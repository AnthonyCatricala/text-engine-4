#!/usr/bin/python3

from Player import Player
from Room import Room
from CommandParser import CommandParser


# Initialization on the game.
def init_game():

    # TODO Take this out of a main file for production.
    # Setup essential game parts.

    player = Player(player_name="Demo")
    room = Room(room_name="Log_Cabin", player_name=player.player_name)
    command_parser = CommandParser(player=player, room=room)

    # Continue to take commands till the player dies or the player achieves win conditions.
    while player.alive and not player.win:
        user_command = input()
        user_command = user_command.lower()
        command_parser.parse_command(user_command)

    # TODO Make dynamic win/loss statements.
    if not player.alive:
        if player.win:
            print("\n\nYou have won, but have died in the process.")
        else:
            print("\n\nYou have died.\nGame Over.")
    elif player.win:
        print("Congratulations, You've Won!")


if __name__ == "__main__":
    init_game()
