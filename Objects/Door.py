class Door:
    open = None
    lock = None
    triggers = None

    def __init__(self, door_dict):
        self.open = door_dict['open']
        self.lock = Lock(door_dict['lock'])
        self.triggers = self.__fill_triggers(door_dict['triggers'])

    @staticmethod
    def __fill_triggers(triggers_dict):
        out = []
        for key, value in triggers_dict.items():
            out.append(Trigger(key, value))
        return out