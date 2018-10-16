import os
import json


class Player:
    player_name = ""
    inventory = None
    alive = None
    win = None

    # Initialize the player
    def __init__(self, player_name=None):
        if player_name is None:
            self.player_name = "Default"
        else:
            self.player_name = player_name
        self.check_save()

    # Checks if a player save exists.
    def check_save(self):
        sav_to_check = "Saves/Player/{}.sav".format(self.player_name)
        if os.path.isfile(sav_to_check):
            with open(sav_to_check, "r") as f:
                player_data = f.read().replace("\n", "")
            loaded_data = json.loads(player_data)
            self.load_player(loaded_data)
        else:
            self.inventory = dict()
            self.alive = True
            self.win = False

            self.save_player()

    # Loads player data into the command parser.
    def load_player(self, player_data):
        self.inventory = player_data["inventory"]
        self.alive = player_data["alive"]
        self.win = player_data["win"]

    # Saves the player information to a '.sav' file.
    def save_player(self):
        player_dict = dict()
        player_dict["player_name"] = self.player_name
        if len(self.inventory) == 0:
            player_dict["inventory"] = dict()
        else:
            player_dict["inventory"] = self.inventory
        player_dict["alive"] = self.alive
        player_dict["win"] = self.win

        player_file = "Saves/Player/{}.sav".format(self.player_name.replace(" ", "_"))
        player_json = json.dumps(player_dict)
        with open(player_file, "w") as f:
            f.write(player_json)
        f.close()
