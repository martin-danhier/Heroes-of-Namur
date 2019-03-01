"""Dictionary
* players : name_player {name_heros : stats_heros}, name_player_2 {}
* database : name_class {lvl : default_stats_table}
* map : size - spawns {players - bot - citadel}

**don't forget nb turns of game in dictionary**
"""

### UI ###
# Display user interface


def display_ui(players, map):
    """ Displays the board (with colors) and statistics of the players, based on two dictionaries: players and map

    Parameters:
    -----------
    players : information about players and their characters (dict)
    map : information about the map, with spur and player spawns coordinates (dict)

    Notes
    -----
    For the format of players and map, see rapport_gr_02_part_02.

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


def create_line_char(first, cross, last, y, x, color, width):
    """ Create and color a border character.

    Parameters
    ----------
    first: first intersection character of the line. (str)
    cross: intersection character in the middle of the line. (str)
    last: last intersection character of the line. (str)
    y: the ordinate of the character (int)
    x: the abcissa of the character (int)
    color: the color of the character (str)
    width: the width of the map (number of columns) (int)

    Returns
    -------
    colored_char: the char that has to be printed at the given coordinates, colored in the given color (str)

    Version
    -------
    specification : Martin Danhier (v.1 01/03/19)
    """
    pass

### INPUT ###
# Check input command written by player


def create_character(players, database):
    """ Attribute the character chosen by player and saved in main dictionary.

    Parameters
    ----------
    players: player data that will contain the chosen heroes (dictionary)
    database: containing default stats characters (dictionary)

    Notes
    -----
    For the format of players and database, see rapport_gr_02_part_02.
    The players dictionary is updated: a new hero is added.

    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.2 01/03/19)

    """
    pass


def parse_command(command):
    """"""


### GENERATION ###
# Use file to apply parameters of HoN

def read_file(path):
    """Read parameter file to complete structure of the game
    ...
    Version
    -------
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
