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
    players : information about players and their characters (dict)

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
    
    Version:
    --------
    specification : Jonathan Nhouyvanisvong (v.1 22/02/19)
    """
    pass

### CLEANING ###
# Clean entities & attributes bonus / malus

def clean(players):
    """ Cleans the board by:
        - Removing the creatures that were killed
        - Putting back on their spawn platforms heroes that were killed
        - Giving victory points to players that are in the killed creatures areas
        - Leveling up heroes if they have enough victory points

    Parameters:
    -----------
    players : information about players and their characters (dict)

    Notes:
    ------
    'players' can be updated:
        - Heroes coordinates can be changed if they are killed 
        - Creatures can be removed from the dictionary if they are killed
        - Victory points and level of heroes can be updated if a creature is killed

    Version:
    --------
    specification : Guillaume Nizet (v.1 01/03/19)    
    """
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