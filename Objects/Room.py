from Objects.Exit import Exit
#from Objects.Item import Item
from Objects.Trigger import *
from Objects.UserScript import *
from Objects.Command import *
from Util.ErrorUtil import *

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
    user_scripts = None

    def __init__(self, room_name, room_file, description, illuminated, inventory, exits, triggers, user_scripts):
        self.room_name = room_name
        self.room_file = room_file
        self.description = description
        self.illuminated = illuminated
        self.inventory = inventory
        self.exits = exits
        self.triggers = triggers
        for trigger in self.triggers:
            trigger.connected_to = self
        self.user_scripts = user_scripts

    @classmethod
    def from_dict(cls, room_dict):
        room_name = room_dict['room_name']
        room_file = room_dict['room_file']
        description = room_dict['description']
        illuminated = room_dict['illuminated']
        inventory = cls.__fill_inventory(room_dict['inventory'])
        exits = cls.__fill_exits(room_dict['exits'])
        triggers = cls.__fill_triggers(room_dict['triggers'])
        user_scripts = cls.__fill_user_scripts(room_dict["user-scripts"])

        return cls(room_name, room_file, description, illuminated, inventory, exits, triggers, user_scripts)

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
        for trigger_command, trigger_wrapper in triggers_dict.items():
            for trigger_type, args_wrapper in trigger_wrapper.items():
                if trigger_type == "print":
                    out.append(PrintTrigger(trigger_command, args_wrapper['description']))
        return out

    @staticmethod
    def __fill_user_scripts(user_script_dict=None):
        if not user_script_dict:
            user_script_dict = dict()

        out = []

        for key, value in user_script_dict.items():
            wrapper = dict()
            wrapper[key] = value

            out.append(UserScript.from_dict(wrapper))

        return out

    def save(self):
        out = dict()
        out['room_name'] = self.room_name
        out['room_file'] = self.room_file
        out['description'] = self.description
        out['illuminated'] = self.illuminated

        out['exits'] = dict()
        if self.exits:
            for e in self.exits:
                key, value = e.to_json()
                out['exits'][key] = value

        out['inventory'] = dict()
        if self.inventory:
            for i in self.inventory:
                key, value = i.to_json()
                out['inventory'][key] = value

        out['triggers'] = dict()
        if self.triggers:
            for t in self.triggers:
                key, value = t.to_json()
                out['triggers'][key] = value

        out['user-scripts'] = dict()
        if self.user_scripts:
            for s in self.user_scripts:
                key, value = s.to_json()
                out['user-scripts'][key] = value

        room_json = json.dumps(out, indent=4)

        if not os.path.isdir("./Rooms/"):
            os.makedirs("./Rooms/")

        if "../" not in self.room_file and self.room_file.endswith(".room"):
            if os.path.isfile(self.room_file):
                print("Overwriting {}".format(self.room_name))
                os.remove(self.room_file)

            tmp_file = "{}.tmp".format(self.room_file)
            with open(tmp_file, "w+") as f:
                f.write(room_json)
            f.close()

            os.rename(tmp_file, self.room_file)

        else:
            # TODO Error handling for "Invalid file name."
            print()

    def load(self, room_file):
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

        room_dict = None

        if room_file:
            if "../" not in room_file and not room_file.startswith("/"):
                if os.path.isfile(room_file):
                    with open(room_file) as f:
                        room_dict = json.load(f)
                    f.close()
                else:
                    error_handler("load_room", "file does not exist")
            else:
                error_handler("load_room", "illegal file path")

        if room_dict:
            self.room_name = room_dict['room_name']
            self.room_file = room_dict['room_file']
            self.description = room_dict['description']
            self.illuminated = room_dict['illuminated']
            self.inventory = self.__fill_inventory(room_dict['inventory'])
            self.exits = self.__fill_exits(room_dict['exits'])
            self.triggers = self.__fill_triggers(room_dict['triggers'])
            self.user_scripts = self.__fill_user_scripts(room_dict["user-scripts"])

    def get_exit(self, compass_direction: str):
        compass_directions = [
            "north",
            "south",
            "east",
            "west"
        ]

        compass_direction = compass_direction.lower()

        out = None
        if compass_direction in compass_directions:
            for e in self.exits:
                if e.compass_direction == compass_direction:
                    out = e
                    break
        else:
            # TODO Error handling for "Invalid compass direction supplied."
            print()

        if not out:
            # TODO Error handling for "No exit in that direction."
            print()

        return out

    def look(self):
        print(self.description)

    # TODO Implement this for gathering all applicable triggers dependent on a command.
    # TODO Work In Progress; Do Not Use!
    def get_triggers(self, primary_command):
        trigger_list = []

        # All triggers in the room.
        for t in self.triggers:
            if t.trigger_command == primary_command:
                trigger_list.append(t)

        # All triggers from all exits
        for e in self.exits:

            # All triggers from the exit
            for t in e.triggers:
                if t.trigger_command == primary_command:
                    trigger_list.append(t)

            # All triggers from the door
            if e.door:
                for t in e.door.triggers:
                    if t.trigger_command == primary_command:
                        trigger_list.append(t)

                # All triggers from the lock.
                if e.door.lock:
                    for t in e.door.lock.triggers:
                        if t.trigger_command == primary_command:
                            trigger_list.append(t)

        return trigger_list
