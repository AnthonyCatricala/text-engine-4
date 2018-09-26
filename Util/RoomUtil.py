def update_initial_room_message(room=None, init_text=""):
    if room is not None:
        room["init"] = init_text


def remove_initial_room_message(room=None):
    if room is not None:
        room["init"] = ""


def update_entering_room_message(room=None, enter_text=""):
    if room is not None:
        room["enter"] = enter_text


def remove_entering_room_message(room=None):
    if room is not None:
        room["enter"] = ""


def add_a_group_of_room_descriptions(room=None, room_description_group=None):
    if room is not None and room_description_group is not None:
        for key,value in room_description_group.items():
            room["look"][key] = value


def add_a_single_room_description(room=None, room_description=None, description_initially_visible=True):
    if room is not None and room_description is not None:
        room["look"][room_description] = description_initially_visible


def remove_a_single_room_description(room=None, room_description=None):
    if room is not None and room_description is not None:
        del room["look"][room_description]


def remove_all_room_descriptions(room=None):
    if room is not None:
        room["look"] = dict()


def create_object(
        object_name=None,
        object_description=None,
        take_description=None,
        drop_description=None,
        read_description=None,
        eat_description=None,
        drink_description=None,
        is_illuminated=False,
        is_container=False):

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
    if room is not None:
        room["illuminated"] = True


def remove_light_from_room(room=None):
    if room is not None:
        room["illuminated"] = False


def illuminate_object(room=None, item=None):
    if room is not None:
        room["illuminated"] = True
    if item is not None:
        item["illuminated"] = False


def create_room(
        room_name="New Room",
        init_text="You walk into a newly-created empty room. "
                  "You have a feeling you are the first person to ever set foot in this room.",
        enter_text="You walk into the room.",
        illuminated=True,):

    room_dict = dict()
    room_dict["room_name"] = room_name
    room_dict["init"] = init_text
    room_dict["enter"] = enter_text
    room_dict["illuminated"] = illuminated
    room_dict["look"] = dict()
    room_dict["inventory"] = dict()
    room_dict["sleep"] = dict()
    room_dict["go"] = dict()
    room_dict["triggers"] = dict()

    return room_dict


def add_object_to_room(room_name=None, item_name=None, item_dict=None):
    if room_name is None:
        print("Error :: No room name was provided.")
    elif item_name is None:
        print("Error :: No item name was provided.")
    elif item_dict is None:
        print("Error :: No item dict was provided.")
    else:
        room["inventory"][item_name] = item_dict
        room_file_name = "./Rooms/{}.room".format(room_name.replace(" ", "_"))
        room_json = json.dumps(room_dict)
        with open(room_file_name, "w") as f:
            f.write(room_json)
        f.close


def link_two_rooms(start_room=None, direction=None, destination_room=None, locked=False, door_open=True, open_description="", locked_description="", door_key=""):
    if start_room is None:
        print("Error :: No starting was provided.")
    elif direction is None:
        print("Error :: No direction was provided.")
    elif destination_room is None:
        print("Error :: No destination_room was provided.")
    else
        start_room["go"][direction] = dict()
        room_exit = start_room["go"][direction]
        room_exit["room_name"] = destination_room["room_name"]
        room_exit["locked"] = locked
        room_exit["open"] = door_open
        room_exit["open_description"] = open_description
        room_exit["key"] = door_key
