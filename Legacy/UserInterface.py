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
                    #s = cc_ele
                    for x in cc_ele:
                        s = s + " " + x
                    s = s[1:]
                    i = i + 1
                par_giv_com = par_giv_com[1:]
            par_giv_com = com_given

        if i == 0 or i > 1:
            s = None
        return s

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

    def start(self, inp_str):
        ##
        # Author: Lucy Oliverio
        # description: Given a string, it returns the simplified version of the command or None if it wasn't valid
        ##
        s = None
        temp_str1 = {"go", "g"}, {"look", "l"}, {"examine", "exam"}, {"inventory", "i", "inv"}, {
            "sleep"}, {"enter", "ent"}, {"north", "n", "northern"}, {
                        "south", "s", "southern"}, {"east", "e", "eastern"}, {"west", "w", "western"}
        temp_str2 = ["go", "look", "examine", "inventory", "sleep", "enter", "north", "south", "east", "west"]
        com_arr = self.refine_input(inp_str, temp_str1, temp_str2)
        del temp_str1, temp_str2
        if (len(com_arr) == 1) and (com_arr[0] in {"inventory", "look", "sleep"}):
                s = com_arr[0]
        elif {"not", "dont", "never"} not in com_arr:
            #   if the command involves a special item
            ch_item = self.com_check(com_arr, self.room_items)
            if ch_item is not None:
                ch_com = self.com_check(com_arr, self.cr.inventory[ch_item])
                if ch_com is not None:
                    s = ch_com + " " + ch_item

            else:
                ch_com = self.com_check(com_arr, {"go", "examine", "enter"})
                if ch_com is not None:
                    ch_item = self.com_check(com_arr, {"north", "south", "east", "west"})
                    if ch_item is not None:
                        s = ch_com + " " + ch_item
                    else:
                        ch_item = self.com_check(com_arr, {"north_east", "south_east", "south_west", "north_west"})
                        if ch_item is not None:
                            s = ch_com + " " + ch_item
            #default return
        return s
