from Objects.Exit import Exit


class Trigger(object):
    trigger_command = None
    connected_to = None

    def __init__(self, trigger_command="", connected_to=None):
        self.trigger_command = trigger_command
        self.connected_to = connected_to

    @classmethod
    def fill_triggers(cls, triggers=None):
        if not triggers:
            triggers = []

        out = []
        for t in triggers:
            if t["type"] == "print":
                out.append(PrintTrigger.from_dict(t))
        return out


class PrintTrigger(Trigger):
    # ##
    # Simple trigger for printing to the users screen.
    # ##

    def __init__(self, trigger_command="", description="", connected_to=None):
        super().__init__(trigger_command, connected_to)
        self.type = "print"
        self.description = description

    def trigger(self):
        print(self.description)

    @classmethod
    def from_dict(cls, trigger_dict):
        instance = cls()
        instance.__dict__.update(trigger_dict)
        return instance

    def to_json(self):
        out = self.__dict__
        out["connected_to"] = None
        return out


class BlockTrigger(PrintTrigger):
    # ##
    # Trigger for blocking exits.
    # ##

    def __init__(self, trigger_command="", description="", connected_to=None):
        super().__init__(trigger_command, description, connected_to)
        self.type = "block"
        self.description = description

    def trigger(self):
        print(self.description)
        if isinstance(self.connected_to, Exit):
            self.connected_to.blocked = False

    @classmethod
    def from_dict(cls, trigger_dict):
        instance = cls()
        instance.__dict__.update(trigger_dict)
        return instance

    def to_json(self):
        out = self.__dict__
        out["connected_to"] = None
        return out


class DeathTrigger(PrintTrigger):
    def __init__(self, trigger_command="", description="", connected_to=None):
        super().__init__(trigger_command, description, connected_to)

    def trigger(self):
        super().trigger()
        exit(0)


class WinTrigger(PrintTrigger):
    def __init__(self, trigger_command="", description="", connected_to=None):
        super().__init__(trigger_command, description, connected_to)

    def trigger(self):
        super().trigger()
        exit(0)


class OpenTrigger(Trigger):
    def __init__(self, trigger_command="", connected_to=None):
        super().__init__(trigger_command, connected_to)
    
    def trigger(self):
        try:
            self.connected_to.open()
        except:
            print("This cannot be opened.")
