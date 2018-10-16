from Objects.Exit import Exit
from Objects.Item import Item
from Objects.Trigger import Trigger


class Room:
    room_name = None
    room_file = None
    description = None
    illuminated = False
    inventory = None
    exits = None
    triggers = None

    def __init__(self, room_dict):
        self.room_name = room_dict['room_name']
        self.room_file = room_dict['room_file']
        self.description = room_dict['description']
        self.illuminated = room_dict['illuminated']
        self.inventory = self.__fill_inventory(room_dict['inventory'])
        self.exits = self.__fill_exits(room_dict['exits'])
        self.triggers = self.__fill_triggers(room_dict['triggers'])

    @staticmethod
    def __fill_inventory(inventory_dict):
        # TODO Come back to this (WIP)

        out = []
        for key, value in inventory_dict.items():
            out.append(Item(key, value))
        return out

    @staticmethod
    def __fill_exits(exits_dict):
        out = []
        for key, value in exits_dict.items():
            out.append(Exit(key, value))
        return out

    @staticmethod
    def __fill_triggers(triggers_dict):
        out = []
        for key, value in triggers_dict.items():
            out.append(Trigger(key, value))
        return out
