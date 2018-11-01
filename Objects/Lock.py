from Objects.Trigger import Trigger


class Lock:
    locked = None
    key = None
    triggers = None

    def __init__(self, locked, key, triggers):
        self.is_locked = locked
        self.key = key
        self.triggers = triggers

    @classmethod
    def from_dict(cls, lock_dict):
        locked = lock_dict['locked']
        key = lock_dict['key']
        triggers = cls.__fill_triggers(lock_dict['triggers'])
        return cls(locked, key, triggers)

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
        out['locked'] = self.is_locked
        out['key'] = self.key
        out['triggers'] = dict()

        if self.triggers:
            for t in self.triggers:
                key, value = t.to_json()
                out[key] = value

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
