from Objects.Lock import Lock
from Objects.Trigger import Trigger


class Door:
    open = None
    lock = None
    triggers = None

    def __init__(self, door_dict):
        self.open = door_dict['open']
        if door_dict['lock']:
            self.lock = Lock(door_dict['lock'])
        else:
            self.lock = dict()
        self.triggers = self.__fill_triggers(door_dict['triggers'])

    @staticmethod
    def __fill_triggers(triggers_dict=None):
        if not triggers_dict:
            triggers_dict = dict()

        out = []
        for key, value in triggers_dict.items():
            out.append(Trigger(key, value))
        return out

    def to_json(self):
        out = dict()
        out['open'] = self.open
        out['lock'] = self.lock.to_json()

        out['triggers'] = dict()
        for t in self.triggers:
            key, value = t.to_json()
            out[key] = value

        return out