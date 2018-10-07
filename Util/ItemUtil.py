

def create_object(object_name=None,
                  object_description=None,
                  alias=None,
                  illuminated=False,
                  obtainable=True,
                  inventory=None,
                  door=None,
                  triggers=None):
    # ##
    # Creates an object that the player can interact with.
    #
    # @author Dakotah Jones
    # @date 09/26/2018
    # ##
    out = None

    if object_name:
        out = dict()
        out[object_name] = dict()
        obj = out[object_name]

        if object_description:
            if type(object_description) is str:
                obj["description"] = object_description

                if alias and type(alias) is list:
                    obj["alias"] = alias
                else:
                    obj["alias"] = []
                    if type(alias) is not list:
                        # TODO Error handling for "Invalid type supplied to alias argument."
                        print()

                if type(illuminated) is bool:
                    obj["illuminated"] = illuminated
                else:
                    obj["illuminated"] = False
                    # TODO Error handling for "Invalid type supplied to illuminated argument."
                    print()

                if type(obtainable) is bool:
                    obj["obtainable"] = obtainable
                else:
                    obj["obtainable"] = True
                    # TODO Error handling for "Invalid type supplied to obtainable argument."
                    print()

                if inventory:
                    if type(inventory) is dict:
                        # TODO Add checks for correct input.
                        for key, value in inventory.items():
                            obj["inventory"] = inventory
                    else:
                        # TODO Error handling for "Invalid type supplied for inventory argument."
                        print()
                else:
                    obj["inventory"] = dict()

                if door:
                    if type(door) is dict:
                        # TODO Add checks for correct input.
                        obj["door"] = door
                    else:
                        # TODO Error handling for "Invalid type supplied for door argument."
                        print()
                else:
                    obj["door"] = dict()

                if triggers:
                    if type(triggers) is dict:
                        # TODO Add checks for correct input.
                        for key, value in triggers.items():
                            obj["triggers"][key] = value
                    else:
                        # TODO Error handling for "Invalid type supplied for triggers argument."
                        print()
                else:
                    obj["triggers"] = dict()

            else:
                # TODO Error handling for "Invalid type supplied for object description."
                print()
        else:
            # TODO Error handling for "No object description supplied."
            print()
    else:
        # TODO Error handling for "No object name supplied."
        print()

    return out


def add_light_to_object(obj=None):
    # ##
    # Adds light to an object.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if obj:
        if type(obj) is dict:
            if len(obj) == 1:
                for key, value in obj.items():
                    if "illuminated" in value:
                        value["illuminated"] = True
                    else:
                        # TODO Error handling for 'Invalid object supplied for room argument.'
                        print()
            else:
                # TODO Error handling for 'Too many objects supplied within obj argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for room argument.'
            print()
    else:
        # TODO Error handling for "No room or object supplied."
        print()


def remove_light_from_object(obj=None):
    # ##
    # Removes light from an object.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if obj:
        if type(obj) is dict:
            if len(obj) == 1:
                for key, value in obj.items():
                    if "illuminated" in value:
                        value["illuminated"] = False
                    else:
                        # TODO Error handling for 'Invalid object supplied for room argument.'
                        print()
            else:
                # TODO Error handling for 'Too many objects supplied within obj argument.'
                print()
        else:
            # TODO Error handling for 'Invalid type supplied for room argument.'
            print()
    else:
        # TODO Error handling for "No room or object supplied."
        print()


def create_alias_list():
    # ##
    # Simple return an empty list function.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    return []

def add_alias_to_alias_list(alias=None, alias_list=None):
    # ##
    # Add an alias to a standalone alias list.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if type(alias_list) is list:
        if alias:
            if type(alias) is str:
                alias_list.append(alias)
            else:
                # TODO Error Handling for "Illegal type supplied to alias argument"
                print()
        else:
            # TODO Error Handling for "No string supplied to alias argument"
            print()
    else:
        # TODO Error Handling for "Illegal type supplied to alias list argument"
        print()


