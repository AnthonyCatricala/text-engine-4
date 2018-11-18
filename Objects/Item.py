import Objects.Door


class Item:
    item_name = None
    description = None
    alias = None
    quantity = None
    visible = None
    illuminated = None
    obtainable = None
    inventory = None
    door = None
    triggers = None
    user_scripts = None

    def __init__(self,
                 item_name: str="",
                 description: str="",
                 alias: list=None,
                 quantity: int=1,
                 visible: bool=True,
                 illuminated: bool=False,
                 obtainable: bool=True,
                 inventory: list= None,
                 door: Objects.Door.Door=None,
                 triggers: list=None,
                 user_scripts: list=None):

        self.item_name = item_name
        self.description = description

        if alias:
            self.alias = alias
        else:
            self.alias = list()

        self.quantity = quantity
        self.visible = visible
        self.illuminated = illuminated
        self.obtainable = obtainable

        if inventory:
            self.inventory = inventory
        else:
            self.inventory = list()

        if isinstance(door, Objects.Door.Door):
            self.door = door
        else:
            self.door = None

        if triggers and isinstance(triggers, list):
            self.triggers = triggers
        else:
            self.triggers = list()
        for trigger in self.triggers:
            trigger.connected_to = self

        if user_scripts and isinstance(user_scripts, list):
            self.user_scripts = user_scripts
        else:
            self.user_scripts = list()
    
    @classmethod
    def fill_inventory(cls, inventory=None):
        if not inventory:
            inventory = []

        out = []
        for i in inventory:
            out.append(cls.from_dict(i))
        return out

    @classmethod
    def from_dict(cls, item_dict):
        import Objects.Trigger
        import Objects.UserScript

        item_name = item_dict['item_name']
        description = item_dict['description']
        alias = item_dict['alias']
        quantity = item_dict['quantity']
        visible = item_dict['visible']
        illuminated = item_dict['illuminated']
        obtainable = item_dict['obtainable']

        inventory_list = item_dict['inventory']
        if isinstance(inventory_list, list):
            inventory = cls.fill_inventory(inventory_list)
        else:
            inventory = []

        door_dict = item_dict['door']
        if door_dict:
            door = Objects.Door.Door.from_dict(door_dict)
        else:
            door = None

        triggers = Objects.Trigger.Trigger.fill_triggers(item_dict['triggers'])
        user_scripts = Objects.UserScript.UserScript.fill_user_scripts(item_dict['user-scripts'])

        return cls(item_name,
                   description,
                   alias,
                   quantity,
                   visible,
                   illuminated,
                   obtainable,
                   inventory,
                   door,
                   triggers,
                   user_scripts)

    def to_json(self):
        out = dict()

        out['item_name'] = self.item_name
        out['description'] = self.description
        out['alias'] = self.alias
        out['quantity'] = self.quantity
        out['visible'] = self.visible
        out['illuminated'] = self.illuminated

        out['obtainable'] = self.obtainable

        out['inventory'] = []
        for i in self.inventory:
            out['inventory'].append(i.to_json())

        if self.door:
            out['door'] = self.door.to_json()
        else:
            out['door'] = dict()

        out['triggers'] = dict()
        if self.triggers:
            for t in self.triggers:
                key, value = t.to_json()
                out['triggers'][key] = value

        out['user-scripts'] = dict()
        if self.user_scripts:
            for s in self.user_scripts:
                key, value = s.to_json()
                out['user-scripts'][key] = value

        return out
