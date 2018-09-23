import re


class UserInterface:
    ##
    # Author: Lucy Oliverio
    # Date: 9/15/18
    # description: It takes out the spaces and changes all upper case letters to lower
    ##
    cr = None
    room_items = None
    __general_error = "Could not understand statement."

    def __init__(self, room):
        self.cr = room
        self.room_items = self.cr.inventory.keys()

    def remove_user_error(self, input_str):
        ##
        # Author: Lucy Oliverio
        # Date: 9/15/18
        # Description: It takes out the spaces and changes all upper case letters to lower
        ##

        out = input_str.lower()
        out = re.sub(r" {2,}", " ", out)
        return out

    def com_check(self, inp_str_arr, inp_comm_arr):
        ##
        # Author: Lucy Oliverio
        # Date: 9/16/18
        # Description: Given an array of the user's input and an array of valid inputs,
        #           the program checks to see if that command is inside the user's input
        ##
        c = None
        tem_item = inp_str_arr
        it_chosen = None
        s = ""
        i_num = 0

        #   checks each individual command with the user's input, if it is there it increases
        #   i. If i > 1, it returns an error that the player has input
        #   too many items for the program to understand. If i = 0, it returns None.
        #   if i = 1, it returns the command in the form of a string

        for x in inp_comm_arr:
            x = x.split("-")
            i = 0
            while i < len(tem_item) - len(x)+1:
                com = tem_item[len(tem_item) - len(x) - i:len(tem_item) - i]
                if com == x:
                    tem_item = tem_item[0:len(tem_item) - len(x)]
                    i_num = i_num + 1
                    it_chosen = x
                    continue
                else:
                    i = i + 1
        #   Checks to see of there is multiple valid commands
        if i_num > 1:
            print("Too many objects in word")
            return None
        elif i_num == 1 and (it_chosen[0] != 'triggers'):
            s = it_chosen[0]
            for x in it_chosen[1:]:
                s = s + "-" + x
            return s
        return None

    def refine_input(self, inp_com):
        ##
        # Author: Lucy Oliverio
        # Date: 9/17/18
        # description: Given a string, the program will replaces all key words with the correct words and spacing
        ##
        com = self.remove_user_error(inp_com)
        par_com = com.split(" ")
        temp_str1 = {"go", "g"}, {"look", "l"}, {"examine"}, {"inventory", "i", "inv"}, {
            "sleep"}, {"enter", "ent"}, {"north", "n", "northern"}, {
                        "south", "s", "southern"}, {"east", "e", "eastern"}, {"west", "w", "western"}
        temp_str2 = ["go", "look", "examine", "inventory", "sleep", "enter", "north", "south", "east", "west"]
        i = 0
        com = ""
        is_there = False
        for x in par_com:
            for xx in temp_str1:
                for xxx in xx:
                    if x == xxx:
                        com = com + " " + temp_str2[i]
                        is_there = True
                i = i + 1
            i = 0
            if is_there is False:
                com = com + " " + x
            elif is_there is True:
                is_there = False
        return com[1:].split()

    def start(self, inp_str):
        ##
        # Author: Lucy Oliverio
        # Date: 9/15/18 - 9/17/18
        # description: Given a string, it returns the simplified version of the command or None if it wasn't valid
        ##
        com_arr = self.refine_input(inp_str)
        if len(com_arr) == 1:
            if com_arr[0] == "inventory" or com_arr[0] == "examine" or com_arr[0] == "examine" or com_arr[0] == "sleep":
                return com_arr[0]
            else:
                return None
        if ("not" in com_arr) or ("dont" in com_arr) or ("never" in com_arr):
            return None

        #   if the command involves a special item
        ch_item = None
        ch_item = self.com_check(com_arr, self.room_items)
        if ch_item is not None:
            ch_com = self.com_check(com_arr, self.cr.inventory[ch_item])
            if ch_com is not None:
                return ch_com + " " + ch_item
            else:
                return None

        #   if the command is normal
        if "sleep" in com_arr:
            return "sleep"
        ch_com = self.com_check(com_arr, {"go", "examine", "enter", "look"})
        if ch_com is not None:
            ch_item = self.com_check(com_arr, {"north", "south", "east", "west", ""})
            if ch_item is not None:
                return ch_com + " " + ch_item
            return None
        #default return
        return None