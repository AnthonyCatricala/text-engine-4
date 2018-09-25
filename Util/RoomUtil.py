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
