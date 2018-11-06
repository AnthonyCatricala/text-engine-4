import os
from Util.RoomUtil import *

class UserParser:
    room = None
    def __init__(self, room_name):
        self.room = load_room(room_name)

    def simplify_command(self, string):
        return string





