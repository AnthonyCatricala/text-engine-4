from Util.RoomUtil import *

import os
import unittest

PROJECT_DIR = os.path.abspath(os.path.join(os.path.join(__file__, os.pardir), os.pardir))
os.chdir(PROJECT_DIR)


class TestApiFunctions(unittest.TestCase):

    def test_change_room_name(self):
        test_room = load_room(room_file="./Tests/Rooms/Test_Room.room")
        change_room_name(test_room, "New Name")

        expected_room_name = "New Name"
        self.assertEqual(expected_room_name, test_room.room_name)

        self.assertTrue(os.path.isfile(test_room.room_file))

        test_room = load_room()
        self.assertEqual(None, test_room)

    def test_change_room_description(self):
        test_room = load_room(room_file="./Tests/Rooms/Test_Room.room")
        change_room_description(test_room, "Changed description")

        expected_description = "Changed description"
        self.assertEqual(expected_description, test_room.description)

        # Description does not change if invalid arguments have been supplied
        change_room_description()
        self.assertEqual(expected_description, test_room.description)

        change_room_description(test_room)
        self.assertEqual(expected_description, test_room.description)

        change_room_description(room_description="Changed description")
        self.assertEqual(expected_description, test_room.description)

    def test_room_illumination(self):
        test_room = load_room(room_file="./Tests/Rooms/Test_Room.room")

        self.assertTrue(test_room.illuminated)

        remove_light_from_room(test_room)
        self.assertFalse(test_room.illuminated)

        add_light_to_room(test_room)
        self.assertTrue(test_room.illuminated)

    def test_room_creation(self):
        test_room = create_room("Unit Test Room", "Unit test room description.")
        self.assertTrue(type(test_room) == Room)

        file_created = os.path.isfile(test_room.room_file)
        self.assertTrue(file_created)

        if file_created:
            os.remove(test_room.room_file)
            self.assertFalse(os.path.isfile(test_room.room_file))

    def test_load_room(self):
        test_room = load_room("Test Room")

        expected_room_name = "Test Room"
        self.assertEqual(expected_room_name, test_room.room_name)

        expected_room_file = "./Rooms/Test_Room.room"
        self.assertEqual(expected_room_file, test_room.room_file)

        expected_room_description = "This is the room's description"
        self.assertEqual(expected_room_description, test_room.description)

        expected_room_illumination = True
        self.assertEqual(expected_room_illumination, test_room.illuminated)

        expected_exit_size = 4
        self.assertEqual(expected_exit_size, len(test_room.exits))

        expected_inventory = []
        self.assertEqual(expected_inventory, test_room.inventory)

        expected_triggers = []
        self.assertEqual(expected_triggers, test_room.triggers)

    # TODO Don't require user input.
    def test_invalid_room_load(self):
        test_room = load_room("Room that doesn't exist")
        self.assertEqual(None, test_room)

        test_room = load_room()
        self.assertEqual(None, test_room)

    def test_save_room(self):
        test_room = create_room("Room Save", "Room save description.")

        if os.path.isfile(test_room.room_file):
            os.remove(test_room.room_file)
        self.assertFalse(os.path.isfile(test_room.room_file))

        save_room(test_room)
        self.assertTrue(os.path.isfile(test_room.room_file))

        if os.path.isfile(test_room.room_file):
            os.remove(test_room.room_file)

        self.assertFalse(os.path.isfile(test_room.room_file))

    def test_door_creation(self):
        test_door = create_door()

        self.assertTrue(type(test_door) is Door)
        self.assertFalse(test_door.is_open)
        self.assertEqual(None, test_door.lock)
        self.assertEqual([], test_door.triggers)

if __name__ == "__main__":
    unittest.main()
