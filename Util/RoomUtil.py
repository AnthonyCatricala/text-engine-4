from Util.ItemUtil import *
from Util.ErrorUtil import *
from Objects.Room import Room
from Objects.Door import Door
from Objects.Lock import Lock
from Objects.Exit import Exit
import json
import os

# TODO Create Item Python Object.
# TODO Create Checks For Object Validity.


def change_room_name(room=None, room_name=None):
    # ##
    # Updates a rooms name.
    # The room name is displayed when entering a room.
    # The room name also determines the '.room' file name.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    if room and type(room) is Room:
        if room_name and type(room_name) is str:
            room.room_name = room_name
            room.save()
        else:
            error_handler("change_room_name", "no name")
    else:
        error_handler("change_room_name", "no room")


def set_room_description(room=None, room_description=None):
    # ##
    # Changes a room description to a room.
    # This message will be displayed when a user supplies a 'look' command.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    #
    # @arg room WhatIF Room Object
    # @arg room_description String describing the room.

    # ##
    change_room_description(room, room_description)


def change_room_description(room=None, room_description=None):
    # ##
    # Changes a room description to a room.
    # This message will be displayed when a user supplies a 'look' command.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##

    if room and type(room) is Room:
        if room_description:
            room.description = room_description
        else:
            error_handler("change_room_description", "invalid format")
    else:
        error_handler("change_room_description", "no room")


def add_light_to_room(room=None):
    # ##
    # Adds light to a room.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room and type(room) is Room:
        room.illuminated = True
    else:
        error_handler("add_light_to_room", "no object")


def remove_light_from_room(room=None):
    # ##
    # Removes light from a room.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    if room and type(room) is Room:
        room.illuminated = False
    else:
        error_handler("remove_light_from_room", "no object")


def create_room(room_name="",
                description="",
                illuminated=True,
                inventory=None,
                exits=None,
                triggers=None):
    # ##
    # Creates a room to be further manipulated via the other room API functions.
    # Base room creation function.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    out = None
    if room_name:
        room_dict = dict()
        room_dict["room_name"] = room_name
        room_dict["room_file"] = "./Rooms/{}.room".format(room_name.replace(" ", "_"))

        if not description:
            error_handler("create_room", "no description")

        room_dict["description"] = description
        room_dict["illuminated"] = illuminated

        if not inventory:
            room_dict["inventory"] = dict()
        else:
            room_dict["inventory"] = inventory

        if not exits:
            room_dict["exits"] = dict()
        else:
            room_dict["exits"] = exits

        if not triggers:
            room_dict["triggers"] = dict()
        else:
            room_dict["triggers"] = triggers

        out = Room.from_dict(room_dict)
        out.save()

    else:
        error_handler("create_room", "no name")

    return out


def load_room(room_name=None, room_file=None):
    # ##
    # Load a json formatted room file.
    #
    # @author Dakotah Jones
    # @date 10/03/2018
    #
    # @arg room_name The room name spelled correctly with spaces.
    # @arg room_file The URL of the room file on disk.
    # @returns WhatIF Room Object.
    # ##

    out = None
    if room_name or room_file:
        if not (room_name and room_file):
            if room_name:
                file_path = "./Rooms/{}.room".format(room_name.replace(" ", "_"))
                if os.path.isfile(file_path):
                    with open(file_path) as f:
                        out = json.load(f)
                    f.close()
                else:
                    error_handler("load_room", "file does not exist")

            if room_file:
                if "../" not in room_file and not room_file.startswith("/"):
                    if os.path.isfile(room_file):
                        with open(room_file) as f:
                            out = json.load(f)
                        f.close()
                    else:
                        error_handler("load_room", "file does not exist")
                else:
                    error_handler("load_room", "illegal file path")
            out = Room.from_dict(out)
        else:
            error_handler("load_room", "too many arguments")
    else:
        error_handler("load_room", "no argumments")

    return out


def save_room(room=None):
    # ##
    # Save a json formatted room file to the file system.
    #
    # @author Dakotah Jones
    # @date 10/03/2018
    #
    # @arg room A WhatIF Room Object.
    # ##

    if room and type(room) is Room:
        room.save()
    else:
        # TODO Error handling for No/Invalid room object supplied.
        print()


