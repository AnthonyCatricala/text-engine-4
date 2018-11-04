from Util.ItemUtil import *
from Util.ErrorUtil import *
from Objects.Room import Room
from Objects.Door import Door
from Objects.Lock import Lock
from Objects.Exit import Exit
import json
import os

# TODO Create Item Python Object.


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
            if out:
                out = Room.from_dict(out)
        else:
            error_handler("load_room", "too many arguments")
    else:
        error_handler("load_room", "no arguments")

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
        error_handler("save_room", "no object")


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
                            error_handler("add_object_to_room", "too many arguments")
                    else:
                        error_handler("add_object_to_room", "invalid object type")
                else:
                    error_handler("add_object_to_room", "invalid format")
            else:
                error_handler("add_object_to_room", "invalid object")
        else:
            error_handler("add_object_to_room", "invalid room type")
    else:
        error_handler("add_object_to_room", "no object")


# TODO Combe back to this when Items have been created.
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
                            error_handler("remove_object_from_room", "no object")
                    else:
                        error_handler("remove_object_from_room", "invalid type")
                else:
                    error_handler("remove_object_from_room", "invalid format")
            else:
                error_handler("remove_object_from_room", "invalid object")
        else:
            error_handler("remove_object_from_room", "invalid type")
    else:
        error_handler("remove_object_from_room", "no room")


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


# TODO Come back to this when Items have been created.
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
            error_handler("create_lock_and_key", "no key description")
    else:
        error_handler("create_lock_and_key", "no key name")

    return lock, key


def apply_lock_to_door(door=None, lock=None):
    if lock:
        if type(lock) is Lock:
            if door:
                if type(door) is Door:
                    door.lock = lock
                else:
                    error_handler("apply_lock_to_door", "invalid door type")
            else:
                error_handler("apply_lock_to_door", "no door object")
        else:
            error_handler("apply_lock_to_door", "invalid lock type")
    else:
        error_handler("apply_lock_to_door", "no lock object")


def remove_lock_from_door(door=None):
    if door:
        if type(door) is Door:
            if door.lock:
                door.lock = None
            else:
                # TODO Error handling for 'There is no lock on that door.'
                print()
        else:
            error_handler("remove_lock_from_door", "invalid door type")
    else:
        error_handler("remove_lock_from_door", "no object")


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
                                    error_handler("create_room_exit", "invalid description type")
                            else:
                                error_handler("create_room_exit", "no description string")
                        else:
                            error_handler("create_room_exit", "room does not exist")
                    else:
                        error_handler("create_room_exit", "invalid link type")
                else:
                    error_handler("create_room_exit", "no link string")
            else:
                error_handler("create_room_exit", "invalid compass direction")
        else:
            error_handler("create_room_exit", "invalid compass direction type")
    else:
        error_handler("create_room_exit", "no compass direction string")

    return out


def apply_door_to_exit(room_exit=None, door=None):
    if room_exit:
        if type(room_exit) is Exit:
            if type(door) is Door:
                room_exit.door = door
            else:
                # TODO Error handling for 'Invalid type supplied for door argument.'
                print()
        else:
            error_handler("apply_door_to_exit", "invalid door type")
    else:
        error_handler("apply_door_to_exit", "no exit object")


def remove_door_from_exit(room_exit=None):
    if room_exit:
        if type(room_exit) is Exit:
            if room_exit.door:
                room_exit.door = None
            else:
                # TODO Error handling for 'No door exists on that exit.'
                print()
        else:
            error_handler("remove_door_from_exit", "invalid type")
    else:
        error_handler("remove_door_from_exit", "no object")


def apply_exit_to_room(room=None, room_exit=None):
    if room:
        if type(room) is Room:
            if room_exit:
                if type(room_exit) is Exit:
                    room.exits.append(room_exit)
                else:
                    error_handler("apply_exit_to_room", "invalid exit type")
            else:
                error_handler("apply_exit_to_room", "no exit object")
        else:
            error_handler("apply_exit_to_room", "invalid room type")
    else:
        error_handler("apply_exit_to_room", "no room object")


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
        if type(room) is Room:
            if compass_direction:
                if type(compass_direction) is str:
                    room_exits = room.exits
                    if compass_direction in compass_directions:
                        exit_found = False
                        for e in room_exits:
                            if e.compass_direction == compass_direction:
                                room_exits.remove(e)
                        if not exit_found:
                            error_handler("remove_exit_from_room", "no exit in speci direction")
                    else:
                        error_handler("remove_exit_from_room", "invalid string")
                else:
                    error_handler("remove_exit_from_room", "no compass direction type")
            else:
                error_handler("remove_exit_from_room", "no compass direction object")
        else:
            error_handler("remove_exit_from_room", "invalid room type")
    else:
        error_handler("remove_exit_from_room", "no room object")
