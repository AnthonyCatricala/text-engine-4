import os
import json


class Room:
    player_name = ""

    room_name = ""
    init = ""
    enter = ""
    go = None
    look = None
    inventory = None
    sleep = None

    def __init__(self, room_name=None, player_name=None):
        self.room_name = room_name
        if player_name is None:
            self.player_name = "Default"
        else:
            self.player_name = player_name
        self.check_save()

    def check_save(self):
        sav_to_check = "Saves/Room/{}_{}.sav".format(self.player_name.format(" ", "_"), self.room_name.replace(" ", "_"))
        if os.path.isfile(sav_to_check):
            with open(sav_to_check, "r") as f:
                room_data = f.read().replace("\n", "")
            f.close()
            loaded_data = json.loads(room_data)
            self.load_room(loaded_data)
        else:
            room_file = "Rooms/" + self.room_name + ".room"
            if os.path.isfile(room_file):
                with open(room_file, "r") as f:
                    room_data = f.read().replace("\n", "")
                f.close()
                loaded_data = json.loads(room_data)
                self.load_room(loaded_data)
                self.save_room()

    # Save the instance of the room.
    def save_room(self):
        room_dict = dict()
        room_dict["room_name"] = self.room_name
        room_dict["init"] = self.init
        room_dict["enter"] = self.enter
        room_dict["look"] = self.look
        room_dict["inventory"] = self.inventory
        room_dict["sleep"] = self.sleep
        room_dict["go"] = self.go

        room_file = "Saves/Room/{}_{}.sav".format(self.player_name.replace(" ", "_"), self.room_name.replace(" ", "_"))
        room_json = json.dumps(room_dict)
        with open(room_file, "w") as f:
            f.write(room_json)
        f.close()

    # Load a new room.
    def load_room(self, room_data):
        self.room_name = room_data["room_name"]
        self.init = room_data["init"]
        self.enter = room_data["enter"]
        self.look = room_data["look"]
        self.inventory = room_data["inventory"]
        self.sleep = room_data["sleep"]
        self.go = room_data["go"]

        print("\n~{}~\n".format(self.room_name.replace("_", " ")))
        if self.init is not None:
            print(self.init)
            self.init = None
            self.save_room()
        else:
            print(self.enter)

    def get_exits(self):
        return self.go
