from Objects.Exit import Exit


class Trigger(object):
    trigger_command = None
    connected_to = None
    type = None

    def __init__(self, trigger_command: str="", trigger_type: str="", description: str="", connected_to=None):
        self.trigger_command = trigger_command
        self.type = trigger_type
        self.description = description
        self.connected_to = connected_to

    @classmethod
    def fill_triggers(cls, triggers: list=None):
        if not triggers:
            triggers = []

        out = []
        for t in triggers:
            if t["type"] == "print":
                out.append(PrintTrigger.from_dict(t))
            elif t["type"] == "description-change":
                out.append(ChangeDescriptionTrigger.from_dict(t))
            elif t["type"] == "block":
                out.append(BlockTrigger.from_dict(t))
            elif t["type"] == "unblock":
                out.append(UnblockTrigger.from_dict(t))

        return out

    @classmethod
    def from_dict(cls, trigger_dict):
        instance = cls()
        instance.__dict__.update(trigger_dict)
        return instance

    def to_json(self):
        out = {}
        out.update(self.__dict__)

        out["connected_to"] = None
        return out


class PrintTrigger(Trigger):
    # ##
    # Simple trigger for printing to the users screen.
    # ##

    def __init__(self, trigger_command="", description="", connected_to=None):
        super().__init__(trigger_command, "print", description, connected_to,)

    def trigger(self):
        print(self.description)


class ChangeDescriptionTrigger(Trigger):
    # ##
    # Trigger for changing the description of a WhatIF Object.
    # ##
    def __init__(self,
                 trigger_command: str="",
                 description: str="",
                 new_description: str= "",
                 connected_to=None):
        super().__init__(trigger_command, "description-change", description, connected_to)
        self.new_description = new_description

    def trigger(self):
        if self.description:
            print(self.description)
        if self.connected_to:
            self.connected_to.description = self.new_description


class BlockTrigger(Trigger):
    # ##
    # Trigger for blocking exits.
    # ##

    def __init__(self, trigger_command:str ="", description: str="", connected_to=None):
        super().__init__(trigger_command, "block", description, connected_to)

    def trigger(self):
        if self.description:
            print(self.description)
        if isinstance(self.connected_to, Exit):
            self.connected_to.blocked = True


class UnblockTrigger(Trigger):
    # ##
    # Trigger for blocking exits.
    # ##

    def __init__(self, trigger_command: str ="", description: str="", connected_to=None):
        super().__init__(trigger_command, "unblock", description, connected_to)

    def trigger(self):
        if self.description:
            print(self.description)
        if isinstance(self.connected_to, Exit):
            self.connected_to.blocked = False


class OpenTrigger(Trigger):
    # ##
    # Trigger for opening doors.
    # ##

    def __init__(self, trigger_command:str ="", description: str="", connected_to=None):
        super().__init__(trigger_command, "open", description, connected_to)

    def trigger(self):
        if self.description:
            print(self.description)

        if "is_open" in self.connected_to.__dict__.keys():
            self.connected_to.is_open = True


class CloseTrigger(Trigger):
    # ##
    # Trigger for closing doors.
    # ##

    def __init__(self, trigger_command: str = "", description: str = "", connected_to=None):
        super().__init__(trigger_command, "close", description, connected_to)

    def trigger(self):
        if self.description:
            print(self.description)

        if "is_open" in self.connected_to.__dict__.keys():
            self.connected_to.is_open = False

# TODO (WIP)
'''
class DeathTrigger(PrintTrigger):
    def __init__(self, trigger_command="", description="", connected_to=None):
        super().__init__(trigger_command, description, connected_to)

    def trigger(self):
        super().trigger()
        exit(0)
'''


class WinTrigger(PrintTrigger):
    def __init__(self, trigger_command="", description="", connected_to=None):
        super().__init__(trigger_command, description, connected_to)

    def trigger(self):
        super().trigger()
        exit(0)
