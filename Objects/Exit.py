from Objects.Door import Door


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
    def __fill_triggers(triggers_dict):
        out = []
        for key, value in triggers_dict.items():
            out.append(Trigger(key, value))
        return out
