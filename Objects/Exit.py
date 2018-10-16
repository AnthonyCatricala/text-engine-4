from Objects.Door import Door
from Objects.Trigger import Trigger


class Exit:
    compass_direction = None
    links_to = None
    description = None
    blocked = None
    door = None
    triggers = None

    def __init__(self, compass_direction, exit_dict):
        self.compass_direction = compass_direction
        self.links_to = exit_dict['links-to']
        self.description = exit_dict['description']
        self.blocked = exit_dict['blocked']
        self.door = Door(exit_dict['door'])
        self.triggers = self.__fill_triggers(exit_dict['triggers'])

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
