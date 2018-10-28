from Objects.Exit import Exit
#from Objects.Item import Item
from Objects.Trigger import Trigger

import os
import json


class Room:
    room_name = None
    room_file = None
    description = None
    illuminated = False
    inventory = None
    exits = None
    triggers = None

    def __init__(self, room_name, room_file, description, illuminated, inventory, exits, triggers):
        self.room_name = room_name
        self.room_file = room_file
        self.description = description
        self.illuminated = illuminated
        self.inventory = inventory
        self.exits = exits
        self.triggers = triggers

    @classmethod
    def from_dict(cls, room_dict):
        room_name = room_dict['room_name']
        room_file = room_dict['room_file']
        description = room_dict['description']
        illuminated = room_dict['illuminated']
        inventory = cls.__fill_inventory(room_dict['inventory'])
        exits = cls.__fill_exits(room_dict['exits'])
        triggers = cls.__fill_triggers(room_dict['triggers'])
        return cls(room_name, room_file, description, illuminated, inventory, exits, triggers)

    @staticmethod
    def __fill_inventory(inventory_dict):
        # TODO Come back to this (WIP)

        out = []
#        for key, value in inventory_dict.items():
#            out.append(Item(key, value))
        return out

    @staticmethod
    def __fill_exits(exits=None):
        if not exits:
            exits = dict()

        out = []

        if type(exits) is dict:
            temp_array = []
            for key, value in exits.items():
                out.append(Exit.from_dict(key, value))
        elif type(exits) is list:
            for e in exits:
                if type(e) is Exit:
                    out.append(e)
                else:
                    out = []
                    # TODO Error handling for 'Exits supplied are not the right format.'
                    print()
                    break

        else:
            # TODO Error handling for 'Exits supplied are not the right format.'
            print()

        return out

    @staticmethod
    def __fill_triggers(triggers_dict=None):
        if not triggers_dict:
            triggers_dict = dict()

        out = []
        for key, value in triggers_dict.items():
            out.append(Trigger(key, value))
        return out

    def save(self):
        out = dict()
        out['room_name'] = self.room_name
        out['room_file'] = self.room_file
        out['description'] = self.description
        out['illuminated'] = self.illuminated

        out['exits'] = dict()
        for e in self.exits:
            key, value = e.to_json()
            out[key] = value

        out['inventory'] = dict()
        for i in self.inventory:
            key, value = i.to_json()
            out[key] = value

        out['triggers'] = dict()
        for t in self.triggers:
            key, value = t.to_json()
            out[key] = value

        room_json = json.dumps(out, indent=4)

        if not os.path.isdir("./Rooms/"):
            os.makedirs("./Rooms/")

        if "../" not in self.room_file and self.room_file.endswith(".room"):
            if os.path.isfile(self.room_file):
                yes = ["y", "yes"]
                no = ["n", "no"]
                overwrite = input(
                    "Room file already exists, would you like to overwrite {}: ".format(self.room_name))

                while overwrite not in yes and overwrite not in no:
                    overwrite = input("Invalid option supplied, overwrite (y/n): ")

                if overwrite in yes:
                    tmp_file = "{}.tmp".format(self.room_file)
                    with open(tmp_file, "w") as f:
                        f.write(room_json)
                    f.close()
                    os.remove(self.room_file)
                    os.rename(tmp_file, self.room_file)
                else:
                    # TODO Notify the user that the room data has not been saved.
                    print()
            else:
                with open(self.room_file, "w+") as f:
                    f.write(room_json)
                f.close()
        else:
            # TODO Error handling for "Invalid file name."
            print()

    def look(self):
        print(self.description)
