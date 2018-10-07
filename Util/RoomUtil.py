import json
import os


def change_room_name(room=None, room_name=None):
    # ##
    # Updates a rooms name.
    # The room name is displayed when entering a room.
    # The room name also determines the '.room' file name.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    if room:
        if "room_name" in room:
            if room_name:
                # Updating room name and the reference to the room file.
                room["room_name"] = room_name
                room["room_file"] = "./Rooms/{}.room".format(room_name.replace(" ", "_"))

                # TODO Recursively find/update all exit references in other rooms. [Dakotah]

            else:
                # TODO Error handling for 'No room name was supplied.'.
                print()
        else:
            # TODO Error handling for 'Invalid room format supplied'.
            print()
    else:
        # TODO Error handling for 'No room supplied'
        print()


def set_room_description(room=None, room_description=None):
    # ##
    # Changes a room description to a room.
    # This message will be displayed when a user supplies a 'look' command.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
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
    if room:
        if "description" in room:
            if room_description:
                room["description"] = room_description
            else:
                # TODO Error handling for 'No room description was supplied'
                print()
        else:
            # TODO Error handling for 'Invalid room format supplied'.
            print()
    else:
        # TODO Error handling for 'No room supplied'
        print()


def add_light_to_room(room=None):
    # ##
    # Adds light to a room.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room:
        if type(room) is dict:
            if "illuminated" in room:
                room["illuminated"] = True
            else:
                # TODO Error handling for 'Invalid object supplied to room argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for room argument.'
            print()
    else:
        # TODO Error handling for 'No object supplied for room argument.'
        print()


def remove_light_from_room(room=None):
    # ##
    # Removes light from a room.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    if room:
        if type(room) is dict:
            if "illuminated" in room:
                room["illuminated"] = False
            else:
                # TODO Error handling for 'Invalid object supplied for room argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for room argument.'
            print()
    else:
        # TODO Error handling for 'No object supplied for room argument.'
        print()


def create_room(room_name="",
                room_file="",
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

    room_dict = dict()
    if room_name:
        room_dict["room_name"] = room_name
        if not room_file:
            room_file = "./Rooms/{}.room".format(room_name.replace(" ", "_"))
        room_dict["room_file"] = room_file

        if not description:
            # TODO Error handling for room without description.
            print()

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

    else:
        # TODO Error handling for no name entered.
        print()

    return room_dict


def load_room(room_name=None, room_file=None):
    # ##
    # Load a json formatted room file.
    #
    # @author Dakotah Jones
    # @date 10/03/2018
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
                    # TODO Error handling for "File does not exist."
                    print()

            if room_file:
                if "../" not in room_file and not room_file.startswith("/"):
                    if os.path.isfile(room_file):
                        with open(room_file) as f:
                            out = json.load(f)
                        f.close()
                    else:
                        # TODO Error handling for "File does not exist."
                        print()
                else:
                    # TODO Error handling for "Illegal file path supplied."
                    print()
        else:
            # TODO Error handling for too many arguments supplied. (One or the other.)
            print()
    else:
        # TODO Error handling for no arguments supplied.
        print()

    return out


def save_room(room=None):
    # ##
    # Save a json formatted room file to the file system.
    #
    # @author Dakotah Jones
    # @date 10/03/2018
    # ##

    if room:
        if "room_file" in room:
            room_file = room["room_file"]
            room_json = json.dumps(room, indent=4)
            if "../" not in room_file and room_file.endswith(".room"):
                if os.path.isfile(room_file):
                    yes = ["y", "yes"]
                    no = ["n", "no"]
                    overwrite = input(
                        "Room file already exists, would you like to overwrite {}: ".format(room["room_name"]))

                    while overwrite not in yes and overwrite not in no:
                        overwrite = input("Invalid option supplied, overwrite (y/n): ")

                    if overwrite in yes:
                        tmp_file = "{}.tmp".format(room_file)
                        with open(tmp_file, "w") as f:
                            f.write(room_json)
                        f.close()
                        os.remove(room_file)
                        os.rename(tmp_file, room_file)
                    else:
                        # TODO Notify the user that the room data has not been saved.
                        print()
                else:
                    with open(room_file, "w+") as f:
                        f.write(room_json)
                    f.close()
            else:
                # TODO Error handling for "Invalid file name."
                print()
        else:
            # TODO Error handling for "Invalid object supplied as room argument."
            print()
    else:
        # TODO Error handling for "No object supplied as room argument."
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


# TODO This one is going to be harder than originally expected.
# TODO Map this out before starting.
def link_two_rooms(start_room=None, direction=None, destination_room=None, locked=False, door_open=True, open_description="", locked_description="", door_key=""):
    if start_room is None:
        print("Error :: No starting was provided.")
    elif direction is None:
        print("Error :: No direction was provided.")
    elif destination_room is None:
        print("Error :: No destination_room was provided.")
    else:
        start_room["go"][direction] = dict()
        room_exit = start_room["go"][direction]
        room_exit["room_name"] = destination_room["room_name"]
        room_exit["locked"] = locked
        room_exit["open"] = door_open
        room_exit["open_description"] = open_description
        room_exit["key"] = door_key
