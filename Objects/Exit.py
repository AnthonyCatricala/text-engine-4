

class Exit:
    compass_direction = None
    links_to = None
    description = None
    blocked = None
    door = None
    triggers = None
    user_scripts = None

    def __init__(self, compass_direction, links_to, description, blocked=False, door=None, triggers=[], user_scripts=[]):
        self.compass_direction = compass_direction
        self.links_to = links_to
        self.description = description
        self.blocked = blocked
        self.door = door
        self.triggers = triggers
        for trigger in self.triggers:
            trigger.connected_to = self
        self.user_scripts = user_scripts

    @classmethod
    def from_dict(cls, compass_direction, exit_dict):
        import Objects.Door
        import Objects.Trigger
        import Objects.UserScript

        compass_direction = compass_direction
        links_to = exit_dict['links-to']
        description = exit_dict['description']
        blocked = exit_dict['blocked']
        door_dict = exit_dict['door']

        if door_dict:
            door = Objects.Door.Door.from_dict(door_dict)
        else:
            door = None

        triggers = Objects.Trigger.Trigger.fill_triggers(exit_dict['triggers'])
        user_scripts = Objects.UserScript.UserScript.fill_user_scripts(exit_dict['user-scripts'])

        return cls(compass_direction, links_to, description, blocked, door, triggers, user_scripts)

    @classmethod
    def fill_exits(cls, exits=None):
        if not exits:
            exits = dict()

        out = []

        if type(exits) is dict:
            for key, value in exits.items():
                out.append(cls.from_dict(key, value))
        elif type(exits) is list:
            for e in exits:
                if isinstance(e, Exit):
                    out.append(e)
                else:
                    out = []
                    # TODO Error handling for 'Exits supplied are not the right format.'
                    print()
                    break

        else:
            # TODO Error handling for 'Exits supplied are not the right format.'
            print()

        return out

    def to_json(self):
        key = self.compass_direction
        value = dict()

        value['links-to'] = self.links_to
        value['description'] = self.description
        value['blocked'] = self.blocked
        if self.door:
            value['door'] = self.door.to_json()
        else:
            value['door'] = dict()

        value['triggers'] = dict()
        if self.triggers:
            for t in self.triggers:
                k, v = t.to_json()
                value[k] = v

        value['user-scripts'] = dict()
        if self.user_scripts:
            for s in self.user_scripts:
                k, v = s.to_json()
                value['user-scripts'][k] = v

        return key, value

    def open_door(self):
        result = ""
        if self.door is not None:
            result = self.door.open()
            print(self.compass_direction, result)
        else:
            print(self.compass_direction, "door does not exist.")
        if result == "door is now open.":
            return True
        return False

    def close_door(self):
        result = ""
        if self.door:
            result = self.door.close()
            print(self.compass_direction, result)
        else:
            print(self.compass_direction, "door does not exist.")
        if result == "door is now closed.":
            return True
        return False

    def lock_door(self, player_inv):
        result = ""
        if self.door:
            result = self.door.lock_door(player_inv)
            print(self.compass_direction, result)
        else:
            print(self.compass_direction, "door does not exist.")
        if result == "door is now locked.":
            return True
        return False

    def unlock_door(self, player_inv):
        result = ""
        if self.door:
            result = self.door.unlock_door(player_inv)
            print(self.compass_direction, result)
        else:
            print(self.compass_direction, "door does not exist.")
        if result == "door is now unlocked.":
            return True
        return False

    def block(self):
        if self.blocked:
            print(self.compass_direction, "door was already blocked.")
        else:
            self.blocked = True
            print(self.compass_direction, "door is now blocked.")

    def unblock(self):
        if not self.blocked:
            print(self.compass_direction, "door was already unblocked.")
        else:
            self.blocked = False
            print(self.compass_direction, "door is now unblocked.")
