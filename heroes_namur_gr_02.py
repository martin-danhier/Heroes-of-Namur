
import colored
import os
from random import randint

### UI ###
# Display user interface


def display_ui(players, map, database):
    """ Displays the board (with colors) and statistics of the players.

    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database: data of hero classes (dict)

    Notes
    -----
    For the formats of players, database and map, see rapport_gr_02_part_02.

    Version
    -------
    specification : Guillaume Nizet, Martin Danhier (v.2 16/03/19)
    implementation : Guillaume Nizet (v.2 16/03/19)
    
    """
    board = "\n     "
    # Get a list of str with the stats
    stats = create_stats(players, map, database).split('\n')

    # Get data
    width = map["size"][0]
    height = map["size"][1]

    # Generate dict with coords to color
    colored_coords = {"spur": []}
    # Get colored borders around spur
    for coords in map["spur"]:
        colored_coords["spur"] += get_coords_to_color((coords[0] * 2, coords[1] * 4 - 2))
    # Get colored borders around players spawn points
    for player in players:
        if player != 'creatures':
            colored_coords['spawn_%s' % player] = get_coords_to_color((map["spawns"][player][0] * 2, map["spawns"][player][1] * 4 - 2))
    # Get player coords
    player_coords = {}
    for player in players:
        for character in players[player]:
            coords = players[player][character]['coords']
            # If the character is a creature
            if player == 'creatures':
                player_coords[coords] = ('magenta', '*')
            else:
                # Get the number of players on the same box
                players_count = 0
                for other_character in players[player]:
                    if players[player][other_character]['coords'] == coords:
                        players_count += 1

                # If there are several characters on the box, their count is displayer
                if players_count > 1:
                    type = str(players_count)

                # If there is only 1 player on the box, its type is displayed
                else:
                    if players[player][character]['type'] == 'barbarian':
                        type = 'B'
                    elif players[player][character]['type'] == 'mage':
                        type = 'M'
                    elif players[player][character]['type'] == 'healer':
                        type = 'H'
                    elif players[player][character]['type'] == 'rogue':
                        type = 'R' 
                # Get the color of the player
                player_coords[coords] = (map['player_colors'][player], type)

    # Add column numbers
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
            
        # For each column
        x_pos = 0
        while x_pos < (4 * width) + 1:

            # Select color
            if (y_pos, x_pos) in colored_coords['spur']:
                color = colored.fg('cyan')
            else:
                found = False
                for player in players:
                    if player != 'creatures':
                        if (y_pos, x_pos) in colored_coords['spawn_%s' % player]:
                            color = colored.fg(map['player_colors'][player])
                            found = True
                if not found:
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
                        if (y_pos//2, x_pos//4 + 1) in player_coords:
                            tile_content = '%s%s %s %s' % (colored.attr('reset'), colored.bg(player_coords[(y_pos//2, x_pos//4 + 1)][0]), player_coords[(y_pos//2, x_pos//4 + 1)][1], colored.attr('reset'))
                        else:
                            tile_content = '   '

                        board += '%s' % tile_content
                        x_pos += 2

                elif y_pos != 1:
                    # Board line
                    board += create_line_char('╠', '╬', '╣', x_pos, y_pos, color, width)
    
            x_pos += 1

        # Add stats
        stat_line = ''
        if len(stats) > 0:
            stat_line = stats[0]
            stats = stats[1 :]
        board += '%s    %s\n' %  (colored.attr('reset'),stat_line)
    
    # If there is still some stats to be displayed
    if len(stats) > 0:
        for stat_line in stats:
            board += ' ' * (width * 4 + 10) + stat_line + '\n'

    # Clear screen
    os.system('cls') # windows
    os.system('clear') # linux
    # Print board
    print(board)

# -----

def get_coords_to_color(coords):
    """ Returns the coordinates that need to be colored around the given coordinates. 

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
    implementation : Guillaume Nizet (v.2 04/03/19)
    
    """
    coords_to_color = []
    # For each character around the coord
    for row in range(coords[0]-1, coords[0] + 2):
        for col in range(coords[1]-2, coords[1]+3):

            # If it is a border (not center), add it
            if row != coords[0] or col not in range(coords[1]-1, coords[1]+2):
                coords_to_color.append((row, col))
    return coords_to_color

# -----

def create_stats(players, map, database):
    """ Generates a string containing the stats of the players.

    Parameters:
    -----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...). (dict)
    database: data of hero classes (dict)

    Returns
    -------
    stats : a multiline string containing the graphical representation of the stats. (str)

    Notes
    -----
    For the formats of 'players', 'map' and 'database', see rapport_gr_02_part_02.

    Version
    -------
    specification : Martin Danhier (v.4 15/03/19)
    implementation : Martin Danhier (v.2 15/03/19)

    """
    stats = '=== TURN #%s ===' % colored.stylize(map['nb_turns'],colored.fg('light_goldenrod_1'))

    # For each player (not including creatures)
    for player in players:
        if player != 'creatures':
            # Add the name of the player
            if len(players[player]) > 0:
                stats += "\n\n%s:" % colored.stylize(player, colored.fg('light_%s' % map['player_colors'][player]))
            else:
                # The player is not playing (no hero)
                striked_name = ''
                for character in player:
                    striked_name += '\u0336' + character 
                stats += '\n\n%s' % colored.stylize(striked_name, colored.fg('light_%s' % map['player_colors'][player]))
            
            # Add hero data
            for hero in players[player]:
                active_effects = players[player][hero]['active_effects']
                hero_class_data = database[players[player][hero]['type']][players[player][hero]['level']]

                # Get damage
                damage = hero_class_data['dmg']
                if 'stun' in active_effects:
                    damage -= active_effects['stun'][1] #new damage = initial damage - x
                if 'energise' in active_effects:
                    damage += active_effects['energise'][1] #new damage = initial damage + x
                if damage < 1:
                    damage = 1 #no damage below 1

                # Color damage
                if damage < hero_class_data['dmg']:
                    damage_color = 'light_red'
                elif damage == hero_class_data['dmg']:
                    damage_color = 'light_goldenrod_1'
                else:
                    damage_color = 'light_green'
                damage = colored.stylize('%d' % damage, colored.fg(damage_color))

                # Display general stats.
                stats += '\n - \'%s\', %s:\n   (HP: %s, XP: %s, LVL: %s, DMG: %s)\n   Position: (%s, %s)' % (
                    colored.stylize(hero, colored.fg('light_%s' % map['player_colors'][player])), players[player][hero]['type'],
                    colored.stylize(players[player][hero]['hp'], colored.fg('light_goldenrod_1')), colored.stylize(players[player][hero]['xp'], colored.fg('light_goldenrod_1')), colored.stylize(players[player][hero]['level'], colored.fg('light_goldenrod_1')),
                     damage, colored.stylize(players[player][hero]['coords'][0], colored.fg('light_goldenrod_1')), colored.stylize(players[player][hero]['coords'][1], colored.fg('light_goldenrod_1')))
                
                # Display abilities stats.
                nb_abilities = len(players[player][hero]['cooldown'])

                # Display them if there are some abilities to display
                if (nb_abilities > 0):
                    stats += '\n   Special abilities: '    
                    for index_ability in range(nb_abilities):
                        # Get data from databases.
                        ability_name = hero_class_data['abilities'][index_ability]['name']
                        ability_cooldown = players[player][hero]['cooldown'][index_ability]
                        # Add the name of the ability and the number of turns left before being able to use it again.
                        if ability_cooldown == 0:
                            stats += ' %s (%s)' % (ability_name, colored.stylize('ready', colored.fg('light_goldenrod_1')))
                        else:
                            stats += '%s (%s turns left)' % (ability_name, colored.stylize(ability_cooldown, colored.fg('light_goldenrod_1')))
                        # Add a comma to separate abilities
                        if nb_abilities > 1 and index_ability < nb_abilities - 1:
                            stats += ','
                else:
                    stats += "\n   No special ability."

                # Display active effects
                index = 0
                if len(active_effects) > 0:
                    stats += '\n   Active effects: '
                    for effect in active_effects:
                        stats += '%s (%s turns left)' % (effect, colored.stylize(active_effects[effect][0], colored.fg('light_goldenrod_1')))
                        # Add a comma to separate effects
                        if index < len(active_effects) - 1:
                            stats += ', '
                        index += 1

    # Return the full stats string
    return stats

# -----

def create_line_char(first, cross, last, x, y, color, width):
    """ Create and color a border character.

    Parameters
    ----------
    first: first intersection character of the line. (str)
    cross: intersection character in the middle of the line. (str)
    last: last intersection character of the line. (str)
    x: the abcissa of the character (int)
    y: the ordinate of the character (int)
    color: the color of the character (str)
    width: the width of the map (number of columns) (int)

    Returns
    -------
    colored_char: the char that has to be printed at the given coordinates, colored in the given color (str)

    Version
    -------
    specification : Martin Danhier (v.3 16/03/19)
    implementation : Martin Danhier (v.2 02/03/19)
    """
    if x == 0:  # on the first position
        return '%s  %s' % (color, first)
    elif x < (width * 4):
        if x % 4 != 0:
            return '%s═' % color
        else:
            return '%s%s' % (color, cross)
    elif x == (width * 4):  # on the last position
        return '%s%s' % (color, last)

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
    implementation : Guillaume Nizet (v.3 20/03/19)
    
    """
    # First, check the validity of the command

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    list_types = ['mage', 'barbarian', 'healer', 'rogue']

    command_is_valid = True

    orders = command.split(' ')
    for order_index in range(len(orders)):
        if order_index < 4:
            info = orders[order_index].split(':')
            if len(info) == 2:
                if len(info[0]) != 0 and len(info[1]) != 0:
                    for character in info[0]:

                        # If the name contains numbers or symbols
                        if character not in alphabet:
                            command_is_valid = False

                    # If the hero type in not valid
                    if info[1] not in list_types:
                        command_is_valid = False

                # If the given hero name or type is empty
                else:
                    command_is_valid = False
            
            # If the command is not in the format 'name' : 'type'
            else:
                command_is_valid = False

            # Do not add heroes that have the same name (keeping the first one)
            if command_is_valid and info[0] not in players[player]:
                    players[player][info[0]] = { 'type' : info[1], 'level' : '1', 'hp' : 10, 'xp' : 0, 'coords' : map['spawns'][player], 'cooldown' : [], 'active_effects' : {}}



# -----

def parse_command(player, command, players, database):
    """ Parse the input into a list of actions.

    Parameters
    ----------
    player: the player that entered the command (str)
    command: the input string to be parsed (str)
    players: data of player heroes and creatures. (dict)
    database : data of hero classes (dict)

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
    For the formats of 'players' and 'database', see rapport_gr_02_part_2.

    Version
    -------
    specification : Martin Danhier (v.3 20/03/2019)
    implementation : Martin Danhier (v.1 20/03/2019)

    """

    actions = []
    abilities_requiring_target = ('immunise', 'fulgura', 'ovibus', 'reach')
    other_abilities = ('energise', 'stun', 'invigorate', 'burst')

    # For each order
    for order_index in range(len(command.split(' '))):
        info = command.split(' ')[order_index].split(':')
        # Basic check: it's useless to lose time if it is false
        if (len(info) == 2 or len(info) == 3) and order_index < 4:

            # Step 1 : CHECK HERO
            if len(info[0]) > 0 and len(info[1]) > 1:
                found = False
                # Check in actions
                for checked_order in actions:
                    if checked_order['hero'] == info[0]:
                        found = True
                # A hero can receive maximum one order each turn
                if not found:
                    exists = False
                    # Does this hero even exist ?
                    for checked_hero in players[player]:
                        if checked_hero == info[0]:
                            exists = True
                    if exists and 'ovibus' not in players[player][info[0]]['active_effects']:
                        # the hero exists and can be ordered something

                        # Step 2: GET ACTION AND TARGET
                        target = ''
                        action_name = ''
                        # Without third info
                        if len(info) == 2:
                            # Ability
                            if info[1] in other_abilities:
                                action_name = info[1]
                            else:
                                # Attack or move
                                target = info[1][1:]
                                if info[1][0] == '@':
                                    action_name = 'move'
                                elif info[1][0] == '*':
                                    action_name = 'attack'
                        # With third info
                        elif info[1] in abilities_requiring_target and len(info[2]) >= 3:
                            action_name = info[1]
                            target = info[2]

                        if action_name != '':

                            valid = False
                            # Step 3 : CHECK THE ACTION
                            if action_name in ('attack', 'move'):
                                valid = True
                            else:
                                # Check if the given ability is available for the hero (right class, right level and cooldown = 0)
                                available_abilities = database[players[player][info[0]]['type']][players[player][info[0]]['level']]['abilities']
                                for index in range(len(available_abilities)):
                                    if info[1] == available_abilities[index]['name'] and players[player][info[0]]['cooldown'][index] == 0:
                                        valid = True

                            # Step 4: STORE THE ACTION
                            if valid:
                                if target == '':
                                    actions.append(
                                        {'player': player, 'hero': info[0], 'action': action_name})
                                else:
                                    # parse the coordinates before storing
                                    splitted_target = target.split('-')
                                    if len(splitted_target) == 2 and splitted_target[0].isdigit() and splitted_target[1].isdigit():
                                        actions.append({'player': player, 'hero': info[0], 'action': action_name, 'target': (int(splitted_target[0]), int(splitted_target[1]))})
    return actions


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
    players: data of players (players, creatures) (dict)

    Notes
    -----
    For the format of 'map', see rapport_gr_02_part_02.
    The format of a typical map file is described in the instructions, p8.
    The 'players' dictionnary will be incomplete, use create_character() to add heroes.

    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.4 15/03/19)
    implementation : Martin Danhier (v.5 19/03/19)
    
    """
    # Get lines from the given file.
    param_file = open(path, 'r')
    param_list = [line.strip('\n') for line in param_file.readlines()]
    param_file.close()

    # Initialize the data dictionaries.
    players = {'creatures': {}}
    map = {'spawns': {}, 'spur': [], 'player_in_citadel': ('', 0), 'nb_turns' : 1, 'nb_turns_without_action' : 0}

    # Initialize some variables for the loop.
    current = ''
    line_in_current = 0

    # For each line,
    for line in param_list:
        # Check if a new file section has been reached.
        if line in ('map:', 'spawn:', 'spur:', 'creatures:'):
            current = line
            line_in_current = 0
        else:
            # Split the data.
            info = line.split(' ')

            # Save the values in the corresponding data dictionnary.
            if current == 'map:':
                map['size'] = (int(info[0]), int(info[1]))
                map['nb_turns_to_win'] = int(info[2])
            elif current == 'spawn:':
                map['spawns']['Player %d' % line_in_current] = (
                    int(info[0]), int(info[1]))
                # Initialize a dictionary for the heroes of that player.
                players['Player %d' % line_in_current] = {}
            elif current == 'spur:':
                map['spur'].append((int(info[0]), int(info[1])))
            elif current == 'creatures:':
                players['creatures'][info[0]] = {'coords': (int(info[1]), int(info[2])), 'hp': int(
                    info[3]), 'dmg': int(info[4]), 'radius': int(info[5]), 'xp': int(info[6])}

        # Increment the line counter.
        line_in_current += 1

    # Return the final dictionaries.
    return players, map

### CLEAN AND UPDATES ###
# Clean, apply bonuses, update cooldowns...


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

def update_counters(players, map):
    """ Decrements cooldowns and increments turn counters.

    Parameters
    ----------
    players : data of player heroes and creatures. (dict)
    map: data of the map (spawns, spur, size, etc...). (dict)

    Notes
    -----
    For the formats of 'players' and 'map', see rapport_gr_02_part_02.
    The 'players' and 'map' dictionaries may be updated.

    Version
    -------
    specification: Martin Danhier (v.1 22/03/2018)
    implementation: Martin Danhier (v.1 22/03/2018)
    """
    # For each hero that is not a creature
    for player in players:
        if player != 'creatures':
            for hero in players[player]:
                
                # Step 1: DECREMENT ABILITIES COOLDOWN
                # For each cooldown of that hero
                cooldowns = players[player][hero]['cooldown']
                for cooldown_index in range(len(cooldowns)):
                    # Decrement the cooldown if it is strictly positive (0 = ready to use)
                    if cooldowns[cooldown_index] > 0:
                       cooldowns[cooldown_index] -= 1

                # Step 2: DECREMENT ACTIVE EFFECTS COOLDOWN
                # For each active effect of that hero
                effects = players[player][hero]['active_effects']
                new_dict = {}
                for effect in effects:
                    # Decrement the cooldown (0 = end of the effect)
                    effects[effect] = (effects[effect][0] - 1, effects[effect][1])
                    # If the cooldown of an effect reached 0, remove that effect
                    # <=> only keep the elements with a strictly positive cooldown
                    # This workaround avoids the RuntimeError "dict changed size during iteration"
                    if effects[effect][0] > 0:
                        new_dict[effect] = effects[effect]
                players[player][hero]['active_effects'] = new_dict

    # Increment turn counter
    map['nb_turns'] += 1
    # Increment turns without action counter
    map['nb_turns_without_action'] += 1
    # Increment citadel counter
    if map['player_in_citadel'][0] != '':
        map['player_in_citadel'] = (map['players_in_citadel'][0], map['players_in_citadel'][1] + 1)

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


def attack(order, players, map, database):
    """ Tries to execute the given attack order.

    Parameters
    ----------
    order: the attack order (dict)
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database: data of hero classes (dict)

    Notes
    -----
    The 'order' dictionary is in the following format: 
        {
            'hero' : hero_name (str),
            'player' : player_name (str),
            'action' : 'fight',
            'target' : ( x (int), y (int) ) #optional
        }
    For the formats of 'players', 'database' and 'map', see rapport_gr_02_part_02.
    The 'players' dictionary may be updated.

    Version
    -------
    specification : Jonathan Nhouyvanisvong (v.4 19/03/19)
    implementation : Guillaume Nizet (v.2 19/03/19)
    
    """
    # If the target tile is occupied by a player or a creature and if it's not the spawn point of any player and if it's not farther than square root of 2 (to be able to attack diagonally)
    if get_tile_info(order['target'], players, map) == 'player' and order['target'] != map['spawns']['Player 1'] and order['target'] != map['spawns']['Player 2'] and get_distance(players[order['player']][order['hero']]['coords'], order['target']) <= 2 ** 0.5:
        
        # Base damage of the hero, based on its type and level
        damage = database[players[order['player']][order['hero']]['type']][players[order['player']][order['hero']]['level']]['dmg']
        
        # Process abilities that can modify the damage

        # Get active effects
        active_effects = players[order['player']][order['hero']]['active_effects']
        
        # Energise increases the damage
        if 'energise' in active_effects:
            damage += active_effects['energise'][1]
        
        # Stun decreases the damage
        if 'stun' in active_effects:
            damage -= active_effects['stun'][1]

        # Damage cannot be less than 1
        if damage < 1:
            damage = 1

        # Then find the player or the creature on that tile
        for player in players:
            for hero in players[player]:
                if players[player][hero]['coords'] == order['target']:


                    # If the target is affected by the ability 'immunise'
                    if player != 'creatures' and 'immunise' in players[player][hero]['active_effects']:
                        damage = 0
                    
                    # Health of the target = its previous health - damage points of the active hero
                    target_hp = players[player][hero]['hp'] - damage
                    
                    # If the target is going to be killed, its hp is set back to 0.
                    if target_hp <= 0:
                        players[player][hero]['hp'] = 0
                    else:
                        players[player][hero]['hp'] = target_hp
                    
                    # Reset no-action counter
                    map['nb_turns_without_action'] = 0

# -----

def move_on(order, players, map):
    """ Tries to execute the given move order.

    Parameters
    ----------
    order: the move order. (dict)
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
    # If the target tile is clear and not farther than square root of 2 (to be able to move diagonally)
    if get_tile_info(order['target'], players, map) == 'clear' and get_distance(players[order['player']][order['hero']]['coords'], order['target']) <= (2 ** 0.5):
        players[order['player']][order['hero']]['coords'] = order['target']


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
    implementation : Jonathan Nhouyvanisvong (v.2 21/03/19)

    """
    order = []
    capacity = ('energise', 'invigorate', 'stun', 'burst', 'immunise', 'fulgura', 'ovibus', 'reach')
    command = ''

    for hero in players[player]:
        # Generate target coordinates
        choice = randint(0, 3)
        hero_coords = players[player][hero]['coords'] # (..., ...)
        
        coords_1 = hero_coords[0] + (randint(0, 1) * 2) - 1
        coords_2 = hero_coords[1] + (randint(0, 1) * 2) - 1
        coords = '%d-%d' % (coords_1, coords_2)

        # keep to reflect about ability
        # coords_1 = randint(1,4)
        # coords_2 = randint(1,4)
        # coords = '%d-%d' % (coords_1, coords_2)

        # Check choice
        if choice == 1: #move
            order.append(str(hero) + ':@' + str(coords)) # nom:@r-c
        elif choice == 2: #attack
            order.append(str(hero) + ':*' + str(coords)) # nom:*r-c
        elif choice == 3: #use ability 
            id = randint(0, len(capacity) - 1)
            if capacity[id] in capacity[4:]: # capacity which need coords
                order.append(str(hero) + ':' + str(capacity[id]) + ':' + str(coords)) # nom:capacity:r-c
            else:
                order.append(str(hero) + ':' + capacity[id]) # nom:capacity
    
    #store commands
    for index, order_done in enumerate(order):
        command += order_done
        if index != len(order) - 1:
            command += ' '

    return command


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
    return ((coords2[0] - coords1[0]) ** 2 + (coords2[1] - coords1[1]) ** 2) ** 0.5

# -----

def get_tile_info(coords, players, map):
    """ Get the details of the given tile.

    Parameters
    ----------
    coords: the coordinates of a tile. (tuple)
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)

    Returns
    -------
    info : the details of the tile (str).

    Notes
    -----
    info can take the following values:
        'wall' if the tile doesn't exist.
        'player' if the tile contains a hero or a creature.
        'clear' if the tile is clear.
    For the formats of players and map, see rapport_gr_02_part_02.
    A typical 'coord' tuple is in the format ( row (int), column (int) ).

    Version
    -------
    specification: Martin Danhier (v.2 16/03/2019)
    implementation: Martin Danhier (v.1 16/03/2019)
    """
    # If the coordinates are out of the map.
    if coords[0] <= 0 or coords[0] > map['size'][0] or coords[1] <= 0 or coords[1] > map['size'][1]:
        return 'wall'
    else:
        # For each hero / creature, check if its coords are equal to tested ones.
        for player in players:
            for individual in players[player]:
                if players[player][individual]['coords'] == coords:
                    return 'player'
        # If this code is reached, then the tile is clear.
        return 'clear'


### MAIN ###
# Entry point of the game

def main(file, AI_repartition = { 'Player 1' : False, 'Player 2' : True}, player_colors = { 'Player 1' : 'green', 'Player 2' : 'red'} ):
    """ Manages the global course of the in-game events.

    Parameters
    ----------
    file: the path of the .hon file used to generate the map. (str)
    AI_repartition: a value is True if the corresponding player must be controlled by the computer (tuple of boolean) (optional)
    player_colors: the colors of each player (tuple of str) (optional)

    Version:
    --------
    specification : Guillaume Nizet, Martin Danhier (v.3 20/03/19)
    implementation : Martiin Danhier (v.2 20/03/19)

    """

    # Create the constant database dictionary containg the data of each class at each level
    database = {
        'barbarian': {
            '1': {'victory_pts': 0, 'hp': 10, 'dmg': 2, 'abilities':[]},
            '2': {'victory_pts': 100, 'hp': 13, 'dmg': 3, 'abilities': [{'name': 'energise', 'radius': 1, 'x': 1, 'cd': 1}]},
            '3': {'victory_pts': 200, 'hp': 16, 'dmg': 4, 'abilities': [{'name': 'energise', 'radius': 2, 'x': 1, 'cd': 1}, {'name': 'stun', 'radius': 1, 'x': 1, 'cd': 1}]},
            '4': {'victory_pts': 400, 'hp': 19, 'dmg': 5, 'abilities': [{'name': 'energise', 'radius': 3, 'x': 2, 'cd': 1}, {'name': 'stun', 'radius': 2, 'x': 2, 'cd': 1}]},
            '5': {'victory_pts': 800, 'hp': 22, 'dmg': 6, 'abilities': [{'name': 'energise', 'radius': 4, 'x': 2, 'cd': 1}, {'name': 'stun', 'radius': 3, 'x': 3, 'cd': 1}]}
        },
        'healer': {
            '1': {'victory_pts': 0, 'hp': 10, 'dmg': 2, 'abilities':[]},
            '2': {'victory_pts': 100, 'hp': 11, 'dmg': 2, 'abilities': [{'name': 'invigorate', 'radius': 1, 'x': 1, 'cd': 1}]},
            '3': {'victory_pts': 200, 'hp': 12, 'dmg': 3, 'abilities': [{'name': 'invigorate', 'radius': 2, 'x': 2, 'cd': 1}, {'name': 'immunise', 'radius': 1, 'cd': 3}]},
            '4': {'victory_pts': 400, 'hp': 13, 'dmg': 3, 'abilities': [{'name': 'invigorate', 'radius': 3, 'x': 3, 'cd': 1}, {'name': 'immunise', 'radius': 2, 'cd': 3}]},
            '5': {'victory_pts': 800, 'hp': 14, 'dmg': 4, 'abilities': [{'name': 'invigorate', 'radius': 4, 'x': 4, 'cd': 1}, {'name': 'immunise', 'radius': 3, 'cd': 3}]}
        },
        'mage': {
            '1': {'victory_pts': 0, 'hp': 10, 'dmg': 2, 'abilities':[]},
            '2': {'victory_pts': 100, 'hp': 12, 'dmg': 3, 'abilities': [{'name': 'fulgura', 'radius': 1, 'x': 3, 'cd': 1}]},
            '3': {'victory_pts': 200, 'hp': 14, 'dmg': 4, 'abilities': [{'name': 'fulgura', 'radius': 2, 'x': 3, 'cd': 1}, {'name': 'ovibus', 'radius': 1, 'x': 1, 'cd': 3}]},
            '4': {'victory_pts': 400, 'hp': 16, 'dmg': 5, 'abilities': [{'name': 'fulgura', 'radius': 3, 'x': 4, 'cd': 1}, {'name': 'ovibus', 'radius': 2, 'x': 2, 'cd': 3}]},
            '5': {'victory_pts': 800, 'hp': 18, 'dmg': 6, 'abilities': [{'name': 'fulgura', 'radius': 4, 'x': 4, 'cd': 1}, {'name': 'ovibus', 'radius': 3, 'x': 2, 'cd': 3}]}
        },
        'rogue': {
            '1': {'victory_pts': 0, 'hp': 10, 'dmg': 2, 'abilities':[]},
            '2': {'victory_pts': 100, 'hp': 12, 'dmg': 3, 'abilities': [{'name': 'reach', 'radius': 1, 'cd': 1}]},
            '3': {'victory_pts': 200, 'hp': 14, 'dmg': 4, 'abilities': [{'name': 'reach', 'radius': 2, 'cd': 1}, {'name': 'burst', 'radius': 1, 'x': 1, 'cd': 1}]},
            '4': {'victory_pts': 400, 'hp': 16, 'dmg': 5, 'abilities': [{'name': 'reach', 'radius': 3, 'cd': 1}, {'name': 'burst', 'radius': 2, 'x': 2, 'cd': 1}]},
            '5': {'victory_pts': 800, 'hp': 18, 'dmg': 6, 'abilities': [{'name': 'reach', 'radius': 4, 'cd': 1}, {'name': 'burst', 'radius': 3, 'x': 3, 'cd': 1}]}
        }
    }

    # Step 1 : create map and implements data
    players, map = read_file('test.hon')

    # Save the player colors
    map['player_colors'] = {'Player %d' % (index + 1) : player_colors[index] for index in range(len(player_colors))}
    
    # Convert AI repartition to a dictionary
    AI_repartition = {'Player %d' % (index + 1) : AI_repartition[index] for index in range(len(AI_repartition))}

    # Step 2 : create 4 heroes/player
    for player in players:
        if player != 'creatures':
            # Display UI several times to prevent cheating if there are more than one human player.
            display_ui(players, map, database)
            if AI_repartition[player]: # AI
                command = 'Blork:mage Groumpf:barbarian Azagdul:healer Bob:rogue' # Naive AI for now
            else: # Human
                command = input('%s, Create 4 heroes:\n>>> ' % colored.stylize(player, colored.fg('light_%s' % map['player_colors'][player])))
            create_character(players, map, command, player)

    # Main loop
    game_is_over = False
    while not game_is_over:

        # Step 3 : give order (store in list)
        orders = []
        for player in players:
            if player != 'creatures' and len(players[player]) > 0:
                # Display UI several times to prevent cheating if there are more than one human player.
                display_ui(players, map, database)
                if AI_repartition[player]: # AI
                    command = think(players, map, database, player)
                else: # Human
                    command = input('%s, Enter orders:\n>>> ' % colored.stylize(player, colored.fg('light_%s' % map['player_colors'][player])))
                
                #Save orders
                orders += parse_command(player, command, players, database)

        # Step 4 : Use special abilities
        # TODO missing function USE_SPECIAL_ABILITY

        # Step 4 : First clear
        # clean(players)

        # Step 5 : Move & Fight
        for order in orders:
            if order['action'] == 'attack':
                attack (order, players, map, database)
            elif order['action'] == 'move':
                move_on (order, players, map)

        # Step 6 : Second clear
        # clean(players)

        # Update cooldowns and counters
        update_counters(players, map)

        # Step 7 : Check if the game is over
        if map['player_in_citadel'][1] - 1 == map['nb_turns_to_win']:
            print('%s WON OMFG WAAAAAAAAA DUIhskfusfd sf!!!!!!!1!!' % map['player_in_citadel'][0])
            game_is_over = True
        elif map['nb_turns_without_action'] == 40:
            print('It\'s a tie !')
            game_is_over = True

        