def add_object_to_room(room=None, obj=None):
    if room:
        if type(room) is dict:
            if "inventory" in room:
                inventory = room["inventory"]
                if type(inventory) is dict:
                    if type(obj) is dict:
                        if len(obj) == 1:
                            for key, value in obj.items():
                                inventory[key] = value
                        else:
                            # TODO Error handling for 'Too many object supplied within obj argument.'
                            print()
                    else:
                        # TODO Error handling for 'Invalid type supplied as obj argument.'
                        print()
                else:
                    # TODO Error handling for 'Illegal inventory format within room argument.'
                    print()
            else:
                # TODO Error handling for 'Invalid object supplied as room argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied as room argument.'
            print()
    else:
        # TODO Error handling for 'No object supplied as room argument.'
        print()


def remove_object_from_room(room=None, obj_name=None):
    if room:
        if type(room) is dict:
            if "inventory" in room:
                inventory = room["inventory"]
                if type(inventory) is dict:
                    if type(obj_name) is str:
                        if obj_name in inventory:
                            # TODO Take quantity into account, drop quantity till zero then delete. [Dakotah]
                            del(inventory[obj_name])
                        else:
                            # TODO Error handling for 'Object is not present within the rooms inventory.'
                            print()
                    else:
                        # TODO Error handling for 'Invalid type supplied as obj name argument.'
                        print()
                else:
                    # TODO Error handling for 'Illegal inventory format within room argument.'
                    print()
            else:
                # TODO Error handling for 'Invalid object supplied as room argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied as room argument.'
            print()
    else:
        # TODO Error handling for 'No object supplied as room argument.'
        print()


def create_door(is_open=False,
                lock=None,
                triggers=None):
    # ##
    # Create a door that can then be placed on containers or exits.
    #
    # @author Dakotah Jones
    # @date 10/03/2018
    # ##
    door_dict = dict()
    door_dict["open"] = is_open
    if lock:
        door_dict["lock"] = lock
    else:
        door_dict["lock"] = dict()

    if triggers:
        door_dict["triggers"] = triggers
    else:
        door_dict["triggers"] = dict()

    out = Door.from_dict(door_dict)

    return out


def create_lock_and_key(key_name="",
                        key_description="",
                        is_locked=True,
                        triggers=None):
    lock = None
    key = None

    if key_name and type(key_name) is str:
        if key_description and type(key_description) is str:
            lock_dict = dict()
            lock_dict["key"] = key_name
            lock_dict["locked"] = is_locked
            lock_dict["triggers"] = triggers

            lock = Lock.from_dict(lock_dict)

            key = create_object(key_name, key_description)

        else:
            # TODO Error handling for 'A key description is required to create a lock.'
            print()
    else:
        # TODO Error handling for 'A key name is required to create a lock.'
        print()

    return lock, key


def apply_lock_to_door(door=None, lock=None):
    if lock:
        if type(lock) is dict:
            if door:
                if type(door) is dict:
                    if "lock" in door:
                        door["lock"] = lock
                    else:
                        # TODO Error handling for 'Illegal door format supplied withing door argument.'
                        print()
                else:
                    # TODO Error handling for 'Invalid type supplied for door argument.'
                    print()
            else:
                # TODO Error handling for 'No object supplied for door argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for lock argument.'
            print()
    else:
        # TODO Error handling for 'No object supplied for lock argument.'
        print()


def remove_lock_from_door(door=None):
    if door:
        if type(door) is dict:
            if "lock" in door:
                door["lock"] = dict()
            else:
                # TODO Error handling for 'Illegal door format supplied withing door argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for door argument.'
            print()
    else:
        # TODO Error handling for 'No object supplied for door argument.'
        print()


