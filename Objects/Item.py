from Objects.Door import *


class Item:
    item_name = None
    description = None
    alias = None
    quantity = None
    illuminated = None
    obtainable = None
    inventory = None
    door = None
    triggers = None
    user_scripts = None

    def __init__(self,
                 item_name: str="",
                 description: str="",
                 alias: list=None,
                 quantity: int=1,
                 illuminated: bool=False,
                 obtainable: bool=True,
                 inventory: list= None,
                 door: Door=None,
                 triggers: list=None,
                 user_scripts: list=None):

        self.item_name = item_name
        self.description = description

        if alias:
            self.alias = alias
        else:
            self.alias = list()

        self.quantity = quantity

        self.illuminated = illuminated
        self.obtainable = obtainable

        if inventory:
            self.inventory = inventory
        else:
            self.inventory = list()

        if isinstance(door, Door):
            self.door = door
        else:
            self.door = None

        if triggers and isinstance(triggers, list):
            self.triggers = triggers
        else:
            self.triggers = list()

        if user_scripts and isinstance(user_scripts, list):
            self.user_scripts = user_scripts
        else:
            self.user_scripts = list()

    @classmethod
    def from_dict(cls, item_dict):
        item_name = item_dict['item_name']
        description = item_dict['description']
        alias = cls.__fill_alias(item_dict['alias'])
        illuminated = item_dict['illuminated']
        quantity = item_dict['quantity']
        illuminated = item_dict['illuminated']
        obtainable = item_dict['obtainable']
        inventory = cls.__fill_inventory(item_dict['inventory'])

        door_dict = item_dict['door']
        if door_dict:
            door = Door.from_dict(door_dict)
        else:
            door = None

        triggers = cls.__fill_triggers(item_dict['triggers'])
        user_scripts = cls.__fill_user_scripts(['user-scripts'])

        return cls(item_name,
                   description,
                   alias,
                   quantity,
                   illuminated,
                   obtainable,
                   inventory,
                   door,
                   triggers,
                   user_scripts)


