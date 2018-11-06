from Util.ErrorUtil import *

import os
import unittest

PROJECT_DIR = os.path.abspath(os.path.join(os.path.join(__file__, os.pardir), os.pardir))
os.chdir(PROJECT_DIR)


class StdOut(object):
    def __init__(self):
        self.data = []

    def write(self, s):
        self.data.append(s)

    def __str__(self):
        return "".join(self.data)


class TestErrorHandling(unittest.TestCase):

    @staticmethod
    def get_output_string(test_function, test_reason):
        original_std_out = sys.stdout
        test_std_out = StdOut()
        try:
            sys.stdout = test_std_out
            error_handler(test_function, test_reason, testing=True)
        finally:
            sys.stdout = original_std_out

        return str(test_std_out)

    def test_change_room_name(self):
        test_function = 'change_room_name'
        expected_output_header = 'It looks like you\'re trying to change the name of a room, '

        test_reason = 'no name'
        expected_output = expected_output_header + 'but haven\'t given a room name.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

        test_reason = 'invalid format'
        expected_output = expected_output_header + 'but did not use the command in the correct format.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

        test_reason = 'no room'
        expected_output = expected_output_header + 'but did not specify which room you want to edit.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

    def test_change_room_description(self):
        test_function = 'change_room_description'
        expected_output_header = 'It looks like you\'re trying to change a room\'s description, '

        test_reason = 'no description'
        expected_output = expected_output_header + 'but haven\'t given a new description for the room.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

        test_reason = 'invalid format'
        expected_output = expected_output_header + 'but did not use the command in the correct format.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

        test_reason = 'no room'
        expected_output = expected_output_header + 'but did not specify which room you want to edit.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

    def test_add_light_to_room(self):
        test_function = 'add_light_to_room'
        expected_output_header = 'It looks like you\'re trying to add a light to a room, '

        test_reason = 'invalid object'
        expected_output = expected_output_header + 'but you haven\'t given the command a valid object.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

        test_reason = 'invalid type'
        expected_output = expected_output_header + 'but did not use a valid type.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

        test_reason = 'no object'
        expected_output = expected_output_header + 'but did not supply an object for the Room argument.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

    def test_remove_light_from_room(self):
        test_function = 'remove_light_from_room'
        expected_output_header = 'It looks like you\'re trying to remove a light from a room, '

        test_reason = 'invalid object'
        expected_output = expected_output_header + 'but you haven\'t given the command a valid object.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

        test_reason = 'invalid type'
        expected_output = expected_output_header + 'but did not use a valid type.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

        test_reason = 'no object'
        expected_output = expected_output_header + 'but did not supply an object for the Room argument.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

    def test_create_room(self):
        test_function = 'create_room'
        expected_output_header = 'It looks like you\'re trying to create a room, '

        test_reason = 'no description'
        expected_output = expected_output_header + 'but haven\'t given a description for your new room.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

        test_reason = 'no name'
        expected_output = expected_output_header + 'but haven\'t given a name for your new room.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

    def test_load_room(self):
        test_function = 'load_room'
        expected_output_header = 'It looks like you\'re trying to load a room, '

        test_reason = 'file does not exist'
        expected_output = expected_output_header + 'but the file you\'re trying to load doesn\'t exist.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

        test_reason = 'illegal file path'
        expected_output = expected_output_header + 'but you\'ve given an invalid file path.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

        test_reason = 'too many arguments'
        expected_output = expected_output_header + 'but you\'ve given too many arguments in your function.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

        test_reason = 'no arguments'
        expected_output = expected_output_header + 'but you haven\'t put any arguments in your function.\n'
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))


if __name__ == "__main__":
    unittest.main()
