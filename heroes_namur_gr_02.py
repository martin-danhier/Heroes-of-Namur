### UI ###
# Display user interface

def display_ui (players, map):
    """Displays the board (with colors) and statistics of the players, based on two dictionaries: players and map

    Parameters:
    -----------
    players: information about players and their characters (dict)
    map: information about the map, with spur and player spawns coordinates (dict)

    Version
    -------
    specification : Guillaume Nizet (v.1 01/03/19)
    """
    pass

def get_coords_to_color(coords):
    """Description of the function
    ...
    Version
    -------
    specification : Guillaume Nizet (v.1 22/02/19)
    """
    pass

def create_stats(players):
    """ Generates a string countaining the stats of the players.
    
    Parameters
    ----------
    players : a dictionnary coutaining the player data. (dict)

    Returns
    -------
    stats : a multiline string countaining the UI of the stats. (str)

    Notes
    -----
    For the format of players, see rapport_gr_02_part_02.

    Version
    -------
    specification : Martin Danhier (v.1 29/02/19)
    """
    pass

def convert_to_true_coords(coords):
    """ Converts a pair of coords to absolute char coords.

    Parameters
    ----------
    coords: a tuple of format (row (int), col (int))

    Returns
    -------
    true_coords: a tuple of format (row (int), col (int)) countaining the coords of the center char of the tile

    Version
    -------
    specification : Martin Danhier (v.1 01/02/19)
    
    """
    pass
def create_line_char():
    """"""
    pass

### INPUT ###
# Check input command written by player

def create_character():
    """Description of the function
    ...
    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.1 22/02/19)
    """
    pass

def parse_command (command):
    """"""
    

### GENERATION ###
# Use file to apply parameters of HoN

def read_file(path):
    """Description of the function
    
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
    """Description of the function
    ...
    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.1 22/02/19)
    """
    pass

### MOVE AND FIGHT ###
# Choice : Move or attack ?

def attack():
    """Description of the function
    ...
    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.1 22/02/19)
    """
    pass

def moving_on():
    """Description of the function
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