class Lock:
    locked = None
    key = None
    triggers = None
    user_scripts = None

    def __init__(self, locked, key, triggers, user_scripts):
        self.is_locked = locked
        self.key = key
        self.triggers = triggers
        for trigger in self.triggers:
            trigger.connected_to = self
        self.user_scripts = user_scripts

    @classmethod
    def from_dict(cls, lock_dict):
        import Objects.Trigger
        import Objects.UserScript

        locked = lock_dict['locked']
        key = lock_dict['key']
        triggers = Objects.Trigger.Trigger.fill_triggers(lock_dict['triggers'])
        user_scripts = Objects.UserScript.UserScript.fill_user_scripts(lock_dict['user-scripts'])

        return cls(locked, key, triggers, user_scripts)

    def to_json(self):
        out = dict()
        out['locked'] = self.is_locked
        out['key'] = self.key

        out['triggers'] = list()
        if self.triggers:
            for t in self.triggers:
                out['triggers'].append(t.to_json)

        out["user-scripts"] = list()
        if self.user_scripts:
            for s in self.user_scripts:
                out["user-scripts"].append(s.to_json())

        return out

    def unlock(self, player_inv):
        if self.key.replace(" ", "_") not in player_inv:
            return "you don't have the key."
        elif not self.is_locked:
            return "door was already unlocked."
        else:
            self.is_locked = False
            return "door is now unlocked."

    def lock(self, player_inv):
        if self.key.replace(" ", "_") not in player_inv:
            return "you don't have the key."
        elif self.is_locked:
            return "door was already locked."
        else:
            self.is_locked = True
            return "door is now locked."
