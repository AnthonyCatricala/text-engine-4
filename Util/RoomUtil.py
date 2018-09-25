def add_init(room_name=None, init_text=""):
    if room_name is None:

def remove_init():
    print()

def change_init():
    print()


def load_room():
    print()

def createRoom(room_name=None, init_text=None, look_text=None):
    if player_name is None:
        self.room_name = "New Room"
    else:
        self.room_name = room_name

    if init_text is None:
        self.init_text = "You walk into a newly-created empty room. You have a feeling you are the first person to ever set foot in this room."
    else:
        self.init_text = init_text

    if look_text is None:
        self.look_text = "You are in an empty room. The room is immaculate, obviously freshly created."
    else:
        self.look_text = look_text

    room_dict = dict()
    room_dict["room_name"] = self.room_name
    room_dict["init"] = self.init
    room_dict["enter"] = self.enter
    room_dict["look"] = self.look
    room_dict["inventory"] = dict()
    room_dict["sleep"] = dict()
    room_dict["go"] = dict()
    room_dict["triggers"] = dict()

    return room_dict


def addToRoom(room_name=None, item_name=None, item_dict=None):
    if room_name is None:
        print("Error :: No room name was provided.")
    elif item_name is None:
        print("Error :: No item name was provided.")
    elif item_dict is None
        print("Error :: No item dict was provided.")
    else
        room["inventory"][item_name] = item_dict
        room_file_name = "./Rooms/{}.room".format(room_name.replace(" ", "_"))
        room_json = json.dumps(room_dict)
        with open(room_file_name, "w") as f:
            f.write(room_json)
        f.close

def linkRoom(start_room=None, direction=None, destination_room=None, locked=False, door_open=True, open_description="", locked_description="", door_key=""):
    if start_room=None:
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
