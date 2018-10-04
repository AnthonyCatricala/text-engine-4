import json
import os


def update_room_name(room=None, room_name=None):
    # ##
    # Updates a rooms name.
    # The room name is displayed when entering a room.
    # The room name also determines the '.room' file name.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room is not None and room_name is not None:
        if len(room_name) > 0:
            room["room_name"] = room_name


def update_initial_room_message(room=None, init_text=""):
    # ##
    # Updates a rooms initial message.
    # This message will be displayed when the user
    # loads the room for the first time.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room is not None:
        room["init"] = init_text


def remove_initial_room_message(room=None):
    # ##
    # Removes a rooms initial message.
    # This message will be displayed when the user
    # loads the room for the first time.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room is not None:
        room["init"] = ""


def update_entering_room_message(room=None, enter_text=""):
    # ##
    # Updates a rooms enter message.
    # This message will be displayed when the user
    # enters the room from another room.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room is not None:
        room["enter"] = enter_text


def remove_entering_room_message(room=None):
    # ##
    # Removes a rooms enter message.
    # This message will be displayed when the user
    # enters the room from another room.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room is not None:
        room["enter"] = ""


def add_a_group_of_room_descriptions(room=None, room_description_group=None):
    # ##
    # Adds a group of room descriptions to a room.
    # These messages will be displayed when a user supplies a 'look' command.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room is not None and room_description_group is not None:
        for key,value in room_description_group.items():
            room["look"][key] = value


def add_a_single_room_description(room=None, room_description=None, description_initially_visible=True):
    # ##
    # Adds a single room description to a room.
    # This message will be displayed when a user supplies a 'look' command.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room is not None and room_description is not None:
        room["look"][room_description] = description_initially_visible


def remove_a_single_room_description(room=None, room_description=None):
    # ##
    # Removes a single room description to a room.
    # This message will be displayed when a user supplies a 'look' command.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room is not None and room_description is not None:
        del room["look"][room_description]


def remove_all_room_descriptions(room=None):
    # ##
    # Removes all room descriptions from a room.
    # No messages will be displayed when a user supplies a 'look' command.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if room is not None:
        room["look"] = dict()


def create_object(object_name=None,
                  object_description=None,
                  take_description=None,
                  drop_description=None,
                  read_description=None,
                  eat_description=None,
                  drink_description=None,
                  is_illuminated=False,
                  is_container=False):
    # ##
    # Creates an object that the player can interact with.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    if object_name is not None:
        obj_wrapper = dict()
        obj_wrapper[object_name] = dict()
        obj = obj_wrapper[object_name]

        if object_description is not None:
            obj["examine"] = object_description

        if read_description is not None:
            obj["read"] = read_description

        if take_description is not None:
            obj["take"] = take_description

        if eat_description is not None:
            obj["eat"] = eat_description

        if drink_description is not None:
            obj["drink"] = drink_description

        if drop_description is not None:
            obj["drop"] = drop_description

        obj["illuminated"] = is_illuminated
        obj["container"] = is_container
        obj["triggers"] = dict()
        obj["inventory"] = dict()

        return obj_wrapper


def add_light_to_room(room=None):
    # ##
    # Adds light to a room preventing darkness.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    illuminate_object(room=room)


def remove_light_from_room(room=None):
    # ##
    # Removes light from a room causing darkness.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##

    if room:
        if "illuminated" in room:
            room["illuminated"] = False
        else:
            # TODO Error handling for "Illegal room object supplied."
            print()
    else:
        # TODO Error handling for "No room object supplied."
        print()


def illuminate_object(item=None, room=None):
    # ##
    # Adds light to a room or object preventing darkness.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    if item or room:
        if item:
            if "illuminated" in item:
                if not item["illuminated"]:
                    item["illuminated"] = True
                else:
                    # TODO Error handling for "Item is already illuminated."
                    print()
            else:
                # TODO Error handling for "Item supplied cannot be illuminated."
                print()
        if room:
            if "illuminated" in room:
                if not room["illuminated"]:
                    room["illuminated"] = True
                else:
                    # TODO Error handling for "Room is already illuminated."
                    print()
            else:
                # TODO Error handling for "Room supplied cannot be illuminated"
                print()
    else:
        # TODO Error handling for "No room or object supplied."
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


def add_object_to_room(room=None, item=None):
    if room is not None and item is not None:
        for key, value in item.items():
            room["inventory"][key] = value


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
