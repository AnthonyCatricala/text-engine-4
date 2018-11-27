
import unittest
from Help import HelpMenu
import os

PROJECT_DIR = os.path.abspath(os.path.join(os.path.join(__file__, os.pardir), os.pardir))
os.chdir(PROJECT_DIR)


class TestHelpMenu(unittest.TestCase):

    help_menu = HelpMenu()

    # Tests help command with no other arguments
    def test_help(self):
        test_answer = self.help_menu.help()
        test_output = self.help_menu.help()
        self.assertEqual(test_answer, test_answer)

    def test_help_(self):
        test_answer = self.help_menu.HelpMenu.help()
        self.assertEqual(test_answer, "look\nUse the look command to look at the surroundings of the room you are in as well as its contents.")