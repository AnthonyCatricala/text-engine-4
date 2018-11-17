from Objects.Lock import Lock
from Objects.Trigger import *


class Door:
    is_open = None
    lock = None
    triggers = None
    user_scripts = None

    def __init__(self, is_open, lock, triggers, user_scripts):
        self.is_open = is_open
        self.lock = lock
        self.triggers = triggers
        for trigger in self.triggers:
            trigger.connected_to = self
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
        for trigger_command, trigger_wrapper in triggers_dict.items():
            for trigger_type, args_wrapper in trigger_wrapper.items():
                if trigger_type == "print":
                    out.append(PrintTrigger(trigger_command, args_wrapper['description']))
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
            return self.lock.lock()
        else:
            return "door has no lock."

    def unlock_door(self):
        if self.lock:
            return self.lock.unlock()
        else:
            return "door has no lock."

    def open(self):
        if not self.is_open:
            if not self.lock or not self.lock.is_locked:
                # If there is no lock or it is unlocked.
                self.is_open = True
                return "door is now open."
            else:
                return "door was locked closed."
        else:
            return "door was already open."

    def close(self):
        if self.is_open:
            if not self.lock or not self.lock.is_locked:
                self.is_open = False
                return "door is now closed."
            else:
                return "door was locked open."
        else:
            return "door was already closed."
