from Objects.Trigger import Trigger


class Lock:
    locked = None
    key = None
    triggers = None

    def __init__(self, lock_dict):
        self.locked = lock_dict['locked']
        self.key = lock_dict['key']
        self.triggers = self.__fill_triggers(lock_dict['triggers'])

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
        out['locked'] = self.locked
        out['key'] = self.key
        out['triggers'] = dict()

        for t in self.triggers:
            key, value = t.to_json()
            out[key] = value

        return out
