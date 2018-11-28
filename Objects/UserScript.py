import os

class UserScript:
    before = None
    instead = None
    after = None

    def __init__(self,
                 trigger_command: str="",
                 before: str="",
                 instead: str="",
                 after: str="",
                 before_file: str="",
                 instead_file: str="",
                 after_file: str=""):

        self.trigger_command = trigger_command

        if before_file and os.path.isfile(before_file):
            self.set_before_from_file(before_file)
        else:
            self.before = before

        if instead_file and os.path.isfile(instead_file):
            self.set_instead_from_file(instead_file)
        else:
            self.instead = instead

        if after_file and os.path.isfile(after_file):
            self.set_after_from_file(after_file)
        else:
            self.after = after

    @classmethod
    def fill_user_scripts(cls, user_scripts=None):
        if not user_scripts:
            user_scripts = list()

        out = []

        for user_script in user_scripts:
            out.append(cls.from_dict(user_script))

        return out

    @classmethod
    def from_dict(cls, script_dict):
            trigger_command = script_dict["trigger_command"]
            before = script_dict["before"]
            instead = script_dict["instead"]
            after = script_dict["after"]
            return cls(trigger_command, before, instead, after)

    def set_before_from_file(self, file_name=""):
        with open(file_name) as f:
            self.before = f.read()
        f.close()

    def set_instead_from_file(self, file_name=""):
        with open(file_name) as f:
            self.instead = f.read()
        f.close()

    def set_after_from_file(self, file_name=""):
        with open(file_name) as f:
            self.after = f.read()
        f.close()

    def to_json(self):
        out = {
            "trigger_command": self.trigger_command,
            "before": self.before,
            "instead": self.instead,
            "after": self.after
        }
        return out
