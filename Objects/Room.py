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

    def __init__(self, room_dict):
        self.room_name = room_dict['room_name']
        self.room_file = room_dict['room_file']
        self.description = room_dict['description']
        self.illuminated = room_dict['illuminated']
        self.inventory = self.__fill_inventory(room_dict['inventory'])
        self.exits = self.__fill_exits(room_dict['exits'])
        self.triggers = self.__fill_triggers(room_dict['triggers'])

    @staticmethod
    def __fill_inventory(inventory_dict):
        # TODO Come back to this (WIP)

        out = []
#        for key, value in inventory_dict.items():
#            out.append(Item(key, value))
        return out

    @staticmethod
    def __fill_exits(exits_dict):
        out = []
        for key, value in exits_dict.items():
            out.append(Exit(key, value))
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
