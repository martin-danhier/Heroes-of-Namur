import os
import colored
from colorama import init
init()

map = {
    "size": (20, 20),
    "spawns": {
        "player1": (1, 1),
        "player2": (8, 8)
    },
    "spur": [(5, 5), (5, 6), (6, 6), (6, 5)]
}

players = {
    "player1": {
        "Michel": {
            "type": "barbarian",
            "level": 1,
            "coords": [3, 4]
        }
    },
    "player2": {
        "Klein": {
            "type": "mage",
            "level": 2,
            "coords": [16, 27]
        }
    },
    "creatures": {
        "Blork": {
            "coords": [12, 15]
        }
    }
}


### UI ###

def get_coords_to_color(coords):
    """insert spec here"""
    coords_to_color = []
    # For each character around the coord
    for row in range(coords[0]-1, coords[0] + 2):
        for col in range(coords[1]-2, coords[1]+3):

            # If it is a border (not center), add it
            if row != coords[0] or col not in range(coords[1]-1, coords[1]+2):
                coords_to_color.append((row, col))
    return coords_to_color

# -----------


def create_stats(players):
    """insert spec here"""
    return "Stats\n-------\nThis is cool\nchaussette\nj'ai faim\nplus que alain\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na"

# -----------


def convert_to_true_coords(coords):
    """insert spec here"""
    return (coords[0] * 2, coords[1] * 4 - 2)

def create_line_char (first, cross, last, x_pos, y_pos, color, width):
    """insert spec here"""
    if x_pos == 0:  # on the first position
        return '%s  %s' % (color, first)
    elif x_pos < (width * 4):
        if x_pos % 4 != 0:
            return '%s═' % color
        else:
            return '%s%s' % (color, cross)
    elif x_pos == (width * 4):  # on the last position
        return '%s%s' % (color, last)

def display_ui(map, players):
    """insert spec here"""

    board = "\n     "
    # Get a list of str with the stats
    stats = create_stats(players).split('\n')

    # Get data
    width = map["size"][0]
    height = map["size"][1]

    # Generate dict with coords to color
    colored_coords = {"spur": []}
    # Get colored borders around spur
    for coords in map["spur"]:
        colored_coords["spur"] += get_coords_to_color(
            convert_to_true_coords(coords))
    # Get colored borders around players spawn points
    colored_coords["spawn_player1"] = get_coords_to_color(convert_to_true_coords(
        map["spawns"]["player1"]))
    colored_coords["spawn_player2"] = get_coords_to_color(
        convert_to_true_coords(map["spawns"]["player2"]))
    # Get player coords
    #TODO

    # --------

    # Add columns numbers
    for col in range(map['size'][1]):
        if col + 1 < 10:
            board += '  %d ' % (col + 1)
        else:
            board += '  %d' % (col + 1)
    board += '\n'

    # Add board
    for y_pos in range(1, (height + 1) * 2):
        # Add tabulation to border lines
        if y_pos % 2 != 0:
            board += '   '
            
        # for each column
        x_pos = 0
        while x_pos < (4 * width) + 1:

            # Select color
            if (y_pos, x_pos) in colored_coords["spur"]:
                color = colored.fg('cyan')
            elif (y_pos, x_pos) in colored_coords["spawn_player1"]:
                color = colored.fg('green')
            elif (y_pos, x_pos) in colored_coords["spawn_player2"]:
                color = colored.fg('red')
            else:
                color = colored.attr('reset')
                   
            # First board line
            if y_pos == 1:
                board += create_line_char('╔', '╦', '╗', x_pos, y_pos, color, width)

            # Last board line
            elif y_pos == ((height * 2) + 1):  # on the last row
                board += create_line_char('╚', '╩', '╝', x_pos, y_pos, color, width)

            #Between the first and the last row
            else:
                # On center line of row
                if y_pos % 2 == 0:
                    # Display row number at the beginning of the line
                    if x_pos == 0:
                        y_row = y_pos//2
                        if y_row < 10:
                            offset = '   '
                        else:
                            offset = '  '
                        board += '%s%s %s║' % (offset, y_row, color)
                    # Board line
                    elif x_pos % 4 == 0:
                        board += '%s║' % color
                    # Tile content
                    else:
                        # Display player
                        # TODO

                        # -- concept art --
                        if x_pos//2 == 6 and y_pos//2 == 8:
                            tile_content = '%s M ' % colored.bg('dark_green')
                        else:
                            tile_content = '   '
                        # / -- concept art --

                        board += '%s' % tile_content
                        x_pos += 2

                elif y_pos != 1:
                    # Board line
                    board += create_line_char('╠', '╬', '╣', x_pos, y_pos, color, width)
    
            x_pos += 1

        # add stats
        stat_line = ''
        if y_pos-1 < len(stats):
            stat_line = stats[y_pos-1]
        board += '%s    %s\n' %  (colored.attr('reset'),stat_line)

    # Clear screen
    os.system('cls') # windows
    os.system('clear') # linux
    # Print board
    print(board)


display_ui(map, players)
