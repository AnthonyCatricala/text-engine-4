from Objects.Trigger import Trigger
from Objects.UserScript import UserScript


class Lock:
    locked = None
    key = None
    triggers = None
    user_scripts = None

    def __init__(self, locked, key, triggers, user_scripts):
        self.is_locked = locked
        self.key = key
        self.triggers = triggers
        self.user_scripts = user_scripts

    @classmethod
    def from_dict(cls, lock_dict):
        locked = lock_dict['locked']
        key = lock_dict['key']
        triggers = cls.__fill_triggers(lock_dict['triggers'])
        user_scripts = cls.__fill_user_scripts(lock_dict['user-scripts'])

        return cls(locked, key, triggers, user_scripts)

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
        out['locked'] = self.is_locked
        out['key'] = self.key

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

    def unlock(self):
        if self.is_locked:
            self.is_locked = False
        else:
            # TODO Flavor text for the door is already unlocked.
            print()

    def lock(self):
        if not self.is_locked:
            self.is_locked = True
        else:
            # TODO Flavor text for the door is already locked.
            print()
