import os
from termcolor import colored
from colorama import init
init()

map = {
    "size": (30, 30),
    "spawns": {
        "player1": (1,1), 
        "player2": (8,8)
    },
    "smur" : [(5,5), (5,6), (6,6), (6,5)]
}

players = {
    "player1" : {
        "Michel" : {
            "type" : "barbarian",
            "level" : 1,
            "coords" : [3,4]
        }
    },
    "player2" : {
        "Klein" : {
            "type" : "mage",
            "level" : 2,
            "coords" : [16,27]
        }
    },
    "creatures" : {
        "Blork" : {
            "coords" : [12,15]
        }
    }
}


def get_coords_to_color(coordinate):

    coords_to_color = []
    
    coords_to_color.append((coordinate[0] * 4 - 4, coordinate[1] * 2 - 1))
    coords_to_color.append((coordinate[0] * 4 - 3, coordinate[1] * 2 - 1))
    coords_to_color.append((coordinate[0] * 4 - 2, coordinate[1] * 2 - 1))
    coords_to_color.append((coordinate[0] * 4 - 1, coordinate[1] * 2 - 1))
    coords_to_color.append((coordinate[0] * 4, coordinate[1] * 2 - 1))
    coords_to_color.append((coordinate[0] * 4 - 1, coordinate[1] * 2))
    coords_to_color.append((coordinate[0] * 4 + 3, coordinate[1] * 2))
    coords_to_color.append((coordinate[0] * 4 - 4, coordinate[1] * 2 + 1))
    coords_to_color.append((coordinate[0] * 4 - 3, coordinate[1] * 2 + 1))
    coords_to_color.append((coordinate[0] * 4 - 2, coordinate[1] * 2 + 1))
    coords_to_color.append((coordinate[0] * 4 - 1, coordinate[1] * 2 + 1))
    coords_to_color.append((coordinate[0] * 4, coordinate[1] * 2 + 1))

    return(coords_to_color)

def create_stats(players):
    return "Stats\n-------\nThis is cool\nchaussette\nj'ai faim\nplus que alain\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na\na"

def display_ui(map, players):

    board = ""
    stats = create_stats(players).split('\n')
    width = map["size"][0]
    height = map["size"][1]

    players_list = {} # dictionary of type { (coordinate) : [team, type] }



    colored_coordinates = {}

    smur_colored_coordinates = []

    for coordinate in map["smur"]:
        smur_colored_coordinates += get_coords_to_color(coordinate)

    colored_coordinates["smur"] = smur_colored_coordinates
    
    colored_coordinates["spawn_player1"] = get_coords_to_color(map["spawns"]["player1"])
    colored_coordinates["spawn_player2"] = get_coords_to_color(map["spawns"]["player2"])

    # We now have a dictionary which keys are the special areas (smur and the players' spawn), and which values are the coordinates that need to be colored

    for y_pos in range((height + 1) * 2):

        if y_pos == 0:
            board += '       '

        elif y_pos % 2 != 0:
            board += '   '
        x_pos = 0
        while x_pos < (width + 1) * 4:

            if (x_pos, y_pos) in colored_coordinates["smur"]:
                color = "blue"

            elif (x_pos, y_pos) in colored_coordinates["spawn_player1"]:
                color = "green"

            elif (x_pos, y_pos) in colored_coordinates["spawn_player2"]:
                color = "red"

            else:
                color = "white"


            if y_pos == 0: #on the first row

                if x_pos < width:
                    len_number = len(str(x_pos + 1))
                   
                    if len_number == 1:
                        offset = '   '

                    else:
                        offset = '  '

                    board += str(x_pos + 1) + offset #the first row shows the x coordinates


            elif y_pos == 1: #on the second row

                if x_pos == 0: #on the first position
                    board += colored('  ╔', color)

                elif x_pos < (width * 4):

                    if x_pos % 4 != 0:
                        board += colored('═', color)

                    else: 
                        board += colored('╦', color)

                elif x_pos == (width * 4): #on the last position
                    board += colored('╗', color)


            elif y_pos == ((height * 2) + 1): #on the last row

                if x_pos == 0: #on the first position
                    board += colored('  ╚', color)

                elif x_pos < (width * 4):
                
                    if x_pos % 4 != 0: 
                        board += colored('═', color)

                    else:
                        board += colored('╩', color)

                elif x_pos == (width * 4): #on the last position
                    board += colored('╝', color)


            else: #between the first and last row
                    if y_pos % 2 == 0:
                        if x_pos == 0: ##### A COMMENTER ##### (en gros, à la première position de la ligne, une ligne sur 2)

                            len_number = len(str(y_pos / 2))

                            if len_number == 3:
                                offset = '  '

                            else:
                                offset = ' '

                            board += offset + str(int(y_pos / 2))

                        else:
                            if (x_pos + 1) % 4 == 0:                        
                                board += colored('║', color)

                            else:
                                board += colored('AAA', color)
                                x_pos = x_pos + 2 # + affichage joueurs ici 

                    elif y_pos % 2 != 0 and y_pos != 1: ### A COMMENTER ###

                        if x_pos == 0: #on the first position
                            board += colored('  ╠', color)

                        elif x_pos < (width * 4):              

                            if x_pos % 4 == 0: 
                                board += colored('╬', color)

                            else:
                                board += colored('═', color)

                        elif x_pos == (width * 4): #on the last position
                            board += colored('╣', color)
            x_pos += 1    
        stats_line_to_display = ""
        
        if y_pos < len(stats):
            stats_line_to_display = stats[y_pos]

        board += '    %s\n' % stats_line_to_display
        
    print(board)


display_ui(map = map, players = players)
