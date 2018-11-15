from Util.RoomUtil import *
from Parser.UserParser import UserParser

import os
import unittest

# TODO The project should run from any directory.
PROJECT_DIR = os.path.abspath(os.path.join(os.path.join(__file__, os.pardir), os.pardir))
os.chdir(PROJECT_DIR)


class TestCommandParser(unittest.TestCase):
    room = load_room("RoomTester")
    command_parser = UserParser(room)

    # Testing empty input.
    def test_empty(self):
        # Empty input should result in empty output.
        test_answer = ['', '', '', '']
        test_input = ''
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

    # All tests that should result in the look command.
    def test_look(self):
        # Look alone should result in look command.
        test_answer = ['look', '', '', '']
        test_input = 'look'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        # Look around should result in look command.
        test_answer = ['look', '', '', '']
        test_input = 'look around'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        # Look alone should result in look command.
        test_answer = ['look', '', '', '']
        test_input = 'l'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        for x in ["north", "south", "east", "west", "exit 1",  "exit 2",  "exit 3",  "exit 4",  "exit 5"]:
            test_answer = ["look", "exit", "from", x.replace(" ", "_")]
            test_input = "look " + x
            test_output = self.command_parser.simplify_command(test_input)
            self.assertEqual(test_output, test_answer)

        for x in ["north", "south", "east", "west", "exit 1", "exit 2", "exit 3", "exit 4", "exit 5"]:
            test_answer = ["look", "door", "from", x.replace(" ", "_")]
            test_input = "look " + x + " door"
            test_output = self.command_parser.simplify_command(test_input)
            self.assertEqual(test_output, test_answer)

        for x in ["north", "south", "east", "west", "exit 1",  "exit 2",  "exit 3",  "exit 4",  "exit 5"]:
            test_answer = ["look", "lock", "from", x.replace(" ", "_")]
            test_input = "look " + x + " lock"
            test_output = self.command_parser.simplify_command(test_input)
            self.assertEqual(test_output, test_answer)

        for x in ["north", "south", "east", "west", "exit 1", "exit 2", "exit 3", "exit 4", "exit 5"]:
            test_answer = ["look", "lock", "from", x.replace(" ", "_")]
            test_input = "look " + x + " door lock"
            test_output = self.command_parser.simplify_command(test_input)
            self.assertEqual(test_output, test_answer)

    # All tests that should result in a go command.
    def test_go(self):
        # Go [compass direction] should result in output primary command being go,
        # and primary object being the compass direction.
        for x in ["go", "move", "walk", "run"]:
            for y in ["north", "south", "east", "west", "exit 1",  "exit 2",  "exit 3",  "exit 4",  "exit 5"]:
                test_answer = ["go", y.replace(" ", "_"), "", ""]
                test_input = x + " " + y
                test_output = self.command_parser.simplify_command(test_input)
                self.assertEqual(test_output, test_answer)

    # Tests for mis-spelled primary commands.
    def test_spelling(self):
        test_answer = ['error', 'not a command', '', '']
        test_input = 'loko'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['error', 'not a command', '', '']
        test_input = 'go nrth'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['error', 'not a command', '', '']
        test_input = 'go soth'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['error', 'not a command', '', '']
        test_input = 'go wst'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['error', 'not a command', '', '']
        test_input = 'go est'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

    # Tests for mixed primary command input.
    def test_mixed_commands(self):
        test_answer = ['error', 'not a command', '', '']
        test_input = 'go north look'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['error', 'not a command', '', '']
        test_input = 'north go'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['error', 'not a command', '', '']
        test_input = 'north look'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['error', 'not a command', '', '']
        test_input = 'look go'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

    def test_open_close(self):
        for x in ['open', 'close']:
            for y in ["north", "south", "east", "west", "exit 1",  "exit 2",  "exit 3",  "exit 4",  "exit 5"]:
                test_answer = [x, y.replace(" ", "_"), "", ""]
                test_input = x + " " + y + " door"
                test_output = self.command_parser.simplify_command(test_input)
                self.assertEqual(test_output, test_answer)
        for x in ['open', 'close']:
            for y in ["north", "south", "east", "west", "exit 1",  "exit 2",  "exit 3",  "exit 4",  "exit 5"]:
                test_answer = ['error', 'not a command', '', '']
                test_input = x + " " + y + " exit"
                test_output = self.command_parser.simplify_command(test_input)
                self.assertEqual(test_output, test_answer)
        for x in ['open', 'close']:
            for y in ["north", "south", "east", "west", "exit 1",  "exit 2",  "exit 3",  "exit 4",  "exit 5"]:
                test_answer = ['error', 'not a command', '', '']
                test_input = x + " " + y + " lock"
                test_output = self.command_parser.simplify_command(test_input)
                self.assertEqual(test_output, test_answer)

    def test_lock_unlock(self):
        for x in ["lock", "unlock"]:
            for y in ["north", "south", "east", "west", "exit 1",  "exit 2",  "exit 3",  "exit 4",  "exit 5"]:
                for z in ["door", "lock", "door lock"]:
                    test_answer = [x, y.replace(" ", "_"), "", ""]
                    test_input = x + " " + y + " " + z
                    test_output = self.command_parser.simplify_command(test_input)
                    self.assertEqual(test_output, test_answer)

            for x in ["lock", "unlock"]:
                for y in ["north", "south", "east", "west", "exit 1", "exit 2", "exit 3", "exit 4", "exit 5"]:
                    test_answer = ['error', 'not a command', '', '']
                    test_input = x + " " + y
                    test_output = self.command_parser.simplify_command(test_input)
                    self.assertEqual(test_output, test_answer)

if __name__ == "__main__":
    unittest.main()
