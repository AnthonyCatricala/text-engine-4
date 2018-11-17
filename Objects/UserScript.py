class UserScript:
    before = None
    instead = None
    after = None

    def __init__(self, trigger_command="", before="", instead="", after=""):
        self.trigger_command = trigger_command
        self.before = before
        self.instead = instead
        self.after = after

    @classmethod
    def from_dict(cls, script_dict):

        for key, value in script_dict.items():
            trigger_command = key

            before = script_dict[key]['before']
            instead = script_dict[key]['instead']
            after = script_dict[key]['after']

            return cls(trigger_command, before, instead, after)

    def to_json(self):
        out_key = self.trigger_command

        out_value = dict()
        out_value['before'] = self.before
        out_value['instead'] = self.instead
        out_value['after'] = self.after

        return out_key, out_value
