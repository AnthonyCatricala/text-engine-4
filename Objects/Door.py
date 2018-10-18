from Objects.Lock import Lock
from Objects.Trigger import Trigger


class Door:
    is_open = None
    lock = None
    triggers = None

    def __init__(self, is_open, lock, triggers):
        self.is_open = is_open
        self.lock = lock
        self.triggers = triggers


    @classmethod
    def from_dict(cls, door_dict):
        is_open = door_dict['open']
        if door_dict['lock']:
            lock = Lock.from_dict(door_dict['lock'])
        else:
            lock = dict()
        triggers = cls.__fill_triggers(door_dict['triggers'])
        return cls(is_open, lock, triggers)

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
        out['open'] = self.is_open
        out['lock'] = self.lock.to_json()

        out['triggers'] = dict()
        for t in self.triggers:
            key, value = t.to_json()
            out[key] = value

        return out

    def lock_door(self):
        if self.lock:
            self.lock.lock()
        else:
            # TODO Flavor text for 'There is no lock on this door.'
            print()

    def unlock_door(self):
        if self.lock:
            self.lock.unlock()
        else:
            # TODO Flavor text for 'There is no lock on this door.'
            print()

    def open(self):
        if not self.is_open:
            if not self.lock or not self.lock.locked:
                # If there is no lock or it is unlocked.
                self.is_open = True
                # TODO Flavor text for door opening.
            else:
                # TODO Flavor text for 'The door is locked'
                print()
        else:
            # TODO Flavor text for 'The door is already open.'
            print()

    def close(self):
        if self.is_open:
            self.is_open = False
            # TODO Flavor text for the door closing.
        else:
            # TODO Flavor text for 'The door is already closed'
            print()
