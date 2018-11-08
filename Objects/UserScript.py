class UserScript:
    before = ""
    instead = ""
    after = ""

    def __init__(self, trigger_command="", before="", instead="", after=""):
        self.trigger_command = trigger_command
        self.before = before
        self.instead = instead
        self.after = after

    @classmethod
    def from_dict(cls, script_dict):
        script = "script"

        for key, value in script_dict.items():
            trigger_command = key

            before = script_dict[key]['before'][script]
            instead = script_dict[key]['instead'][script]
            after = script_dict[key]['after'][script]

            return cls(trigger_command, before, instead, after)

    # TODO Look into scoping for room and player access
    # TODO As of right now we will have to exec these strings from the engine for changes to the room and player to take place.
    ''' 
    def trigger_before(self):
        exec(self.before)

    def trigger_instead(self):
        exec(self.instead)

    def trigger_after(self):
        exec(self.after)
    '''

    def to_json(self):
        out_key = self.trigger_command

        out_value = dict()
        out_value['before'] = self.before
        out_value['instead'] = self.instead
        out_value['after'] = self.after

        return out_key, out_value
