"""Dictionary
* players : name_player {name_heros : stats_heros}, name_player_2 {}
* database : name_class {lvl : default_stats_table}
* map : size - spawns {players - bot - citadel}

**don't forget nb turns of game in dictionary ===> map['turn']**
"""

### UI ###
# Display user interface


def display_ui(players, map):
    """ Displays the board (with colors) and statistics of the players.

    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)

    Notes
    -----
    For the format of players and map, see rapport_gr_02_part_02.

    Version
    -------
    specification : Guillaume Nizet (v.2 02/03/19)
    """
    pass


def get_coords_to_color(coords):
    """ Generates the coordinates that need to be colored around the given coordinates. 

    Parameters
    ----------
    coords : coordinates which need to have their surrounding coordinates colored (tuple)

    Returns
    -------
    coords_to_color : coordinates that need to be colored (tuple).

    Notes
    -----
    A typical 'coord' tuple is in the format ( row (int), column (int) ).

    Version:
    --------
    specification : Guillaume Nizet (v.2 02/03/19)
    """
    pass


def create_stats(players):
    """ Generates a string containing the stats of the players.

    Parameters:
    -----------
    players : data of player heroes and creatures (dict)

    Returns
    -------
    stats : a multiline string countaining the graphical representation of the stats. (str)

    Notes
    -----
    For the format of players, see rapport_gr_02_part_02.

    Version
    -------
    specification : Martin Danhier (v.3 02/03/19)
    """
    pass


def convert_to_true_coords(coords):
    """ Converts the given tile coordinates to absolute char coordinates.

    Parameters
    ----------
    coords: the tile coordinates to convert (tuple).
    
    Returns
    -------
    true_coords: the coordinates of the center character of the tile. (tuple)

    Notes
    -----
    A typical 'coord' tuple is in the format ( row (int), column (int) ).

    Version
    -------
    specification : Martin Danhier (v.2 02/03/19)

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
    """ Parse the input into a list of actions.
    
    Parameters
    ----------
    command: the input string to be parsed (str)
    
    Returns
    -------
    actions: a list of actions (list of dict)

    Notes
    -----
    The format of the "command" string is destribed in the instructions, p14.
    A typical "action" dict looks like this : 
        {
            'hero' : hero_name (str),
            'action' : action (str) (can be the name of an ability (as 'fulgura') or 'attack' or 'fight'),
            'coords' : ( x (int), y (int) ) (tuple, optional)
        }
    
    Version
    -------
    specification : Martin Danhier (v.1 02/03/2019)"""


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
    players : information about players and their characters : heroes and creatures (dict)

    Notes:
    ------
    'players' can be modified:
        - Heroes coordinates can be updated if they are killed 
        - Creatures can be removed from the dictionary if they are killed
        - Victory points and level of heroes can be updated if a creature is killed
    For the format of players, see rapport_gr_02_part_02.

    Version:
    --------
    specification : Guillaume Nizet (v.2 03/03/19)    
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

def attack(heroes_players):
    """ Prepare and store the attack chosen by player
    Parameters
    ----------
    hero_player: containing data for the hero who will attack and the enemy who will be attacked (dictionary)

    Notes
    -------
    parse_command() store in a list the move made. And the statistic of heroes_players updates automatically.

    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.1 22/02/19)
    """
    pass

def moving_on(hero_player, map):
    """ Prepare and update the movement chosen by player.

    Parameters
    ----------
    hero_player: hero who wants to move (dictionary)
    map: map coordinates to check differents entities (dictionary)

    Notes
    -----
    parse_command() store in a list the move made. And the coordinates of hero_player updates automatically.

    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.2 01/03/19)

    """
    pass


### CREATURES ###

def process_creatures(players):
    """ Automatically computes an action for a creature to perform:
            - does nothing if there is no hero in its area of influence or if it's not affected by any special ability
            - goes towards the nearest player if there is at least one hero in its area of influence or if it's affected by a special ability
            - attacks a player if it is right next to it

    Parameters:
    -----------
    players : information about players and their characters : heroes and creatures (dict)

    Notes:
    ------
    'players' can be modified:
        - Creatures coordinates can be updated if they move towards a player
        - Players health can be updated if they get attacked by a creature

    Version:
    --------
    specification : Guillaume Nizet (v.1 01/03/19)
    """
    pass


### AI ###

def think(players, map, database, player):
    """ Entry point of the IA: process data and create an "order string".
    
    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
    player : the name of the AI player (str)

    Returns
    -------
    command : string countaining the orders to execute (str)

    Notes
    -----
    For the format of players, map and database, see rapport_gr_02_part_02.
    The format of command is described in the instructions, p14.

    Version
    -------
    specificaation : Martin Danhier (v.1 02/03/19)
    """

### TOOLS ###


def is_coord_in_range(coords_1, coords_2):
    pass

### MAIN ###
#!One function can be lauched for 1 party!


def main():
    """ Main loop for the game, calls every function during each iteration
    
    Version:
    --------
    specification : Guillaume Nizet (v.1 01/03/19)
    """
    pass


main()
