import re
import Util.RoomUtil
import Objects.Exit
import json
import os


class UserParser:
    room = None

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
            cc_ele = cc_ele.split('_')
            while len(par_giv_com) >= len(cc_ele):
                if par_giv_com[:len(cc_ele)] == cc_ele:
                    for x in cc_ele:
                        s = s + " " + x
                    s = s[1:]
                    i = i + 1
                par_giv_com = par_giv_com[1:]
            par_giv_com = com_given

        if i == 0 or i > 1:
            s = ""
        return s

    def cut_off_str(self, input_str, inp_cutoff_word):
        object_str = []
        x = ""
        while x != inp_cutoff_word:
            object_str.append(x)
            x = input_str.pop()
        return object_str[1:]

    def turn_into_array(self, list_of_object):
        list_of_exits = []
        for exit in list_of_object:
            list_of_exits.append(exit.compass_direction)
        return list_of_exits

    def refine_input(self, inp_com, temp_str1, temp_str2):
        ##
        # Author: Lucy Oliverio
        # description: Given a string, the program will replaces all key words with the correct words and spacing
        ##
        com = self.remove_user_error(inp_com)
        par_com = com.split(" ")
        i = 0
        com = ""
        is_there = False
        for x in par_com:
            for xx in temp_str1:
                for xxx in xx:
                    if x == xxx:
                        com = com + " " + temp_str2[i]
                        is_there = True
                        continue
                i = i + 1
            i = 0
            if is_there is False:
                com = com + " " + x
            elif is_there is True:
                is_there = False
        del temp_str1, temp_str2, par_com, is_there, i
        return com[1:].split()

    #TODO make it so doors = compass door
    def simplify_command(self, input_string):
        chosen_command = ""
        chosen_object = ""
        preposition = ""
        second_chosen_object = ""
        temp_str1 = {"go", "walk", "run", "enter", "g"}, {"look", "l"}, {"examine", "exam"}, {"north", "n", "northern"}, {
                        "south", "s", "southern"}, {"east", "e", "eastern"}, {"west", "w", "western"}
        temp_str2 = ["go", "look", "examine", "north", "south", "east", "west"]
        user_str = self.refine_input(input_string, temp_str1, temp_str2)
        del temp_str1, temp_str2
        print(user_str)
        #TODO fill out rest of the commands that are available
        chosen_command = self.com_check(user_str, ["look", "go", "open", "close"])
        if chosen_command == "":
            return ["error", "not a command", "", ""]
        #if the command is valid
        main_obj = self.cut_off_str(user_str.copy(), chosen_command)
        main_obj.reverse()
        #object 1
        if chosen_command == "look" and len(user_str) == 1:
            return ["look", "", "", ""]
        if len(main_obj) == 0:
            return ["error", "no object", "", ""]
        if chosen_command == "look":
            chosen_object = self.com_check(main_obj, ["north", "south", "east", "west"])
            if chosen_object != "":
                return [chosen_command, chosen_object, "", ""]
            #TODO check objects for look command
        if len(self.room.exits) != 0:
            temp_arr = self.turn_into_array(self.room.exits)
            chosen_object = self.com_check(main_obj[:], temp_arr)
            #TODO remove open and look from the if statement below when items are created
            if (chosen_command in ["open", "close"]) and (chosen_object != ""):
                return [chosen_command, "door", "from", chosen_object]
            if (chosen_command in ["go"]) and (chosen_object == ""):
                return ["Error", "invalid exit", "", ""]
            if chosen_command == "look" and (chosen_object != ""):
                place_of_obj = temp_arr.index(chosen_object.replace(" ", "_"))
                if ("door" in user_str) and (self.room.exits[place_of_obj].door is not None):
                    return [chosen_command, "door", "from", chosen_object]
                if ("door" in user_str or "lock" in user_str) and (self.room.exits[place_of_obj].door is None):
                    return ["Error", "no door", "", ""]
                if ("lock" in user_str) and (self.room.exits[place_of_obj].door.lock is not None):
                    return [chosen_command, "lock", "from", chosen_object]
                if ("lock" in user_str) and (self.room.exits[place_of_obj].door.lock is None):
                    return ["Error", "no lock", "", ""]
                return [chosen_command, "exit", "from", chosen_object]

        return [chosen_command, chosen_object, preposition, second_chosen_object]

    def testing_method(self, inp_str):
        arr = ["Help", "compass direction"]
        str = "compass direction"
        item = arr.index(str)
        print(item)





