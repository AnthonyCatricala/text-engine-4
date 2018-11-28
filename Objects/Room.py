from Objects.Item import Item
from Objects.Exit import Exit
from Objects.Trigger import Trigger
from Objects.UserScript import UserScript

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
        inventory = Item.fill_inventory(room_dict['inventory'])
        exits = Exit.fill_exits(room_dict['exits'])
        triggers = Trigger.fill_triggers(room_dict['triggers'])
        user_scripts = UserScript.fill_user_scripts(room_dict["user-scripts"])

        return cls(room_name, room_file, description, illuminated, inventory, exits, triggers, user_scripts)

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

        out['inventory'] = list()
        if self.inventory:
            for i in self.inventory:
                out['inventory'].append(i.to_json())

        out['triggers'] = list()
        if self.triggers:
            for t in self.triggers:
                out['triggers'].append(t.to_json())

        out["user-scripts"] = list()
        if self.user_scripts:
            for s in self.user_scripts:
                out['user-scripts'].append(s.to_json())

        room_json = json.dumps(out, indent=4)

        if not os.path.isdir("./Rooms/"):
            os.makedirs("./Rooms/")

        if "../" not in self.room_file and self.room_file.endswith(".room"):
            if os.path.isfile(self.room_file):
                # print("Overwriting {}".format(self.room_name))
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
            self.inventory = Item.fill_inventory(room_dict['inventory'])
            self.exits = Exit.fill_exits(room_dict['exits'])
            self.triggers = Trigger.fill_triggers(room_dict['triggers'])
            self.user_scripts = UserScript.fill_user_scripts(room_dict["user-scripts"])

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

    # Gets all applicable triggers and removes them from their respective objects.
    def get_triggers(self, primary_command):
        trigger_list = []

        # Get all applicable triggers from the room.
        room_triggers = []
        for t in self.triggers:
            if t.trigger_command == primary_command:
                room_triggers.append(t)

        # Remove all applicable triggers from the room.
        for t in room_triggers:
            self.triggers.remove(t)
        trigger_list += room_triggers

        # All exits
        for e in self.exits:

            # Get all applicable triggers from the exit.
            exit_triggers = []
            for t in e.triggers:
                if t.trigger_command == primary_command:
                    exit_triggers.append(t)

            # Remove all applicable triggers form the exit.
            for t in exit_triggers:
                e.triggers.remove(t)
            trigger_list += exit_triggers

            # The door attached to the exit.
            if e.door:

                # Get all applicable triggers from the door.
                door_triggers = []
                for t in e.door.triggers:
                    if t.trigger_command == primary_command:
                        door_triggers.append(t)

                # Remove all applicable triggers from the door.
                for t in e.door.triggers:
                    e.door.triggers.remove(t)
                trigger_list += door_triggers

                # The lock on the door.
                if e.door.lock:

                    # Get all applicable triggers from the lock.
                    lock_triggers = []
                    for t in e.door.lock.triggers:
                        if t.trigger_command == primary_command:
                            lock_triggers.append(t)

                    # Remove all applicable triggers from the lock.
                    for t in lock_triggers:
                        e.door.lock.triggers.remove(t)
                    trigger_list += lock_triggers

        return trigger_list

    def get_user_scripts(self, primary_command):
        user_scripts = []

        # Get all applicable triggers from the room.
        for us in self.user_scripts:
            if us.trigger_command == primary_command:
                user_scripts.append(us)

        # All exits
        for e in self.exits:

            # Get all applicable triggers from the exit.
            for us in e.user_scripts:
                if us.trigger_command == primary_command:
                    user_scripts.append(us)

            # The door attached to the exit.
            if e.door:

                # Get all applicable triggers from the door.
                for us in e.door.user_scripts:
                    if us.trigger_command == primary_command:
                        user_scripts.append(us)

                # The lock on the door.
                if e.door.lock:

                    # Get all applicable triggers from the lock.
                    for us in e.door.lock.user_scripts:
                        if t.trigger_command == primary_command:
                            user_scripts.append(us)

        return user_scripts
