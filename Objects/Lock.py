class Lock:
    locked = None
    key = None
    triggers = None

    def __init__(self, lock_dict):
        self.locked = lock_dict['locked']
        self.key = lock_dict['key']
        self.triggers = self.__fill_triggers(lock_dict['triggers'])

    @staticmethod
    def __fill_triggers(triggers_dict):
        out = []
        for key, value in triggers_dict.items():
            out.append(Trigger(key, value))
        return out
