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
    room = load_room(room_file='Tests/Rooms/RoomTester.room')
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
        expected_output = 'There is no exit in that direction.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['go', 'south', '', '']
        expected_output = 'There is no exit in that direction.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['go', 'east', '', '']
        expected_output = 'There is no exit in that direction.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['go', 'west', '', '']
        expected_output = 'There is no exit in that direction.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['go', 'exit_1', '', '']
        expected_output = 'You move to RoomTester.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

        test_input = ['go', 'exit_2', '', '']
        expected_output = 'The door seems to be locked.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

        test_input = ['go', 'exit_3', '', '']
        expected_output = 'You move to RoomTester.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

        test_input = ['go', 'exit_4', '', '']
        expected_output = 'The door blocks your path.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['go', 'exit_5', '', '']
        expected_output = 'There is something in the way.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

    def test_open(self):
        test_input = ['open', 'exit_1', '', '']
        expected_output = 'exit_1 door was already open.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['open', 'exit_2', '', '']
        expected_output = 'exit_2 door was locked closed.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['open', 'exit_3', '', '']
        expected_output = 'exit_3 door was already open.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['open', 'exit_4', '', '']
        expected_output = 'exit_4 door is now open.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['open', 'invalid exit', '', '']
        expected_output = 'That is not a valid exit, thus there was no door.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['open', 'exit_5', '', '']
        expected_output = 'exit_5 does not have a door.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

    def test_close(self):
        test_input = ['close', 'exit_1', '', '']
        expected_output = 'exit_1 door was locked open.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['close', 'exit_2', '', '']
        expected_output = 'exit_2 door was already closed.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['close', 'exit_3', '', '']
        expected_output = 'exit_3 door is now closed.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['close', 'exit_4', '', '']
        expected_output = 'exit_4 door was already closed.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['close', 'invalid exit', '', '']
        expected_output = 'That is not a valid exit, thus there was no door.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['close', 'exit_5', '', '']
        expected_output = 'exit_5 does not have a door.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

    def test_lock(self):
        test_input = ['lock', 'exit_1', '', '']
        expected_output = 'exit_1 door was already locked.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['lock', 'exit_2', '', '']
        expected_output = 'exit_2 door was already locked.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['lock', 'exit_3', '', '']
        expected_output = 'exit_3 door is now locked.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['lock', 'exit_4', '', '']
        expected_output = 'exit_4 door has no lock.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['lock', 'invalid exit', '', '']
        expected_output = 'That is not a valid exit, thus there was no door.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['open', 'exit_5', '', '']
        expected_output = 'exit_5 does not have a door.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

    def test_unlock(self):
        test_input = ['unlock', 'exit_1', '', '']
        expected_output = 'exit_1 door is now unlocked.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['unlock', 'exit_2', '', '']
        expected_output = 'exit_2 door is now unlocked.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        #test_input = ['unlock', 'exit_3', '', '']
        #expected_output = 'exit_3 door was already unlocked.\n'
        #self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['unlock', 'exit_4', '', '']
        expected_output = 'exit_4 door has no lock.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['unlock', 'invalid exit', '', '']
        expected_output = 'That is not a valid exit, thus there was no door.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['unlock', 'exit_5', '', '']
        expected_output = 'exit_5 does not have a door.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

if __name__ == "__main__":
    unittest.main()
