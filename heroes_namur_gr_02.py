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
    For the formats of players and map, see rapport_gr_02_part_02.

    Version
    -------
    specification : Guillaume Nizet (v.2 02/03/19)
    implementation : prenom nom (v.1 06/03/19)
    
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
    implementation : prenom nom (v.1 06/03/19)
    
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
    implementation : prenom nom (v.1 06/03/19)
    
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
    implementation : prenom nom (v.1 06/03/19)
    
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
    specification : Martin Danhier (v.2 01/03/19)
    implementation : prenom nom (v.1 06/03/19)
    
    """
    pass

### INPUT ###
# Process input


def create_character(players, map, command, player):
    """ Parse the input command and create the players.

    Parameters
    ----------
    players : data of player heroes and creatures. (dict)
    map: data of the map (spawns, spur, size, etc...). (dict)
    command: the input string to be parsed. (str)
    player: the player executing the command. (str)

    Notes
    -----
    For the formats of 'players' and 'map', see rapport_gr_02_part_02.
    The 'players' dictionary is updated: one or more heroes can be added.

    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.3 02/03/2019)
    implementation : prenom nom (v.2 08/03/19)
    
    """

    #create 4 heros/player
    #choose heros

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
            'player' : player_name (str),
            'action' : action (str) (can be the name of an ability (as 'fulgura') or 'attack' or 'fight'),
            'target' : ( x (int), y (int) ) #optional
        }

    Version
    -------
    specification : Martin Danhier (v.2 02/03/2019)
    implementation : prenom nom (v.2 08/03/19)
    
    """
    #Syntax command
    # nom:type #type of character (create)
    # nom:capacity #use capacity
    # OR -> nom:capacity:r-c #use capacity, position required

    # nom:@r-c #move
    # nom:*r-c #attack




### GENERATION ###
# Create map

def read_file(path):
    """
    Reads map file and create the data structures.

    Parameters
    ----------
    path: the path of a map file (str)

    Returns
    -------
    map: data of the map (spawns, spur, size, etc...). (dict)

    Notes
    -----
    For the format of 'map', see rapport_gr_02_part_02.
    The format of a typical map file is described in the instructions, p8.

    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.3 03/03/19)
    implementation : Jonathan Nhouyvanisvong (v.2 07/03/19)
    
    """

    #coords map
    ## (range, column, turns)

    #coords spawn
    ## (range, column) x2

    #coords spur
    ## (range, column) x4

    #coords creatures
    ## (range, column, hp, dmg, rayon_influence, victory_pts) x ?

    pass

### CLEANING ###
# Clean and apply bonuses


def clean(players):
    """ Cleans the board (managing death and levels).

    Parameters
    ----------
    players : data of player heroes and creatures. (dict)

    Notes
    -----
    'players' can be updated if a hero or a creature is killed.
    For the format of 'players', see rapport_gr_02_part_02.
    More details about the rules of the cleaning can be found in the instructions, p10.

    Version
    -------
    specification : Guillaume Nizet (v.4 02/03/19)
    implementation : prenom nom (v.2 08/03/19)
    
    """

    #creatures dispawn

    #heroes revives in their spawn

    #attributes bonus
    pass

### ACTIONS ###
# Execute orders


def use_special_ability(order, players, map):
    """ Tries to execute the given ability order.

    Parameters
    ----------
    order: the ability order. (dict)
    players : data of player heroes and creatures. (dict)
    map: data of the map (spawns, spur, size, etc...). (dict)

    Notes
    -----
    The 'order' dictionary is in the following format: 
        {
            'hero' : hero_name (str),
            'player' : player_name (str),
            'action' : 'ability_name',
            'target' : ( x (int), y (int) ) #optional
        }
    For the formats of 'players' and 'map', see rapport_gr_02_part_02.
    The 'players' dictionary may be updated.

    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.3 03/03/19)
    implementation : prenom nom (v.2 08/03/19)
    
    """
    #compare class & level required
    #check ability
    #execute bonus/malus concerning active skill
    pass

