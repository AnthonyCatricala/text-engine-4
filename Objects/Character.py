from Objects.Trigger import Trigger
from Objects.Exit import Exit
from Objects.Item import Item
from Objects.UserScript import UserScript

import os
import json


class Character:
    name = None
    inventory = None
    description = None

    def __init__(self, name, inventory, description):
        self.name = name
        self.inventory = inventory
        self.description = description


class Player(Character):
    character_file = None
    current_room_file = None
    alive = None

    def __init__(self, name, inventory, description, character_file="", current_room_file="", alive=True):
        super().__init__(name, inventory, description)

        if character_file:
            self.character_file = character_file
        else:
            self.character_file = "./Players/{}.player".format(self.name)

        self.current_room_file = current_room_file

        self.alive = alive

    def save(self, room_file: str=""):
        if isinstance(room_file, str) and room_file != "":
            self.current_room_file = room_file

            out = dict()
            out["name"] = self.name

            out['inventory'] = list()
            if self.inventory:
                for i in self.inventory:
                    out['inventory'].append(i.to_json())

            out['description'] = self.description
            out['character_file'] = self.character_file
            out['current_room_file'] = self.current_room_file
            out['alive'] = self.alive

            player_json = json.dumps(out, indent=4)

            if not os.path.isdir("./Players/"):
                os.makedirs("./Players/")

            if "../" not in self.character_file and self.character_file.endswith(".player"):
                if os.path.isfile(self.character_file):
                    # print("Overwriting {}".format(self.room_name))
                    os.remove(self.character_file)

                tmp_file = "{}.tmp".format(self.name)
                with open(tmp_file, "w+") as f:
                    f.write(player_json)
                f.close()

                os.rename(tmp_file, self.character_file)

    @classmethod
    def load(cls, character_file: str=None):
        if isinstance(character_file, str):

            character_dict = None
            if character_file:
                if "../" not in character_file and not character_file.startswith("/"):
                    if os.path.isfile(character_file):
                        with open(character_file) as f:
                            character_dict = json.load(f)
                        f.close()

            if character_dict:
                name = character_dict['name']
                inventory = Item.fill_inventory(character_dict['inventory'])
                description = character_dict['description']
                current_room_file = character_dict['current_room_file']
                alive = character_dict['alive']
                return cls(name, inventory, description, character_file, current_room_file, alive)


class NPC(Character):

    talk_output = None
    dialogue_dict = None

    def dialogue(self, dialogue_dict, talk_output):

        self.dialogue_dict = dialogue_dict
        self.talk_output = talk_output

    def examine(self):
        print(self.description)

    def talk_to(self):
        print(self.talk_output)

    def ask_about(self, topic=""):
        if self.dialogue_dict[topic]:
            print(self.dialogue_dict[topic])


# Everything after this point should go in command executor

    def examine_function(self, parsed_string):

        examine_target = parsed_string[1]

        if examine_target not in Room.inventory and examine_target not in Room.Character.name:
            print("That doesn't seem to be here. What are you trying to examine?")
        elif examine_target in Room.inventory:
            print(Room.inventory.examine_target.description)
        elif examine_target in Room.Character.name:
            print(Room.Character.examine_target.description)


    def talk_function(self, parsed_string):
        # TODO Add call to talk_function to command executor if parsed_string[0] == 'TALK'
        talk_target = parsed_string[1]

        if talk_target not in Room.Character.name:
            print("That person doesn't seem to be here. Who are you trying to talk to?")
        elif talk_target in Room.Character.name:
            print(Room.Character.talk_target.talk_output)

    def dialogue_function(self, parsed_string):
        # TODO Add call to dialogue_function to command executor if parsed_string[0] == 'ASK'.
        # TODO In command parser, user input ASK TARGET ABOUT TOPIC or ASK TARGET TOPIC should have same result.
        ask_target = parsed_string[1]
        topic = parsed_string[2]
        if ask_target not in Room.Character.name:
            print("That person doesn't seem to be here. Who are you trying to ask?")
        elif ask_target in Room.Character.name:
            print(Room.Character.ask_target.dialogue_dict[topic])


