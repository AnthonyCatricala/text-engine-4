from Util.RoomUtil import *
from Parser.CommandExecuter import CommandExecutor
from Objects.Character import Player

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
    p_inv = [
        Item("player_item_1", "look player item 1.", [], 100, True, False, True, [],
             [Door(True, [Lock(False, "", [], [])], [], [])], [], []),
        Item("player_item_2", "look player item 2.", [], 100, True, False, True, [],
             [Door( True, None, [], [])], [], []),
        Item("player_item_3","look player item 3.",[], 100, True, False, True, [], {}, [], []),
        Item("invisible_player_item","look player item 3.",[], 100, False, False, True, [], {}, [], [])
    ]
    r_inv = [
        Item("room_item_1", "look room item 1.", [], 100, True, False, True, [],
             [Door(True, [Lock(False, "", [], [])], [], [])], [], []),
        Item("room_item_2", "look room item 2.", [], 100, True, False, True, [],
             [Door( True, None, [], [])], [], []),
        Item("room_item_3","look room item 3.",[], 100, True, False, True, [], {}, [], []),
        Item("invisible_room_item","look room item 3.",[], 100, False, False, True, [], {}, [], [])
    ]
    room.inventory = r_inv
    player = Player("player", p_inv, "Player description", None)
    ce = CommandExecutor(room, player)

    def get_output_string(self, test_input):
        original_std_out = sys.stdout
        test_std_out = StdOut()
        try:
            sys.stdout = test_std_out
            self.ce.executor(test_input)
        finally:
            sys.stdout = original_std_out

        return str(test_std_out)

    def test_empty(self):
        test_input = ['', '', '', '']
        expected_output = '\n RoomTester\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

    def test_look(self):
        #Dark Room check
        self.room.illuminated = False
        test_input = ['look', '', '', '']
        expected_output = "\n RoomTester\nIt's too dark!\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        #Normal checks
        self.room.illuminated = True
        test_input = ['look', '', '', '']
        expected_output = "\n RoomTester\nThis is the room's description\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        #Exit check
        test_input = ['look', 'exit', 'exit', 'exit_1']
        expected_output = '\n RoomTester\nlook exit 1\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'door', 'exit', 'exit_1']
        expected_output = "\n RoomTester\ndoors don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'lock', 'exit', 'exit_1']
        expected_output = "\n RoomTester\nlocks don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'exit', 'exit', 'exit_2']
        expected_output = '\n RoomTester\nlook exit 2\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'door', 'exit', 'exit_2']
        expected_output = "\n RoomTester\ndoors don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'lock', 'exit', 'exit_2']
        expected_output = "\n RoomTester\nlocks don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'exit', 'exit', 'exit_3']
        expected_output = '\n RoomTester\nlook exit 3\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'door', 'exit', 'exit_3']
        expected_output = "\n RoomTester\ndoors don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'lock', 'exit', 'exit_3']
        expected_output = "\n RoomTester\nlocks don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        # Player inventory
        test_input = ['look', 'player_item', 'player_item', 'player_item_1']
        expected_output = '\n RoomTester\nlook player item 1.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'door', 'player_item', 'player_item_1']
        expected_output = "\n RoomTester\ndoors don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'lock', 'player_item', 'player_item_1']
        expected_output = "\n RoomTester\nlocks don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'player_item', 'player_item', 'player_item_2']
        expected_output = '\n RoomTester\nlook player item 2.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'door', 'player_item', 'player_item_2']
        expected_output = "\n RoomTester\ndoors don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'lock', 'player_item', 'player_item_2']
        expected_output = "\n RoomTester\nlocks don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'player_item', 'player_item', 'player_item_3']
        expected_output = '\n RoomTester\nlook player item 3.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'door', 'player_item', 'player_item_3']
        expected_output = "\n RoomTester\ndoors don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'lock', 'player_item', 'player_item_3']
        expected_output = "\n RoomTester\nlocks don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        # Room inventory check
        test_input = ['look', 'room_item', 'room_item', 'room_item_1']
        expected_output = '\n RoomTester\nlook room item 1.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'door', 'room_item', 'room_item_1']
        expected_output = "\n RoomTester\ndoors don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'lock', 'room_item', 'room_item_1']
        expected_output = "\n RoomTester\nlocks don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'room_item', 'room_item', 'room_item_2']
        expected_output = '\n RoomTester\nlook room item 2.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'door', 'room_item', 'room_item_2']
        expected_output = "\n RoomTester\ndoors don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'lock', 'room_item', 'room_item_2']
        expected_output = "\n RoomTester\nlocks don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'room_item', 'room_item', 'room_item_3']
        expected_output = '\n RoomTester\nlook room item 3.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'door', 'room_item', 'room_item_3']
        expected_output = "\n RoomTester\ndoors don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'lock', 'room_item', 'room_item_3']
        expected_output = "\n RoomTester\nlocks don't have a description.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'exit', 'exit', 'north']
        expected_output = '\n RoomTester\nNo description given.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'door', 'exit', 'north']
        expected_output = "\n RoomTester\nNo description given.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'lock', 'exit', 'north']
        expected_output = "\n RoomTester\nNo description given.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        test_input = ['look', 'room_item', 'room_item', 'invisible_room_item']
        expected_output = "\n RoomTester\nYou can't see that item.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)

    def test_block(self):
        test_input = ['block', 'exit_1', 'exit', '']
        expected_output = '\n RoomTester\nexit_1 door is now blocked.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.exits[0].blocked = True
        test_input = ['block', 'exit_1', 'exit', '']
        expected_output = '\n RoomTester\nexit_1 door was already blocked.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.exits[0].blocked = False
        test_input = ['block', 'fake', 'exit', '']
        expected_output = '\n RoomTester\nThat is not a valid exit.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

    def test_unblock(self):
        test_input = ['unblock', 'exit_1', 'exit', '']
        expected_output = '\n RoomTester\nexit_1 door was already unblocked.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.exits[0].blocked = True
        test_input = ['unblock', 'exit_1', 'exit', '']
        expected_output = '\n RoomTester\nexit_1 door is now unblocked.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.exits[0].blocked = False
        test_input = ['block', 'fake', 'exit', '']
        expected_output = '\n RoomTester\nThat is not a valid exit.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

    def test_inventory(self):
        #TODO it worked fine
        #test_input = ['inventory', '', '', '']
        #expected_output = '\n RoomTester\ninventory:\nplayer_item_1\nplayer_item_2\nplayer_item_3\ninvisible_player_item\n'
        #self.assertEqual(self.get_output_string(test_input), expected_output)
        #self.player.inventory = []
        test_input = ['inventory', '', '', '']
        expected_output = '\n RoomTester\ninventory:\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)

    def test_get(self):
        # General pick up test
        self.room.inventory.clear()
        self.room.inventory.append(Item("test_item", "testing_item.", [], 3, True, False, True, [], {}, [],[]))
        self.room.save()
        self.player.inventory.clear()
        test_input = ['get', 'test_item', 'room_item', '']
        expected_output = '\n RoomTester\ntook test_item\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)   # Item was picked up
        self.assertEqual(self.room.inventory[0].quantity, 2)   # counter works
        self.assertEqual(self.player.inventory[0].quantity, 1)   # adding items worked
        test_input = ['get', 'test_item', 'room_item', '']
        expected_output = '\n RoomTester\ntook test_item\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)   # item was picked up
        self.assertEqual(self.room.inventory[0].quantity, 1)   # decrease counter works
        self.assertEqual(self.player.inventory[0].quantity, 2)   # increase counter works
        test_input = ['get', 'test_item', 'room_item', '']
        expected_output = '\n RoomTester\ntook test_item\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)   # item was picked up
        self.assertEqual(self.room.inventory, [])   # item was deleted from inventory
        self.assertEqual(self.player.inventory[0].quantity, 3)   # counter increase worked
        # invisible, can still pick up invisible things
        self.player.inventory.clear()
        self.room.inventory.clear()
        self.room.inventory.append(Item("test_item", "testing_item.", [], 1, False, False, True, [], {}, [],[]))
        self.room.save()
        test_input = ['get', 'test_item', 'room_item', '']
        expected_output = '\n RoomTester\ntook test_item\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)   # item was picked up
        self.assertEqual(self.room.inventory, [])   # item was deleted from inventory
        self.assertEqual(self.player.inventory[0].quantity, 1)   # counter increase worked
        # reset
        self.player.inventory.clear()
        self.room.inventory.append(Item("test_item", "testing_item.", [], 3, True, False, False, [], {}, [],[]))
        self.room.save()
        test_input = ['get', 'test_item', 'room_item', '']
        expected_output = '\n RoomTester\ntest item is not obtainable!\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)   # item wasnt picked up
        self.assertEqual(len(self.room.inventory), 1)   # item remains in inventory
        self.assertEqual(self.player.inventory, [])   # counter remains
        # reset
        self.room.inventory.clear()
        self.room.save()
        self.player.inventory.clear()

    def test_drop(self):
        self.room.inventory.clear()
        self.room.save()
        self.player.inventory.clear()
        self.player.inventory.append(Item("test_item", "testing_item.", [], 3, True, False, True, [], {}, [],[]))
        test_input = ['drop', 'test_item', 'player_item', '']
        expected_output = '\n RoomTester\ndropped test_item\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)   # Item was dropped
        self.assertEqual(self.player.inventory[0].quantity, 2)   # counter works
        self.assertEqual(self.room.inventory[0].quantity, 1)   # dropping items worked
        test_input = ['drop', 'test_item', 'player_item', '']
        expected_output = '\n RoomTester\ndropped test_item\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)   # item was dropped
        self.assertEqual(self.player.inventory[0].quantity, 1)   # decrease counter works
        self.assertEqual(self.room.inventory[0].quantity, 2)   # increase counter works
        test_input = ['drop', 'test_item', 'room_item', '']
        expected_output = '\n RoomTester\ndropped test_item\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)   # item was dropped
        self.assertEqual(self.player.inventory, [])   # item was deleted from inventory
        self.assertEqual(self.room.inventory[len(self.room.inventory)-1].quantity, 3)   # counter increase worked
        # invisible, can still pick up invisible things
        self.room.inventory.clear()
        self.room.save()
        self.player.inventory.append(Item("test_item", "testing_item.", [], 1, False, False, True, [], {}, [],[]))
        test_input = ['drop', 'test_item', 'room_item', '']
        expected_output = '\n RoomTester\ndropped test_item\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)   # item was picked up
        self.assertEqual(self.player.inventory, [])   # item was deleted from inventory
        self.assertEqual(self.room.inventory[0].quantity, 1)   # counter increase worked
        # reset
        self.room.inventory.clear()
        self.room.save()
        self.player.inventory.append(Item("test_item", "testing_item.", [], 1, True, False, False, [], {}, [],[]))
        test_input = ['drop', 'test_item', 'room_item', '']
        expected_output = '\n RoomTester\ndropped test_item\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)   # item was dropped
        self.assertEqual(self.player.inventory, [])   # item was deleted from inventory
        self.assertEqual(self.room.inventory[0].quantity, 1)   # counter increase worked
        # reset
        self.room.inventory.clear()
        self.room.save()

    def test_go_exit_1(self):
        # Exit 1
        room_trans = load_room(room_file="./Tests/Rooms/RoomTesterTransverse.room") # Exit leads to a room on the other side
        self.room.exits[0].links_to = "./Tests/Rooms/RoomTesterTransverse.room"
        self.room.exits[1].links_to = ""
        self.room.exits[2].links_to = ""
        room_trans.exits[0].links_to = ""
        room_trans.exits[1].links_to = ""
        room_trans.exits[2].links_to = ""
        room_trans.exits[0].door.lock.is_locked = False
        self.room.exits[0].door.lock.is_locked = False
        room_trans.exits[0].door.is_open = True
        self.room.exits[0].door.is_open = True
        self.room.exits[0].blocked = False
        room_trans.exits[0].blocked = False
        self.room.save()
        room_trans.save()
        # Tests
        test_input = ['go', 'north', 'exit', '']   # invalid exit
        expected_output = '\n RoomTester\nThere is no exit in that direction.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # exit links on one side
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # Exit links on both sides
        room_trans.exits[0].links_to = "./Tests/Rooms/RoomTester.room"
        room_trans.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # blocked on one side
        self.room.exits[0].blocked = True
        self.room.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = '\n RoomTester\nThere is something blocking the exit_1 exit of the RoomTester. ' \
                          'You cannot enter.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # blocked other side
        self.room.exits[0].blocked = False
        room_trans.exits[0].blocked = True
        self.room.save()
        room_trans.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = '\n RoomTester \nThere is something blocking the exit_1_transverse exit of the RoomTesterTransverse. ' \
                          'You cannot enter.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # exit is locked open on one side
        room_trans.exits[0].blocked = False
        room_trans.exits[0].door.lock.is_locked = True
        room_trans.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # exit is locked open both sides
        self.room.exits[0].door.lock.is_locked = True
        self.room.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # exit is locked open on other side
        room_trans.exits[0].door.lock.is_locked = False
        room_trans.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # exit is closed on both sides
        room_trans.exits[0].door.lock.is_locked = False
        self.room.exits[0].door.lock.is_locked = False
        room_trans.exits[0].door.is_open = False
        self.room.exits[0].door.is_open = False
        self.room.save()
        room_trans.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nThe exit_1 door is closed. You can try to open the door.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # exit is closed locked on one side
        room_trans.exits[0].door.lock.is_locked = True
        room_trans.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nThe exit_1 door is closed. You can try to open the door.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # exit is closed locked on both sides
        self.room.exits[0].door.lock.is_locked = True
        self.room.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nThe RoomTester's exit_1 door seems to be locked. You cannot enter.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # exit is closed locked on other side
        room_trans.exits[0].door.lock.is_locked = False
        room_trans.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nThe RoomTester's exit_1 door seems to be locked. You cannot enter.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        # Reset
        room_trans.exits[0].links_to = ""
        room_trans.exits[0].door.lock.is_locked = False
        self.room.exits[0].door.lock.is_locked = False
        room_trans.exits[0].door.is_open = True
        self.room.exits[0].door.is_open = True
        self.room.exits[0].blocked = False
        room_trans.exits[0].blocked = False
        self.room.save()
        room_trans.save()
        # Exit 2
        room_trans.exits[1].links_to = "./Tests/Rooms/RoomTester.room"
        room_trans.exits[1].door.is_open = True
        room_trans.save()
        test_input = ['go', 'exit_1', 'exit', '']   # normal all open
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   #locked open
        self.room.exits[0].door.lock.is_locked = True
        self.room.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   #closed both sides
        self.room.exits[0].door.lock.is_locked = False
        self.room.exits[0].door.is_open = False
        room_trans.exits[1].door.is_open = False
        self.room.save()
        room_trans.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nThe exit_1 door is closed. You can try to open the door.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   #closed locked
        self.room.exits[0].door.lock.is_locked = True
        self.room.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nThe RoomTester's exit_1 door seems to be locked. You cannot enter.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        # reset
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")
        self.room.exits[0].door.lock.is_locked = False
        room_trans.exits[1].door.is_open = True
        self.room.exits[0].door.is_open = True
        room_trans.exits[1].links_to = ""
        self.room.save()
        room_trans.save()
        # exit 3
        room_trans.exits[2].links_to = "./Tests/Rooms/RoomTester.room"  # general open
        room_trans.save()
        test_input = ['go', 'exit_1', 'exit', '']   # normal all open
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # Locked open
        self.room.exits[0].door.lock.is_locked = True
        self.room.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # closed
        self.room.exits[0].door.lock.is_locked = False
        self.room.exits[0].door.is_open = False
        self.room.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nThe exit_1 door is closed. You can try to open the door.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   #closed locked
        self.room.exits[0].door.lock.is_locked = True
        self.room.save()
        test_input = ['go', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nThe RoomTester's exit_1 door seems to be locked. You cannot enter.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        # reset
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")
        self.room.exits[0].door.lock.is_locked = False
        self.room.exits[0].door.is_open = True
        room_trans.exits[2].links_to = ""
        self.room.exits[0].links_to = ""
        self.room.save()
        room_trans.save()

    def test_go_exit_2(self):
        # Exit 1
        room_trans = load_room(room_file="./Tests/Rooms/RoomTesterTransverse.room") # Exit leads to a room on the other side
        self.room.exits[1].links_to = "./Tests/Rooms/RoomTesterTransverse.room"
        self.room.exits[0].links_to = ""
        self.room.exits[2].links_to = ""
        room_trans.exits[0].links_to = ""
        room_trans.exits[1].links_to = ""
        room_trans.exits[2].links_to = ""
        room_trans.exits[0].door.lock.is_locked = False
        room_trans.exits[0].door.is_open = True
        self.room.exits[1].door.is_open = True
        self.room.exits[1].blocked = False
        room_trans.exits[0].blocked = False
        self.room.save()
        room_trans.save()
        #Tests
        test_input = ['go', 'exit_2', 'exit', '']   #exit links on one side
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # Exit links on both sides
        room_trans.exits[0].links_to = "./Tests/Rooms/RoomTester.room"
        room_trans.save()
        test_input = ['go', 'exit_2', 'exit', '']
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # blocked on one side
        self.room.exits[1].blocked = True
        self.room.save()
        test_input = ['go', 'exit_2', 'exit', '']
        expected_output = '\n RoomTester\nThere is something blocking the exit_2 exit of the RoomTester. ' \
                          'You cannot enter.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # blocked other side
        self.room.exits[1].blocked = False
        room_trans.exits[0].blocked = True
        self.room.save()
        room_trans.save()
        test_input = ['go', 'exit_2', 'exit', '']
        expected_output = '\n RoomTester \nThere is something blocking the exit_1_transverse exit of the RoomTesterTransverse. ' \
                          'You cannot enter.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # exit is locked open on one side
        room_trans.exits[0].blocked = False
        room_trans.exits[0].door.lock.is_locked = True
        room_trans.save()
        test_input = ['go', 'exit_2', 'exit', '']
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # exit is closed on one side
        room_trans.exits[0].door.lock.is_locked = False
        room_trans.exits[0].door.is_open = False
        self.room.exits[1].door.is_open = False
        self.room.save()
        room_trans.save()
        test_input = ['go', 'exit_2', 'exit', '']
        expected_output = "\n RoomTester\nThe exit_2 door is closed. You can try to open the door.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        # Reset
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")
        room_trans.exits[0].links_to = ""
        room_trans.exits[0].door.lock.is_locked = False
        room_trans.exits[0].door.is_open = True
        self.room.exits[1].door.is_open = True
        self.room.exits[1].blocked = False
        room_trans.exits[0].blocked = False
        self.room.save()
        room_trans.save()
        # Exit 2
        room_trans.exits[1].links_to = "./Tests/Rooms/RoomTester.room"
        test_input = ['go', 'exit_2', 'exit', '']   # normal all open
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   #closed both sides
        room_trans.exits[1].door.is_open = False
        self.room.exits[1].door.is_open = False
        self.room.save()
        room_trans.save()
        test_input = ['go', 'exit_2', 'exit', '']
        expected_output = "\n RoomTester\nThe exit_2 door is closed. You can try to open the door.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        # reset
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")
        room_trans.exits[1].door.is_open = True
        self.room.exits[1].door.is_open = True
        room_trans.exits[1].links_to = ""
        self.room.save()
        room_trans.save()
        # exit 3
        room_trans.exits[2].links_to = "./Tests/Rooms/RoomTester.room"  # general open
        room_trans.save()
        test_input = ['go', 'exit_2', 'exit', '']   # normal all open
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # closed
        self.room.exits[1].door.is_open = False
        self.room.save()
        test_input = ['go', 'exit_2', 'exit', '']
        expected_output = "\n RoomTester\nThe exit_2 door is closed. You can try to open the door.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        # reset
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")
        room_trans.exits[2].links_to = ""
        self.room.exits[1].links_to = ""
        self.room.save()
        room_trans.save()

    def test_go_exit_3(self):
        # Exit 1
        room_trans = load_room(room_file="./Tests/Rooms/RoomTesterTransverse.room") # Exit leads to a room on the other side
        self.room.exits[2].links_to = "./Tests/Rooms/RoomTesterTransverse.room"
        self.room.exits[0].links_to = ""
        self.room.exits[1].links_to = ""
        room_trans.exits[0].links_to = ""
        room_trans.exits[1].links_to = ""
        room_trans.exits[2].links_to = ""
        room_trans.exits[0].door.lock.is_locked = False
        room_trans.exits[0].door.is_open = True
        self.room.exits[2].blocked = False
        room_trans.exits[0].blocked = False
        self.room.save()
        room_trans.save()
        #Tests
        test_input = ['go', 'exit_3', 'exit', '']   #exit links on one side
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # Exit links on both sides
        room_trans.exits[0].links_to = "./Tests/Rooms/RoomTester.room"
        room_trans.save()
        test_input = ['go', 'exit_3', 'exit', '']
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # blocked on one side
        self.room.exits[2].blocked = True
        self.room.save()
        test_input = ['go', 'exit_3', 'exit', '']
        expected_output = '\n RoomTester\nThere is something blocking the exit_3 exit of the RoomTester. ' \
                          'You cannot enter.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # blocked other side
        self.room.exits[2].blocked = False
        room_trans.exits[0].blocked = True
        self.room.save()
        room_trans.save()
        test_input = ['go', 'exit_3', 'exit', '']
        expected_output = '\n RoomTester \nThere is something blocking the exit_1_transverse exit of the RoomTesterTransverse. ' \
                          'You cannot enter.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # exit is locked open on one side
        room_trans.exits[0].blocked = False
        room_trans.exits[0].door.lock.is_locked = True
        room_trans.save()
        test_input = ['go', 'exit_3', 'exit', '']
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # exit is closed on one sides
        room_trans.exits[0].door.lock.is_locked = False
        room_trans.exits[0].door.is_open = False
        room_trans.save()
        test_input = ['go', 'exit_3', 'exit', '']
        expected_output = "\n RoomTester \nThe door is closed on the other side. You cannot enter.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   # locked closed other side
        room_trans.exits[0].door.lock.is_locked = False
        room_trans.save()
        test_input = ['go', 'exit_3', 'exit', '']
        expected_output = "\n RoomTester \nThe door is closed on the other side. You cannot enter.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)

        # Reset
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")
        room_trans.exits[0].links_to = ""
        room_trans.exits[0].door.lock.is_locked = False
        room_trans.exits[0].door.is_open = True
        self.room.exits[2].blocked = False
        room_trans.exits[0].blocked = False
        self.room.save()
        room_trans.save()
        # Exit 2
        room_trans.exits[1].links_to = "./Tests/Rooms/RoomTester.room"
        room_trans.exits[1].door.is_open = True
        room_trans.save()
        test_input = ['go', 'exit_3', 'exit', '']   # normal all open
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")   #closed both sides
        room_trans.exits[1].door.is_open = False
        self.room.save()
        room_trans.save()
        test_input = ['go', 'exit_3', 'exit', '']
        expected_output = "\n RoomTester \nThe door is closed on the other side. You cannot enter.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        # reset
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")
        room_trans.exits[1].door.is_open = True
        room_trans.exits[1].links_to = ""
        self.room.save()
        room_trans.save()
        # exit 3
        room_trans.exits[2].links_to = "./Tests/Rooms/RoomTester.room"  # general open
        room_trans.save()
        test_input = ['go', 'exit_3', 'exit', '']   # normal all open
        expected_output = '\nRoomTesterTransverse\nTransferred rooms.\n'
        self.assertEqual(self.get_output_string(test_input), expected_output)
        # reset
        self.room.load(room_file="./Tests/Rooms/RoomTester.room")
        room_trans.exits[2].links_to = ""
        self.room.exits[2].links_to = ""
        self.room.save()
        room_trans.save()

    def test_unlock_exit_1(self):
        #exit_1
        room_trans = load_room(room_file="./Tests/Rooms/RoomTesterTransverse.room") # Exit leads to a room on the other side
        self.room.exits[0].links_to = "./Tests/Rooms/RoomTesterTransverse.room"
        self.room.exits[1].links_to = ""
        self.room.exits[2].links_to = ""
        room_trans.exits[0].links_to = ""
        room_trans.exits[1].links_to = ""
        room_trans.exits[2].links_to = ""
        room_trans.exits[0].door.lock.is_locked = False
        self.room.exits[0].door.lock.is_locked = False
        room_trans.exits[0].door.is_open = True
        self.room.exits[0].door.is_open = True
        self.room.exits[0].blocked = False
        self.room.exits[0].door.lock.key = ""
        room_trans.exits[0].door.lock.key = ""
        room_trans.exits[0].blocked = False
        self.room.save()
        room_trans.save()
        test_input = ['unlock', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nexit_1 you don't have the key.\n" # unlocked no key
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.assertEqual(self.room.exits[0].door.lock.is_locked, False)
        room_trans.exits[0].links_to = "./Tests/Rooms/RoomTester.room"
        room_trans.save()
        test_input = ['unlock', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nexit_1 you don't have the key.\n" # unlocked no key, connected exit
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.assertEqual(self.room.exits[0].door.lock.is_locked, False)
        self.assertEqual(room_trans.exits[0].door.lock.is_locked, False)
        self.room.exits[0].door.lock.key = "key"    # key initialized and added
        self.room.save()
        self.player.inventory.append( Item("key","key",[], 1, False, False, True, [], {}, [], []))
        test_input = ['unlock', 'exit_1', 'exit', '']   # both unlocked w key
        expected_output = "\n RoomTester\nexit_1 door was already unlocked.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.assertEqual(self.room.exits[0].door.lock.is_locked, False)
        self.assertEqual(room_trans.exits[0].door.lock.is_locked, False)
        room_trans.exits[0].door.lock.is_locked = True     # one locked
        room_trans.save()
        test_input = ['unlock', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nexit_1 door was already unlocked.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.assertEqual(self.room.exits[0].door.lock.is_locked, False)
        self.assertEqual(room_trans.exits[0].door.lock.is_locked, True)
        self.room.exits[0].door.lock.is_locked = True  # both locked
        self.room.save()
        test_input = ['unlock', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nexit_1 door is now unlocked.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.assertEqual(self.room.exits[0].door.lock.is_locked, False)
        self.assertEqual(room_trans.exits[0].door.lock.is_locked, True)
        room_trans.exits[0].door.lock.key = "key"    # key initialized other side
        room_trans.save()
        test_input = ['unlock', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nexit_1 door was already unlocked.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.assertEqual(self.room.exits[0].door.lock.is_locked, False)
        self.assertEqual(room_trans.exits[0].door.lock.is_locked, True)
        self.room.exits[0].door.lock.is_locked = True  # both locked
        room_trans.exits[0].door.lock.is_locked = True
        room_trans.save()
        self.room.save()
        test_input = ['unlock', 'exit_1', 'exit', '']
        expected_output = "\n RoomTester\nexit_1 door is now unlocked.\n"
        self.assertEqual(self.get_output_string(test_input), expected_output)
        self.assertEqual(self.room.exits[0].door.lock.is_locked, False)
        # self.assertEqual(room_trans.exits[0].door.lock.is_locked, False)#TODO: figure it out
        # reset
        self.room.exits[0].door.lock.is_locked = False
        room_trans.exits[0].door.lock.is_locked = False
        self.room.exits[0].door.lock.key = ""
        room_trans.exits[0].door.lock.key = ""
        self.room.exits[0].links_to = ""
        room_trans.exits[0].links_to = ""
        self.room.save()
        room_trans.save()

if __name__ == "__main__":
    unittest.main()