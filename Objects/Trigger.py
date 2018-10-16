# TODO Work out how new triggers will work with the CommandExecutor.


class Trigger:
    command = None
    trigger_type = None
    description = None

    def __init__(self, command, trigger_dict):
        self.command = command
