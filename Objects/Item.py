class Item:
    item_name = ""
    description = ""
    illuminated = False
    inventory = None
    triggers = None
    user_scripts = None

    def __init__(self, n, descrip, ill, invent, trigg, user_scrip):
        self.name = n
        self.description = descrip
        self.illuminated = ill
        self.inventory = invent
        self.triggers = trigg
        self.user_scripts = user_scrip