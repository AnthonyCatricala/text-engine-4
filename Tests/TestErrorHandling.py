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
            error_handler(test_function, test_reason)
        finally:
            sys.stdout = original_std_out

        return str(test_std_out)

    def hold(self):
        test_function = ''
        test_reason = ''
        expected_output = ''
        self.assertEqual(expected_output, self.get_output_string(test_function, test_reason))

    def test_change_room_description(self):
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


if __name__ == "__main__":
    unittest.main()
