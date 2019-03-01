"""Dictionary
* players : name_player {name_heros : stats_heros}, name_player_2 {}
* database : name_class {lvl : default_stats_table}
* map : size - spawns {players - bot - citadel}

**don't forget nb turns of game in dictionary**
"""

### UI ###
# Display user interface

def display_ui (players, map):
    """ Displays the board (with colors) and statistics of the players, based on two dictionaries: players and map

    Parameters:
    -----------
    players : information about players and their characters (dict)
    map : information about the map, with spur and player spawns coordinates (dict)

    Version:
    --------
    specification : Guillaume Nizet (v.1 01/03/19)
    """
    pass

def get_coords_to_color(coords):
    """ Returns a list of coordinates that need to be colored, which are around the given coordinates 'coords'

    Parameters:
    -----------
    coords : coordinates which need to have their surrounding coordinates colored (tuple)

    Returns:
    --------
    coords_to_color : coordinates that need to be colored (list)

    Version:
    --------
    specification : Guillaume Nizet (v.1 1/03/19)
    """
    pass

def create_stats(players):
    """ Generates a string containing the stats of the players.
    
    Parameters:
    -----------
    players : a dictionnary

    Returns:
    --------
    stats : a multi line string countain

    Version:
    --------
    specification : Martin Danhier (v.1 28/02/19)
    """
    pass

def convert_to_true_coords():
    """"""
    pass
def create_line_char():
    """"""
    pass

### INPUT ###
# Check input command written by player

def create_character(player_dictionary, database):
"""Attribute the character chosen by player and saved in main dictionary
   Parameters
   ----------
   player_dictionary: player data that will contain the chosen heroes (dictionary)
   database: containing default stats characters (dictionary)
   
   Returns
   -------
   players_dictionary : update with a new hero (dictionary)

   Version
   -------
   specification : Jonathan Nhouyvanisvong (v.2 01/03/19)
   
   """
    pass

def parse_command (command):
    """"""
    

### GENERATION ###
# Use file to apply parameters of HoN

def read_file(path):
<<<<<<< HEAD
    """Read parameter file to complete structure of the game
    ...
=======
    """Description of the function
    
>>>>>>> e112d11bdb7e40e260f56b31ed18f021ba96e66e
    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.1 22/02/19)
    """
    pass

### CLEANING ###
# Clean entities & attributes bonus / malus

def clean():
    pass

### SPECIAL ABILITY ###
# Step : use abilities (!before CLEANING & MOVE AND FIGHT!)

def special_abilities():
    """Prepare special abilities to use
    ...
    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.1 22/02/19)
    """
    pass

### MOVE AND FIGHT ###
# Choice : Move or attack ?

def attack(player_1, player_2):
    """Prepare and store the attack chosen by player
    ...
    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.1 22/02/19)
    """
    pass

def moving_on(player, map):
    """Prepare and store the movement chosen by player
    ...
    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.1 22/02/19)
    """
    pass


### CREATURES ###

def process_creatures():
    pass

### AI ###

def think(players, map):
    pass

### TOOLS ###

def is_coord_in_range(coords_1, coords_2):
    pass

### MAIN ###
#!One function can be lauched for 1 party!

def main():
    pass

main()