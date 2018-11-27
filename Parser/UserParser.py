import re
import Util.RoomUtil


class UserParser:
    room = None
    applicable_commands = {
        "go": ["go", "travel", "walk", "run", "enter", "g", "move"],
        "look": ["look", "l"],
        "examine": ["examine", "exam"],
        "north": ["north", "n", "northern"],
        "south": ["south", "s", "southern"],
        "east": ["east", "e", "eastern"],
        "west": ["west", "w", "western"]
    }

    def __init__(self, room_name = Util.RoomUtil.Room):
        self.room = room_name

    def remove_user_error(self, input_str):
        ##
        # Author: Lucy Oliverio
        # Description: It takes out the spaces and changes all upper case letters to lower
        ##

        out = input_str.lower()
        out = re.sub(r" {2,}", " ", out)
        return out

    def com_check(self, com_given, com_check):
        ##
        # Author: Lucy Oliverio
        # Description: Given an array of the user's input and an array of valid inputs,
        #           the program checks to see if that command is inside the user's input
        ##
        par_giv_com = com_given
        i = 0
        ch_item = None
        s = ""

        #   checks each individual command with the user's input, if it is there it increases
        #   i. If i > 1, it returns an error that the player has input
        #   too many items for the program to understand. If i = 0, it returns None.
        #   if i = 1, it returns the command in the form of a string

        for cc_ele in com_check:
            cc_ele = cc_ele.split(' ')
            while len(par_giv_com) >= len(cc_ele):
                if par_giv_com[:len(cc_ele)] == cc_ele:
                    for x in cc_ele:
                        s = s + " " + x
                    s = s[1:]
                    i = i + 1
                par_giv_com = par_giv_com[1:]
            par_giv_com = com_given

        if i == 0:
            s = ""
        if i > 1:
            s = "error"
        return s

    def cut_off_str(self, input_str, inp_cutoff_word):
        i = 0
        for x in input_str:
            if x != inp_cutoff_word:
                i = i + 1
            else:
                break
        return input_str[i+1:]

    def turn_into_array(self, list_of_object):
        list_of_exits = []
        for exit in list_of_object:
            list_of_exits.append(exit.compass_direction.replace("_", " "))
        return list_of_exits

    def refine_input(self, user_command):
        # Split the user supplied command.
        command_parts = user_command.split(" ")
        for i in range(len(command_parts)):

            # Compare to like commands and replace where needed.
            for actual_command, like_commands in self.applicable_commands.items():
                if command_parts[i] in like_commands:
                    command_parts[i] = actual_command
                    break

        return command_parts

    def chosen_obj_check(self, chosen_object, main_obj, chosen_command):
        if not (chosen_object == "" or chosen_object == "error"):
            if (chosen_command == "look") and ("lock" in main_obj):
                return ["look", "lock", "from", chosen_object.replace(" ", "_")]
            elif (chosen_command == "look") and ("door" in main_obj):
                return ["look", "door", "from", chosen_object.replace(" ", "_")]
            elif chosen_command == "look":
                return ["look", "exit", "from", chosen_object.replace(" ", "_")]
            elif (chosen_command == "go") and ("door" not in main_obj) and ("lock" not in main_obj):
                return ["go", chosen_object.replace(" ", "_"), "", ""]
            elif (chosen_command == "open") and (("door" in main_obj) or main_obj == chosen_object.split(" ")):
                return ["open", chosen_object.replace(" ", "_"), "", ""]
            elif (chosen_command == "close") and (("door" in main_obj)or main_obj == chosen_object.split(" ")):
                return ["close", chosen_object.replace(" ", "_"), "", ""]
            elif (chosen_command == "lock") and (("door" in main_obj) or ("lock" in main_obj)or main_obj == chosen_object.split(" ")):
                return ["lock", chosen_object.replace(" ", "_"), "", ""]
            elif (chosen_command == "unlock") and (("door" in main_obj) or ("lock" in main_obj)or main_obj == chosen_object.split(" ")):
                return ["unlock", chosen_object.replace(" ", "_"), "", ""]
            elif chosen_command == "block":
                return ["block", chosen_object.replace(" ", "_"), "", ""]
            elif chosen_command == "unblock":
                return ["unblock", chosen_object.replace(" ", "_"), "", ""]
    #TODO make it so doors = compass door

    def simplify_command(self, input_string):
        ##
        # Author: Lucy Oliverio
        # description: Given a string, returns
        ##

        # If given empty return empty.
        if input_string == "":
            return ["", "", "", ""]

        user_str = self.refine_input(input_string)

        #commands
        chosen_command = self.com_check(user_str, ["look", "go", "open", "close", "lock", "unlock", "block", "unblock"])
        if chosen_command == "":
            return ["error", "not a command", "", ""]
        elif chosen_command == "error":
            if self.com_check(user_str, ["go", "open", "close", "block", "unblock", "unlock"]) == "error":
                return ["error", "not a command", "", ""]
            if self.com_check(user_str, ["look", "go", "open", "close", "unlock", "block", "unblock"]) == "look":
                chosen_command = "look"
            elif self.com_check(user_str, ["look", "go", "open", "close", "unlock", "block", "unblock"]) == "unlock":
                chosen_command = "unlock"
            else:
                chosen_command = "lock"
        #takes the second half of the string (the one that recieves the action)
        main_obj = self.cut_off_str(user_str.copy(), chosen_command)
        #if the command is look only
        if (chosen_command == "look") and ((len(user_str) == 1) or (main_obj == ["around"])):
            return ["look", "", "", ""]
        if len(self.room.exits) != 0:
            temp_arr = self.turn_into_array(self.room.exits)
            chosen_object = self.com_check(main_obj, temp_arr)
            result = self.chosen_obj_check(chosen_object, main_obj, chosen_command)
            if result is not None:
                return result
        chosen_object = self.com_check(main_obj, ["north", "south", "east", "west"])
        result = self.chosen_obj_check(chosen_object, main_obj, chosen_command)
        if result is not None:
            return result
        return ["error", "not a command", "", ""]