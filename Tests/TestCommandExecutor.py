from Util.RoomUtil import *
from Parser.CommandExecuter import CommandExecutor

import os
import sys
import unittest

# TODO The project should run from any directory.
PROJECT_DIR = os.path.abspath(os.path.join(os.path.join(__file__, os.pardir), os.pardir))
os.chdir(PROJECT_DIR)


class StdOut(object):
    def __init__(self):
        self.data = []

    def write(self, s):
        self.data.append(s)

    def __str__(self):
        return "".join(self.data)


class TestCommandParser(unittest.TestCase):
    room = load_room("Test_Room")
    ce = CommandExecutor(room, None)

    def get_output_string(self, test_input):
        original_std_out = sys.stdout
        test_std_out = StdOut()
        try:
            sys.stdout = test_std_out
            self.ce.executor(test_input)
        finally:
            sys.stdout = original_std_out

        return str(test_std_out)

    # Testing empty input.
    def test_empty(self):
        test_input = ['', '', '', '']
        expected_output = ''
        self.assertEqual(self.get_output_string(test_input), expected_output)

    # All tests that should result in the look command.
    def test_look(self):
        test_input = ['look', '', '', '']
        expected_output = 'This is the room\'s description\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

    def test_go(self):
        test_input = ['go', 'north', '', '']
        expected_output = 'You move to Test Room.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

        test_input = ['go', 'south', '', '']
        expected_output = 'The door blocks your path.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

        test_input = ['go', 'east', '', '']
        expected_output = 'The door seems to be locked.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

        test_input = ['go', 'west', '', '']
        expected_output = 'You move to Test Room.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)


if __name__ == "__main__":
    unittest.main()
