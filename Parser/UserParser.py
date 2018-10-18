import re

import Util.RoomUtil
import json
import os

class UserParser:
    room = None

    def __init__(self, room_name):
        self.room = Util.RoomUtil.load_room(room_name)

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
    def simplify_command(self, input_string):
        str = self.remove_user_error(input_string).split(" ")
        s = self.com_check(str, ["haha"])
        return s




