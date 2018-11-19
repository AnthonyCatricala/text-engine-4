from Objects import Door
from Objects import Trigger
from Objects import UserScript


class Item:
    name = None
    alias = None
    description = None
    illuminated = False
    obtainable = False
    inventory = None
    door = None
    triggers = None
    user_scripts = None

    def __init__(self, n, al, descrip, ill, obt, invent, d, trigg, user_scrip):
        self.name = n
        self.alias = al
        self.description = descrip
        self.illuminated = ill
        self.obtainable = obt
        self.inventory = invent
        self.door = d
        self.triggers = trigg
        self.user_scripts = user_scrip

    @classmethod
    def from_dict(cls, item_name, item_dict):
        name = item_name
        alias = item_dict['alias']
        description = item_dict['description']
        illuminated = item_dict['illuminated']
        obtainable = item_dict['obtainable']
        inventory= item_dict['inventory']
        door_dict = item_dict['door']
        if door_dict:
            door = Door.from_dict(door_dict)
        else:
            door = None

        triggers = cls.__fill_triggers(item_dict['triggers'])
        user_scripts = cls.__fill_user_scripts(item_dict['user-scripts'])

        return cls(name, alias, description, illuminated, obtainable, inventory, door, triggers, user_scripts)

    @staticmethod
    def __fill_triggers(triggers_dict=None):
        if not triggers_dict:
            triggers_dict = dict()

        out = []
        for key, value in triggers_dict.items():
            out.append(Trigger(key, value))
        return out

    @staticmethod
    def __fill_user_scripts(user_script_dict=None):
        if not user_script_dict:
            user_script_dict = dict()

        out = []

        for key, value in user_script_dict.items():
            wrapper = dict()
            wrapper[key] = value

            out.append(UserScript.from_dict(wrapper))

        return out

    def to_json(self):
        key = self.name
        value = dict()

        value['alias'] = self.alias
        value['description'] = self.description
        value['illuminated'] = self.illuminated
        value['obtainable'] = self.obtainable
        value['inventory'] = self.inventory

        if self.door:
            value['door'] = self.door.to_json()
        else:
            value['door'] = dict()

        value['triggers'] = dict()
        if self.triggers:
            for t in self.triggers:
                k, v = t.to_json()
                value[k] = v

        value['user-scripts'] = dict()
        if self.user_scripts:
            for s in self.user_scripts:
                k, v = s.to_json()
                value['user-scripts'][k] = v

        return key, value