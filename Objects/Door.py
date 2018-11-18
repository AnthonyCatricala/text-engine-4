

class Door:
    is_open = None
    lock = None
    triggers = None
    user_scripts = None

    def __init__(self, is_open, lock, triggers, user_scripts):
        self.is_open = is_open
        self.lock = lock
        self.triggers = triggers
        for trigger in self.triggers:
            trigger.connected_to = self
        self.user_scripts = user_scripts

    @classmethod
    def from_dict(cls, door_dict):
        import Objects.Trigger
        import Objects.UserScript
        import Objects.Lock

        is_open = door_dict['open']
        if door_dict['lock']:
            lock = Objects.Lock.Lock.from_dict(door_dict['lock'])
        else:
            lock = None
        triggers = Objects.Trigger.Trigger.fill_triggers(door_dict['triggers'])
        user_scripts = Objects.UserScript.UserScript.fill_user_scripts(door_dict['user-scripts'])
        return cls(is_open, lock, triggers, user_scripts)

    def to_json(self):
        out = dict()
        out['open'] = self.is_open

        if self.lock:
            out['lock'] = self.lock.to_json()
        else:
            out['lock'] = dict()

        out['triggers'] = dict()
        if self.triggers:
            for t in self.triggers:
                key, value = t.to_json()
                out[key] = value

        out['user-scripts'] = dict()
        if self.user_scripts:
            for s in self.user_scripts:
                key, value = s.to_json()
                out['user-scripts'][key] = value

        return out

    def lock_door(self):
        if self.lock:
            return self.lock.lock()
        else:
            return "door has no lock."

    def unlock_door(self):
        if self.lock:
            return self.lock.unlock()
        else:
            return "door has no lock."

    def open(self):
        if not self.is_open:
            if not self.lock or not self.lock.is_locked:
                # If there is no lock or it is unlocked.
                self.is_open = True
                return "door is now open."
            else:
                return "door was locked closed."
        else:
            return "door was already open."

    def close(self):
        if self.is_open:
            if not self.lock or not self.lock.is_locked:
                self.is_open = False
                return "door is now closed."
            else:
                return "door was locked open."
        else:
            return "door was already closed."