def attack(order, players, map):
    """ Tries to execute the given attack order.

    Parameters
    ----------
    order: the attack order. (dict)
    players : data of player heroes and creatures. (dict)
    map: data of the map (spawns, spur, size, etc...). (dict)

    Notes
    -----
    The 'order' dictionary is in the following format: 
        {
            'hero' : hero_name (str),
            'player' : player_name (str),
            'action' : 'fight',
            'target' : ( x (int), y (int) ) #optional
        }
    For the formats of 'players' and 'map', see rapport_gr_02_part_02.
    The 'players' dictionary may be updated.

    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.3 03/03/19)
    implementation : prenom nom (v.2 08/03/19)
    
    """
    #analyze surface : is it any enemies ? -> are_coords_in_range(source, target, range)
    pass


def move_on(order, players, map):
    """ Tries to execute the given move order.

    Parameters
    ----------
    order: the attack order. (dict)
    players : data of player heroes and creatures. (dict)
    map: data of the map (spawns, spur, size, etc...). (dict)

    Notes
    -----
    The 'order' dictionary is in the following format: 
        {
            'hero' : hero_name (str),
            'player' : player_name (str),
            'action' : 'move',
            'target' : ( x (int), y (int) ) #optional
        }
    For the formats of 'players' and 'map', see rapport_gr_02_part_02.
    The 'players' dictionary may be updated.

    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.3 03/03/19)
    implementation : prenom nom (v.2 08/03/19)
    
    """
    #analyze map : wall ? player ? -> are_coords_in_range(source, target, range)
    pass


### CREATURES ###
# Process creatures

def process_creatures(players):
    """ Automatically computes an action for a creature to perform.

    Parameters:
    -----------
    players : data of player heroes and creatures (dict)

    Notes:
    ------
    For the format of 'players', see rapport_gr_02_part_02.
    The 'players' dict can be modified.

    Version:
    --------
    specification : Guillaume Nizet (v.2 03/03/19)
    implementation : prenom nom (v.2 08/03/19)
    
    """
    #actually, create a stupid AI (Exem. : It can attack but it failed because nobody here)
    # Action : left, right, up, down, attack, nothing
    pass


### AI ###
# Artificial player

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
    For the formats of 'players', 'map' and 'database', see rapport_gr_02_part_02.
    The format of 'command' is described in the instructions, p14.

    Version
    -------
    specification : Martin Danhier (v.2 02/03/19)
    implementation : prenom nom (v.1 06/03/19)
    
    """



### TOOLS ###
# Useful methods

def get_distance(coords1, coords2):
    """ Get the distance between two coordinates.

    Parameters
    ----------
    coords1: the first pair of coordinates. (tuple)
    coords2: the second pair of coordinates. (tuple)

    Returns
    -------
    distance: the distance between the two coordinates (int)

    Notes
    -----
    A typical 'coord' tuple is in the format ( row (int), column (int) ).

    Version
    -------
    specification: Martin Danhier (v.3 08/03/19)
    implementation : Guillaume Nizet (v.1 16/03/19)

    """

    # Euclidian distance formula
    return (coords2[0] - coords1[0]) ** 2 + (coords2[1] - coords1[1]) ** 2) ** 0.5

def get_tile_info(coords):
    """ Get the details of the given tile.
    
    Parameters
    ----------
    coords: the coordinates of a tile.
    
    Returns
    -------
    info : the details of the tile (str).

    Notes
    -----
    info can take the following values:
        'wall' if the tile doesn't exist.
        'player' if the tile contains a hero or a creature.
        'clear' if the tile is clear.

    Version
    -------
    specification: Martin Danhier (v.1 08/03/2019)
    implementation: void
    """

### MAIN ###
# Entry point of the game

def main():
    """ Manages the global course of the in-game events.

    Version:
    --------
    specification : Guillaume Nizet (v.2 03/03/19)
    implementation : prenom nom (v.2 08/03/19)

    """
    #Step 1 : create map and implements data
    #Step 2 : create 4 heros/player
    ##LOOP##
    #Step 3 : give order (store in list)
    #Step 4 : First clear
    #Step 5 : Lauch orders
    #Step 6 : Second clear
    #Step 7 : Check if "game over" (nb turns finished ?, 1 heros remaining ?, nb turns passed in citadel)
    pass


main()
