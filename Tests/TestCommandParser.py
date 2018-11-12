from Util.RoomUtil import *
from Parser.UserParser import UserParser

import os
import unittest

# TODO The project should run from any directory.
PROJECT_DIR = os.path.abspath(os.path.join(os.path.join(__file__, os.pardir), os.pardir))
os.chdir(PROJECT_DIR)


class TestCommandParser(unittest.TestCase):
    room = load_room('Test Room')
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

    # All tests that should result in a go command.
    def test_go(self):
        # Go [compass direction] should result in output primary command being go,
        # and primary object being the compass direction.
        test_answer = ['go', 'north', '', '']
        test_input = 'go north'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['go', 'south', '', '']
        test_input = 'go south'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['go', 'east', '', '']
        test_input = 'go east'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['go', 'west', '', '']
        test_input = 'go west'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        # Move commands should map to go primary commands.
        test_answer = ['go', 'north', '', '']
        test_input = 'move north'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['go', 'south', '', '']
        test_input = 'move south'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['go', 'east', '', '']
        test_input = 'move east'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['go', 'west', '', '']
        test_input = 'move west'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        # Walk commands should map to go primary commands.
        test_answer = ['go', 'north', '', '']
        test_input = 'walk north'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['go', 'south', '', '']
        test_input = 'walk south'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['go', 'east', '', '']
        test_input = 'walk east'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['go', 'west', '', '']
        test_input = 'walk west'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        # Move commands should map to go primary commands.
        test_answer = ['go', 'north', '', '']
        test_input = 'run north'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['go', 'south', '', '']
        test_input = 'run south'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['go', 'east', '', '']
        test_input = 'run east'
        test_output = self.command_parser.simplify_command(test_input)
        self.assertEqual(test_output, test_answer)

        test_answer = ['go', 'east', '', '']
        test_input = 'run west'
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


if __name__ == "__main__":
    unittest.main()
