import Util.RoomUtil
import json
import os

class UserParser:
    room = None

    def __init__(self, room_name):
        self.room = Util.RoomUtil.load_room(room_name)

    def simplify_command(self, String):
        return String