def create_room_exit(compass_direction="",
                     links_to="",
                     description="",
                     is_blocked=False,
                     door=None,
                     triggers=None):

    compass_direction = compass_direction.lower()
    compass_directions = ["north",
                          "northeast",
                          "east",
                          "southeast",
                          "south",
                          "southwest",
                          "west",
                          "northwest"]

    out = None
    if compass_direction:
        if type(compass_direction) is str:
            if compass_direction in compass_directions:

                if links_to:
                    if type(links_to) is str:
                        if os.path.isfile(links_to):

                            if description:
                                if type(description) is str:
                                    out = dict()
                                    out[compass_direction] = dict()

                                    room_exit = out[compass_direction]
                                    room_exit["links-to"] = links_to
                                    room_exit["description"] = description
                                    room_exit["blocked"] = is_blocked

                                    if door:
                                        room_exit["door"] = door
                                    else:
                                        room_exit["door"] = dict()

                                    if triggers:
                                        room_exit["triggers"] = triggers
                                    else:
                                        room_exit["triggers"] = dict()

                                    out = Exit.from_dict(compass_direction, room_exit)

                                else:
                                    # TODO Error handling for 'Invalid type supplied for description argument.'
                                    print()
                            else:
                                # TODO Error handling for 'No string supplied for description argument.'
                                print()
                        else:
                            # TODO Error handling for 'Room file you are linking to does not exist.'
                            print()
                    else:
                        # TODO Error handling for 'Invalid type supplied for links to argument..'
                        print()
                else:
                    # TODO Error handling for 'No string supplied for links to argument.'
                    print()
            else:
                # TODO Error handling for 'Invalid compass direction supplied to compass direction arguement.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for compass direction argument.'
            print()
    else:
        # TODO Error handling for 'No string supplied for compass direction argument.'
        print()

    return out


def apply_door_to_exit(room_exit=None, door=None):
    if room_exit:
        if type(room_exit) is dict:
            if len(room_exit) == 1:
                for key, value in room_exit.items():
                    if "door" in value:
                        if door:
                            if type(door) is dict:
                                value["door"] = door
                            else:
                                # TODO Error handling for 'Invalid type supplied for compass direction argument.'
                                print()
                        else:
                            # TODO Error handling for 'No object supplied for door argument.'
                            print()
                    else:
                        # TODO Error handling for 'Invalid room exit format supplied for room exit argument.'
                        print()
            else:
                # TODO Error handling for 'Too many object supplied within the room exit argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for room exit argument.'
            print()
    else:
        # TODO Error handling for 'No object supplied for the room exit argument.'
        print()


def remove_door_from_exit(room_exit=None):
    if room_exit:
        if type(room_exit) is dict:
            if len(room_exit) == 1:
                for key, value in room_exit.items():
                    if "door" in value:
                        value["door"] = dict()
                    else:
                        # TODO Error handling for 'Invalid room exit format supplied for room exit argument.'
                        print()
            else:
                # TODO Error handling for 'Too many object supplied within the room exit argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for room exit argument.'
            print()
    else:
        # TODO Error handling for 'No object supplied for the room exit argument.'
        print()


def apply_exit_to_room(room=None, room_exit=None):
    if room:
        if type(room) is dict:
            if "exits" in room:

                if room_exit:
                    if type(room_exit) is dict:
                        if len(room_exit) == 1:
                            for key, value in room_exit.items():
                                room["exits"][key] = value
                        else:
                            # TODO Error handling for 'Too many object supplied within the room exit argument.'
                            print()
                    else:
                        # TODO Error handling for 'Invalid type supplied for room exit argument.'
                        print()
                else:
                    # TODO Error handling for 'No object supplied for the room exit argument.'
                    print()
            else:
                # TODO Error handling for 'Invalid room format supplied for room argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for room argument.'
            print()
    else:
        # TODO Error handling for 'No object supplied for the room argument.'
        print()


def remove_exit_from_room(room=None, compass_direction=None):
    compass_direction = compass_direction.lower()
    compass_directions = ["north",
                          "northeast",
                          "east",
                          "southeast",
                          "south",
                          "southwest",
                          "west",
                          "northwest"]

    if room:
        if type(room) is dict:
            if "exits" in room:

                if compass_direction:
                    if type(compass_direction) is str:
                        room_exits = room["exits"]
                        if compass_direction in compass_directions:
                            if compass_direction in room_exits:
                                del(room_exits[compass_direction])
                            else:
                                # TODO Error handling for 'No exit in compass direction specified.'
                                print()
                        else:
                            # TODO Error handling for 'Invalid string supplied to compass direction argument.'
                            print()
                    else:
                        # TODO Error handling for 'Invalid type supplied for compass direction argument.'
                        print()
                else:
                    # TODO Error handling for 'No object supplied for the compass direction argument.'
                    print()
            else:
                # TODO Error handling for 'Invalid room format supplied for room argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for room argument.'
            print()
    else:
        # TODO Error handling for 'No object supplied for the room argument.'
        print()
