import re
import Util.RoomUtil
import Help.HelpMenu
from Objects.Character import *


class UserParser:
    room = None
    player = None
    h = None
    #TODO: add item alias
    applicable_commands = {
        "go": ["go", "travel", "walk", "run", "enter", "g", "move"],
        "look": ["look", "l", "examine" "exam", "inspect "],
        "north": ["north", "n", "northern"],
        "south": ["south", "s", "southern"],
        "east": ["east", "e", "eastern"],
        "west": ["west", "w", "western"],
        "get": ["acquire", "take", "grab"],
        "inventory": ["i"]
    }

    def __init__(self, room_name = Util.RoomUtil.Room, p = Player):
        self.room = room_name
        self.player = p
        self.h = Help.HelpMenu.HelpMenu()

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

    def refine_input(self, user_command, li):
        # Split the user supplied command.
        command_parts = user_command.split(" ")
        for i in range(len(command_parts)):

            # Compare to like commands and replace where needed.
            for actual_command, like_commands in li:
                if command_parts[i] in like_commands:
                    command_parts[i] = actual_command
                    break
            temp_str = ""
        # pick up check
        for x in command_parts:
            temp_str = temp_str + " " + x
        command_parts = temp_str[1:].replace("pick up", "get").split(" ")

        return command_parts

    def chosen_exit_check(self, chosen_object, main_obj, chosen_command, obj_type, temp_arr):
        if not (chosen_object == "" or chosen_object == "error"):
            if (chosen_command == "look") and ("lock" in main_obj):
                return ["look", "lock", obj_type, chosen_object.replace(" ", "_")]
            elif (chosen_command == "look") and ("door" in main_obj):
                return ["look", "door", obj_type, chosen_object.replace(" ", "_")]
            elif chosen_command == "look":
                return ["look", obj_type, obj_type, chosen_object.replace(" ", "_")]
            elif (chosen_command == "go") and ("door" not in main_obj) and ("lock" not in main_obj):
                return ["go", chosen_object.replace(" ", "_"), obj_type, ""]
            elif (chosen_command == "open") and (("door" in main_obj) or main_obj == chosen_object.split(" ")):
                return ["open", chosen_object.replace(" ", "_"), obj_type, ""]
            elif (chosen_command == "close") and (("door" in main_obj)or main_obj == chosen_object.split(" ")):
                return ["close", chosen_object.replace(" ", "_"), obj_type, ""]
            elif (chosen_command == "lock") and (("door" in main_obj) or ("lock" in main_obj)or main_obj == chosen_object.split(" ")):
                return ["lock", chosen_object.replace(" ", "_"), obj_type, ""]
            elif (chosen_command == "unlock") and (("door" in main_obj) or ("lock" in main_obj)or main_obj == chosen_object.split(" ")):
                return ["unlock", chosen_object.replace(" ", "_"), obj_type, ""]
            elif chosen_command == "block":
                return ["block", chosen_object.replace(" ", "_"), obj_type, ""]
            elif chosen_command == "unblock":
                return ["unblock", chosen_object.replace(" ", "_"), obj_type, ""]
    #TODO make it so doors = compass door

    def error_clause(self, chosen_command):
        exit_arr = []
        room_item_arr = []
        player_item_arr = []
        all_item_arr = []
        if self.player.inventory:
            for x in self.player.inventory:
                player_item_arr.append(x.item_name.replace("_", " ").upper())
                all_item_arr.append(x.item_name.replace("_", " ").upper())
        if self.room.inventory:
            for x in self.room.inventory:
                room_item_arr.append(x.item_name.replace("_", " ").upper())
                all_item_arr.append(x.item_name.replace("_", " ").upper())
        if self.room.exits:
            for x in self.room.exits:
                exit_arr.append(x.compass_direction.replace("_", " "))
                all_item_arr.append(x.compass_direction.replace("_", " "))
        if chosen_command in ["go", "block", "unblock"]:
            return ['error', 'not a command', chosen_command, exit_arr]
        elif chosen_command in ["look", "open", "close", "unlock", "lock"]:
            return ['error', 'not a command', chosen_command, all_item_arr]
        elif chosen_command == "get":
            return ['error', 'not a command', chosen_command, room_item_arr]
        elif chosen_command == "drop":
            return ['error', 'not a command', chosen_command, player_item_arr]
        else:
            return ['error', 'not a command', "", ""]

    def alias_change(self, ls, main_obj):
        st = ""
        for x in ls:
            for mo in main_obj:
                st = st + " " + mo
            st = st[1:]
            if x.alias:
                for al in x.alias:
                    if al in st:
                        main_obj = st.replace(al, x.item_name).split(" ")
                        break
        return main_obj

    def item_check(self, main_obj, chosen_command, ls, tp):
        result = None
        temp_arr = []
        main_obj = self.alias_change(ls, main_obj)
        for x in ls:
            temp_arr.append(x.item_name.replace("_", " "))
        chosen_object = self.com_check(main_obj, temp_arr)
        if chosen_command in ["unlock", "lock", "open", "close", "look"]:
            result = self.chosen_exit_check(chosen_object, main_obj, chosen_command, tp, temp_arr)
        elif tp == "player_item" and chosen_command == "drop" and chosen_object != "" and chosen_object != "error":
            result = [chosen_command, chosen_object.replace(" ", "_"), tp, ""]
        elif tp == "room_item" and chosen_command == "get" and chosen_object != "" and chosen_object != "error":
            result = [chosen_command, chosen_object.replace(" ", "_"), tp, ""]
        return result

    def simplify_command(self, input_string):
        ##
        # Author: Lucy Oliverio
        # description: Given a string, returns the correct response
        ##
        help_choice = ""
        # If given empty return empty.
        if input_string == "":
            return ["", "", "", ""]
        # takes out the pre-determined short cuts
        temp_arr = ""
        user_str = self.refine_input(input_string, self.applicable_commands.items())
        # check for action commands
        result = None
        # inventory
        if user_str == ["inventory"]:
            return["inventory", "", "", ""]
        # other action commands
        chosen_command = self.com_check(user_str, ["look", "go", "open", "close", "lock", "unlock", "block", "unblock",
                                                   "get", "drop"])
        if chosen_command != "error":
            if self.com_check(user_str, ["help"]) == "help":
                print("\nHelp")
                #print("Please stand by, the help menu is under construction.")
                print(self.h.help_command(chosen_command))  # -- right now it breaks the code
                return ["", "", "", ""]
        if chosen_command == "" and not help_choice:
            return ["error", "not a command", "There is no action command. Active commands are:", ["look", "go", "open",
                                                                                                   "close", "lock",
                                                                                                   "unlock", "block",
                                                                                                   "unblock", "get",
                                                                                                   "drop", "help"]]
        elif chosen_command == "error":
            if self.com_check(user_str, ["go", "open", "close", "block", "unblock", "unlock"]) == "error":
                return ["error", "not a command", "", ""]
            if self.com_check(user_str, ["look", "go", "open", "close", "unlock", "block", "unblock"]) == "look":
                chosen_command = "look"
            elif self.com_check(user_str, ["look", "go", "open", "close", "unlock", "block", "unblock"]) == "unlock":
                chosen_command = "unlock"
            else:
                chosen_command = "lock"
        # takes the second half of the string (the one that receives the action)
        main_obj = self.cut_off_str(user_str.copy(), chosen_command)
        # if the command is look only
        if (chosen_command == "look") and ((len(user_str) == 1) or (main_obj == ["around"])):
            return ["look", "", "", ""]
        # Room Inventory Check:
        if self.room.inventory:
            result = self.item_check(main_obj, chosen_command, self.room.inventory, "room_item")
        # Player inventory
        if (result is None) and self.player.inventory != []:
            result = self.item_check(main_obj, chosen_command, self.player.inventory, "player_item")

        # Exits check
        if self.room.exits and (result is None):
            temp_arr = []
            for ext in self.room.exits:
                temp_arr.append(ext.compass_direction.replace("_", " "))
            chosen_object = self.com_check(main_obj, temp_arr)
            result = self.chosen_exit_check(chosen_object, main_obj, chosen_command, "exit", temp_arr)
            #print(result)
        if result is None:
            #North/south/east/west check
            chosen_object = self.com_check(main_obj, ["north", "south", "east", "west"])
            result = self.chosen_exit_check(chosen_object, main_obj, chosen_command, "exit", ["north", "south", "east",
                                                                                              "west"])
        if result is not None:
            return result
        ans = self.error_clause(chosen_command)
        return ans