def remove_alias_to_alias_list(alias=None, alias_list=None):
    # ##
    # Remove an alias to from a standalone alias list.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if type(alias_list) is list:
        if alias:
            if type(alias) is str:
                if alias in alias_list:
                    alias_list.remove(alias)
                else:
                    # TODO Error Handling for "Alias supplied was not part of the alias list."
                    print()
            else:
                # TODO Error Handling for "Illegal type supplied to alias argument"
                print()
        else:
            # TODO Error Handling for "No string supplied to alias argument"
            print()
    else:
        # TODO Error Handling for "Illegal type supplied to alias list argument"
        print()


def apply_alias_list_to_object(obj=None, alias_list=None):
    # ##
    # Sets an alias list to the supplied object
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if obj:
        if type(obj) is dict:
            if len(obj) == 1:
                for key, value in obj.items():
                    if "alias" in value:
                        if type(alias_list) is list:
                            value["alias"] = alias_list
                        else:
                            # TODO Error Handling for 'Illegal type supplied for alias list argument.
                            print()
                    else:
                        # TODO Error Handling for 'Invalid object supplied to obj argument.'
                        print()
            else:
                # TODO Error Handling for 'Too many objects supplied within obj argument.'
                print()
        else:
            # TODO Error Handling for 'Illegal type supplied to obj argument.'
            print()
    else:
        # TODO Error Handling for 'No object supplied to obj argument.'
        print()


def add_alias_to_object(obj=None, alias=None):
    # ##
    # Add an alias to an object.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if obj:
        if type(obj) is dict:
            if len(obj) == 1:
                for key, value in obj.items():
                    if "alias" in value:
                        if alias:
                            if type(alias) is str:
                                value["alias"].append(alias)
                            else:
                                # TODO Error Handling for 'Illegal type supplied for alias argument.'
                                print()
                        else:
                            # TODO Error Handling for 'No string supplied as alias argument.'
                            print()
                    else:
                        # TODO Error Handling for 'Invalid object supplied as obj argument.'
                        print()
            else:
                # TODO Error Handling for 'Too many objects supplied within obj argument.'
                print()
        else:
            # TODO Error Handling for 'Illegal type supplied to obj argument.'
            print()
    else:
        # TODO Error Handling for 'No object supplied as obj argument.'
        print()


def remove_alias_from_object(obj=None, alias=None):
    # ##
    # Add an alias to an object.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if obj:
        if type(obj) is dict:
            if len(obj) == 1:
                for key, value in obj.items():
                    if "alias" in value:
                        if alias:
                            if type(alias) is str:
                                value["alias"].remove(alias)
                            else:
                                # TODO Error Handling for 'Illegal type supplied for alias argument.'
                                print()
                        else:
                            # TODO Error Handling for 'No string supplied as alias argument.'
                            print()
                    else:
                        # TODO Error Handling for 'Invalid object supplied as obj argument.'
                        print()
            else:
                # TODO Error Handling for 'Too many objects supplied within obj argument.'
                print()
        else:
            # TODO Error Handling for 'Illegal type supplied to obj argument.'
            print()
    else:
        # TODO Error Handling for 'No object supplied as obj argument.'
        print()


def clear_object_alias_list(obj=None):
    # ##
    # Remove an alias to an object.
    #
    # @author Dakotah Jones
    # @date 10/07/2018
    # ##
    if obj:
        if type(obj) is dict:
            if len(obj) == 1:
                for key, value in obj.items():
                    if "alias" in value:
                        value["alias"] = []
                    else:
                        # TODO Error Handling for 'Invalid object supplied within obj argument.'
                        print()
            else:
                # TODO Error Handling for 'Too many objects supplied within obj argument.'
                print()
        else:
            # TODO Error Handling for 'Invalid object supplied as obj argument.'
            print()
    else:
        # TODO Error Handling for 'No object supplied as obj argument.'
        print()