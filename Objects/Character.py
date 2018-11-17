class Character:
    # TODO Add character file to room
    name = None
    inventory = None
    description = None
    character_file = None

    def __init__(self, name, inventory, description, character_file):

        self.name = name
        self.inventory = inventory
        self.description = description
        self.character_file = character_file


class Player(Character):

    alive = True
#  TODO  if not alive: game over trigger


class NPC(Character):

    talk_output = None
    dialogue_dict = None

    def dialogue(self, dialogue_dict, talk_output):

        self.dialogue_dict = dialogue_dict
        self.talk_output = talk_output

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


