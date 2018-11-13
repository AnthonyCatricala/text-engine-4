from Objects.Lock import Lock
from Objects.Trigger import Trigger


class Door:
    is_open = None
    lock = None
    triggers = None
    user_scripts = None

    def __init__(self, is_open, lock, triggers, user_scripts):
        self.is_open = is_open
        self.lock = lock
        self.triggers = triggers
        self.user_scripts = user_scripts

    @classmethod
    def from_dict(cls, door_dict):
        is_open = door_dict['open']
        if door_dict['lock']:
            lock = Lock.from_dict(door_dict['lock'])
        else:
            lock = None
        triggers = cls.__fill_triggers(door_dict['triggers'])
        user_scripts = cls.__fill_user_scripts(door_dict['user-scripts'])
        return cls(is_open, lock, triggers, user_scripts)

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
        out = dict()
        out['open'] = self.is_open

        if self.lock:
            out['lock'] = self.lock.to_json()
        else:
            out['lock'] = dict()

        out['triggers'] = dict()
        if self.triggers:
            for t in self.triggers:
                key, value = t.to_json()
                out[key] = value

        out['user-scripts'] = dict()
        if self.user_scripts:
            for s in self.user_scripts:
                key, value = s.to_json()
                out['user-scripts'][key] = value

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
            if not self.lock or not self.lock.is_locked:
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
