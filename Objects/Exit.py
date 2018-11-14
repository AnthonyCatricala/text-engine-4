from Objects.Door import Door
from Objects.Trigger import Trigger
from Objects.UserScript import UserScript


class Exit:
    compass_direction = None
    links_to = None
    description = None
    blocked = None
    door = None
    triggers = None
    user_scripts = None

    def __init__(self, compass_direction, links_to, description, blocked=False, door=None, triggers=[], user_scripts=[]):
        self.compass_direction = compass_direction
        self.links_to = links_to
        self.description = description
        self.blocked = blocked
        self.door = door
        self.triggers = triggers
        self.user_scripts = user_scripts

    @classmethod
    def from_dict(cls, compass_direction, exit_dict):
        compass_direction = compass_direction
        links_to = exit_dict['links-to']
        description = exit_dict['description']
        blocked = exit_dict['blocked']
        door_dict = exit_dict['door']
        if door_dict:
            door = Door.from_dict(door_dict)
        else:
            door = None

        triggers = cls.__fill_triggers(exit_dict['triggers'])
        user_scripts = cls.__fill_user_scripts(exit_dict['user-scripts'])

        return cls(compass_direction, links_to, description, blocked, door, triggers, user_scripts)

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
        key = self.compass_direction
        value = dict()

        value['links-to'] = self.links_to
        value['description'] = self.description
        value['blocked'] = self.blocked
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

    def open_door(self):
        if self.door:
            print(self.compass_direction, self.door.open())
        else:
            print(self.compass_direction, "does not have a door.")

    def close_door(self):
        if self.door:
            print(self.compass_direction, self.door.close())
        else:
            print(self.compass_direction, "does not have a door.")

    def lock_door(self):
        if self.door:
            print(self.compass_direction, self.door.lock_door())
        else:
            print(self.compass_direction, "does not have a door.")

    def unlock_door(self):
        if self.door:
            print(self.compass_direction, self.door.unlock_door())
        else:
            print(self.compass_direction, "does not have a door.")

    def block(self):
        self.blocked = True

    def unblock(self):
        self.blocked = False
