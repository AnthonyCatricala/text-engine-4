from Objects.Door import Door
from Objects.Trigger import Trigger


class Exit:
    compass_direction = None
    links_to = None
    description = None
    blocked = None
    door = None
    triggers = None

    def __init__(self, compass_direction, links_to, description, blocked, door, triggers):
        self.compass_direction = compass_direction
        self.links_to = links_to
        self.description = description
        self.blocked = blocked
        self.door = door
        self.triggers = triggers

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

        return cls(compass_direction, links_to, description, blocked, door, triggers)

    @staticmethod
    def __fill_triggers(triggers_dict=None):
        if not triggers_dict:
            triggers_dict = dict()

        out = []
        for key, value in triggers_dict.items():
            out.append(Trigger(key, value))
        return out

    def to_json(self):
        key = self.compass_direction
        value = dict()

        value['links-to'] = self.links_to
        value['description'] = self.description
        value['blocked'] = self.blocked
        value['door'] = self.door.to_json()

        value['triggers'] = dict()
        for t in self.triggers:
            k, v = t.to_json()
            value[k] = v

        return key, value

    def open_door(self):
        if self.door:
            self.door.open()
        else:
            # TODO Flavor text for 'This exit does not have a door.
            print()

    def close_door(self):
        if self.door:
            self.door.close()
        else:
            # TODO Flavor text for 'This exit does not have a door.
            print()
