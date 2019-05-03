import math

def get_AI_orders(players, map, database, player):
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
    specification : Martin Danhier (v.2 02/03/2019)
    implementation : Martin Danhier (v.1 01/05/2019)
    """
    actions = []
    # Get an action for each hero
    for hero in players[player]:
        hero_type = players[player][hero]['type']

        if hero_type == 'barbarian':
            actions.append(process_barbarian(players, map, database, actions, player, hero))

        elif hero_type == 'healer':
            actions.append(process_healer(players, map, database, actions,  player, hero))

        elif hero_type == 'mage':
            actions.append(process_mage(players, map, database, actions, player, hero))

        elif hero_type == 'rogue':
            actions.append(process_rogue(players, map, database, actions, player, hero))
    # Generate a command string for those actions
    return generate_command_string(actions)

def process_barbarian(players, map, database, orders, player, hero):
    """ Generates an action dictionary for the given barbarian.

    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
    orders: the orders already given to the allies (list of dict)
    player : the name of the AI player (str)
    hero : the name of the current hero. It must be a barbarian. (str)

    Returns 
    -------
    action : the order to give to the given hero (dict)

    Notes
    -----
    For the formats of 'players', 'map' and 'database', see rapport_gr_02_part_02.
    A typical "action" dict looks like this : 
        {
            'hero' : hero_name (str),
            'action' : action (str) (can be the name of an ability (as 'fulgura') or 'attack' or 'move'),
            'target' : ( x (int), y (int) ) #optional
        }

    Version
    -------
    specification: Martin Danhier (v.1 01/05/2019)
    """

    # NOTE
    # nb: check level beginning with the higher levels
    # because if there is nothing to do at a level, try to do the actions of the previous one and so on

    # If there are no creatures left OR level == 4 => return rush_citadel
    # else : voir le tableau
    return farm_creatures(players, map, database, orders, player, hero)

def process_healer(players, map, database, orders, player, hero):
    """ Generates an action dictionary for the given healer.

    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
    orders: the orders already given to the allies (list of dict)
    player : the name of the AI player (str)
    hero : the name of the current hero. It must be a healer. (str)

    Returns 
    -------
    action : the order to give to the given hero (dict)

    Notes
    -----
    For the formats of 'players', 'map' and 'database', see rapport_gr_02_part_02.
    A typical "action" dict looks like this : 
        {
            'hero' : hero_name (str),
            'action' : action (str) (can be the name of an ability (as 'fulgura') or 'attack' or 'move'),
            'target' : ( x (int), y (int) ) #optional
        }

    Version
    -------
    specification: Martin Danhier (v.1 01/05/2019)
    """
    # NOTE
    # nb: check level beginning with the higher levels
    # because if there is nothing to do at a level, try to do the actions of the previous one and so on

    # If there are no creatures left OR level == 4 => return rush_citadel
    # else : voir le tableau

    # test: move each healer in a diagonal
    return farm_creatures(players, map, database, orders, player, hero)

def process_mage(players, map, database, orders, player, hero):
    """ Generates an action dictionary for the given mage.

    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
    orders: the orders already given to the allies (list of dict)
    player : the name of the AI player (str)
    hero : the name of the current hero. It must be a mage. (str)

    Returns 
    -------
    action : the order to give to the given hero (dict)

    Notes
    -----
    For the formats of 'players', 'map' and 'database', see rapport_gr_02_part_02.
    A typical "action" dict looks like this : 
        {
            'hero' : hero_name (str),
            'action' : action (str) (can be the name of an ability (as 'fulgura') or 'attack' or 'move'),
            'target' : ( x (int), y (int) ) #optional
        }

    Version
    -------
    specification: Martin Danhier (v.1 01/05/2019)
    implementation: Jonathan Nhouyvanisvong (v.1 02/05/2019)
    """
    # NOTE
    # nb: check level beginning with the higher levels
    # because if there is nothing to do at a level, try to do the actions of the previous one and so on
    hero_lvl = players[player][hero]['level']
    if hero_lvl == '4' or len(players['creatures']) == 0:
        # If there are no creatures left OR level == 4 => return rush_citadel
        return rush_citadel

    if hero_lvl >= '3':
        # Support ally -> Check closest ally
        hero_coords = players[player][hero]['coords']
        list_target = get_closest_entity(hero_coords, players, False, 'allies') # Temp parameters
        # join closest ally

        # Target creature
        ovibus_range = database['mage'][str(players[player][hero]['level'])]['abilities'][0]['radius']
        ovibus_cooldown = players[player][hero]['cooldown'][1]

        # Check if creature -> use ovibus
        for player_checked in players:
            if player_checked == 'creatures':
                for creature in players[player_checked]:
                    distance = math.floor(get_distance(players[player][hero]['coords'], players[player_checked][creature]['coords']))
                    if distance <= ovibus_range and ovibus_cooldown == 0:
                        return {'hero': hero, 'action': 'ovibus', 'target': (x, y)}

    if hero_lvl == '2':
        fulgura_range = database['mage'][str(players[player][hero]['level'])]['abilities'][0]['radius']
        fulgura_cooldown = players[player][hero]['cooldown'][0]

        # Check if enemy -> use fulgura
        for player_checked in players:
            if player_checked != player:
                for hero_checked in players[player_checked]:
                    distance = math.floor(get_distance(players[player][hero]['coords'], players[player_checked][hero_checked]['coords']))
                    if distance <= fulgura_range and fulgura_cooldown  == 0:
                        return {'hero': hero, 'action': 'fulgura'}
                
    # else : voir le tableau
    return farm_creatures(players, map, database, orders, player, hero)

def process_rogue(players, map, database, orders, player, hero):
    """ Generates an action dictionary for the given rogue.

    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
    orders: the orders already given to the allies (list of dict)
    player : the name of the AI player (str)
    hero : the name of the current hero. It must be a rogue. (str)

    Returns 
    -------
    action : the order to give to the given hero (dict)

    Notes
    -----
    For the formats of 'players', 'map' and 'database', see rapport_gr_02_part_02.
    A typical "action" dict looks like this : 
        {
            'hero' : hero_name (str),
            'action' : action (str) (can be the name of an ability (as 'fulgura') or 'attack' or 'move'),
            'target' : ( x (int), y (int) ) #optional
        }

    Version
    -------
    specification: Martin Danhier (v.1 01/05/2019)
    implementation: Jonathan Nhouyvanisvong (v.1 02/05/2019)
    """
    # NOTE
    # nb: check level beginning with the higher levels
    # because if there is nothing to do at a level, try to do the actions of the previous one and so on
    hero_lvl = players[player][hero]['level']
    if hero_lvl == '5' or len(players['creatures']) == 0:
        # If there are no creatures left OR level == 4 => return rush_citadel
        return rush_citadel

    if hero_lvl >= '3':
        # target healer
        hero_coords = players[player][hero]['coords']
        list_target = get_closest_entity(hero_coords, players, False, 'hero_enemies') # Temp parameters

        # Join & fight closest healer_enemy if exists
        ###
        if player == 'Player 1':
            player_checked = 'Player 2'
        else:
            player_checked = 'Player 1'
        ###
        healer_exists = False
        for hero_checked in list_target:
            if players[player_checked][hero_checked]['type'] == 'healer':
                healer_founded = hero_checked
                healer_exists = True
        if not healer_exists:
            mark = get_closest_entity(hero_coords, players, True, 'hero_enemies')

        # !! Recheck
        several_enemies = False
        enemies_counter = 0
        dict_enemies = {}
        for player_checked in players:
            if player_checked != player:

                for hero_checked in players[player_checked]:
                    if get_distance(hero_coords, players[player_checked][hero_checked]['coords']) == 1:
                        dict_enemies[player_checked].append(hero_checked)
                        enemies_counter += 1
                        if enemies_counter > 1:
                            several_enemies = True

        if not several_enemies:
            # coords_target = players[]
            return {'hero': hero, 'action': 'attack', 'target': (x, y)}
        elif several_enemies:
            # Check list of target
            if hero_hp <= 4:
                if hero_checked in players['creatures']:
                    return {'hero': hero, 'action': 'attack', 'target': (x, y)}
                elif hero_checked not in players['creatures']:
                    return {'hero': hero, 'action': 'attack', 'target': (x, y)}
            else:
                # Use burst
                return {'hero': hero, 'action': 'burst', 'target': (x, y)}
                
        elif players[player][hero]['cooldown'][0] == 0 and get_distance(hero_coords, players[player_checked][healer_founded]) > 1:
            # Use reach where ?
            return {'hero': hero, 'action': 'reach', 'target': (x, y)}

    return farm_creatures(players, map, database, orders, player, hero)

    # If there are no creatures left OR level == 4 => return rush_citadel
    # else : voir le tableau
    return farm_creatures(players, map, database, orders, player, hero)


def farm_creatures(players, map, database, orders, player, hero):
    """ Hunt creatures to earn victory points.
    
    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
    orders: the orders already given to the allies (list of dict)
    player : the name of the AI player (str)
    hero : the name of the current hero. It must be a rogue. (str)

    Returns
    -------
    action : the order to give to the given hero (dict)
    
    Notes
    -----
    For the formats of 'players', 'map' and 'database', see rapport_gr_02_part_02.
    A typical "action" dict looks like this : 
        {
            'hero' : hero_name (str),
            'action' : action (str) (can be the name of an ability (as 'fulgura') or 'attack' or 'move'),
            'target' : ( x (int), y (int) ) #optional
        }

    Version
    -------
    specification: Martin Danhier (v.1 01/05/2019)
    """
    # NOTE (supprimer après implémentation):
    # Lvl 1 dans le tableau.
    # ! si un héro d'un lvl > 1 n'arrive pas à faire ses capacités spéciales, il reviendra à cette fonction
    # cette fonction doit toujours générer une action valide pour éviter qu'un héro soit bloqué à jamais
    # Commun à toutes les classes de héros, d'où une fonction séparée
    
    # SI un joueur adverse approche trop de la citadelle : se déplacer vers lui et l’attaquer.
    # SINON : Rechercher des créatures pour gagner des points de victoire et des niveaux.

    if False:
        return {}
        # changer la condition
        # si un joueur approche un peu trop de la citadelle il vaut se déplacer vers lui et s'il est à portée, l'attaquer
    else:
        target = get_closest_entity(players[player][hero]['coords'], players, True, 'creatures')[0]
        # get target coords
        target_coords = players[target[0]][target[1]]['coords']
        
        order = find_path(players, map, players[player][hero]['coords'], target_coords)
        order['hero'] = hero
        return order
        # if the citadel is safe, target creatures
        # -> aller vers la créature la plus proche
        # -> si créature est à portée, l'attaquer



    return {}

def rush_citadel(players, map, database, orders, player, hero):
    """ Try to conquer and defend the citadel.

    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
    orders: the orders already given to the allies (list of dict)
    player : the name of the AI player (str)
    hero : the name of the current hero. It must be a rogue. (str)

    Returns
    -------
    action : the order to give to the given hero (dict)
    
    Notes
    -----
    For the formats of 'players', 'map' and 'database', see rapport_gr_02_part_02.
    A typical "action" dict looks like this : 
        {
            'hero' : hero_name (str),
            'action' : action (str) (can be the name of an ability (as 'fulgura') or 'attack' or 'move'),
            'target' : ( x (int), y (int) ) #optional
        }

    Version
    -------
    specification: Martin Danhier (v.1 01/05/2019)
    """

    # ! il faut faire gaffe qu'un héros ait toujours quelque chose à faire et ne soit pas bloqué à jamais

    # Tous les alliés vers la citadelle
    # PARMI les alliés sur la citadelle :
    #   SI pv_allié <= seuil_critique : Changer avec un autre héros 3 (pour éviter la
    #   réinitialisation de la possession de la citadelle)
    # SI ennemis à proximité de la citadelle :
    #   Le héros allié sur la citadelle y reste.
    #   Les autres héros attaquent les ennemis proche (priorité attaque de groupe)
    # SINON : Healer reste sur la citadelle
    # SI la citadelle est inoccupée ET nombre_tours_sans_perte_pv <=
    # seuil_inactivité_critique :
    #   Chercher un ennemi à attaquer (Pour éviter un match nul)
    return {}

# === TOOLS ===
# Useful functions
def find_path(players, map, source, target):
    """
    """
    order = {}
    distance = math.floor(get_distance(source, target))
    # If the source is next to the target
    if distance == 1:
        # The source attacks the target
        order['action'] = 'attack'
        order['target'] = target
    else:
        # The source moves towards the target
        order['action'] = 'move'

        # The source can move on 9 tiles
        first_loop = True

        # Get the smallest distance
        for x_coord in range(source[0] - 1, source[0] + 2):
            for y_coord in range(source[1] - 1, source[1] + 2):

                # Get the distance between the checked tile and the hero
                distance_hero_tile = get_distance(
                    (x_coord, y_coord), target)

                if first_loop:
                    min_distance = distance_hero_tile
                    first_loop = False

                else:
                    if distance_hero_tile < min_distance:
                        min_distance = distance_hero_tile

        # Get the first coordinates that are at the smallest distance from the closest hero
        for x_coord in range(source[0] - 1, source[0] + 2):
            for y_coord in range(source[1] - 1, source[1] + 2):
                if get_distance((x_coord, y_coord), target) == min_distance:
                    # The creature moves on to this tile
                    order['target'] = (x_coord, y_coord)
    return order


def get_tile_info(coords, players, map, orders):
    """ Get the details of the given tile.

    Parameters
    ----------
    coords: the coordinates of a tile. (tuple)
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    orders: the orders already given to the allies (list of dict)

    Returns
    -------
    info : the details of the tile (str).

    Notes
    -----
    info can take the following values:
        'wall' if the tile doesn't exist.
        'player' if the tile contains a hero or a creature.
        'spur' if the tile is in the spur.
        'clear' if the tile is clear.# If there is no hero in the radius, get the closest # If there is no hero in the radius, get the closest heroes# If there is no hero in the radius, get the closest heroesheroes
    For the formats of players and map, see rapport_gr_02_part_02.
    A typical 'coord' tuple is in the format ( row (int), column (int) ).

    Version
    -------
    specification: Martin Danhier (v.3 02/05/2019)
    implementation: Martin Danhier (v.3 02/05/2019)
    """
    # If the coordinates are out of the map or if the coordinates are part of the spur while it is still locked.
    if coords[0] <= 0 or coords[0] > map['size'][0] or coords[1] <= 0 or coords[1] > map['size'][1] or (coords in map['spur'] and map['nb_turns'] <= 20):
        return 'wall'
    else:      
        # For each hero / creature, check if its coords are equal to tested ones.
        for player in players:
            for individual in players[player]:
                if players[player][individual]['coords'] == coords:
                    return 'player'
        # Return player if an ally is planning to move to the chosen tile
        for order in orders:
            if order != {}:
                if order['action'] == 'move' and order['target'] == coords:
                    return 'player'
        # If this code is reached, then there is no player on this tile
        if coords in map['spur']:
            return 'spur'
        else:
            return 'clear'

def generate_command_string(actions):
    """ Converts a list of actions to a command string.

    Parameters
    ----------
    actions: a list of actions (list of dict)

    Returns
    -------
    command: a command string readable by the game (str)

    Notes
    -----
    The format of the "command" string is destribed in the instructions, p14.
    A typical "action" dict looks like this : 
        {
            'hero' : hero_name (str),
            'action' : action (str) (can be the name of an ability (as 'fulgura') or 'attack' or 'move'),
            'target' : ( x (int), y (int) ) #optional
        }

    Version
    -------
    specification: Martin Danhier (v.1 01/05/2019)
    """
    command = ''
    # For each action dictionary
    for action in actions:
        # Converts the action to a string and append it to command
        if action != {}:
            if action['action'] == 'move':
                command += '%s:@%d-%d' % (action['hero'], action['target'][0], action['target'][1])
            elif action['action'] == 'attack':
                command += '%s:*%d-%d' % (action['hero'], action['target'][0], action['target'][1])
            else:
                command += '%s:%s' % (action['hero'], action['action'])
                if 'target' in action:
                    command+= ':%d-%d' % (action['target'][0], action['target'][1])
            command += ' '
    return command

def get_closest_entity(coords, players, restrictive, mode):
    """ Returns the closest entiti(es) around the given tile.

    Parameters:
    ----------
    coords : the coordinates of a tile (tuple).
    players : data of player heroes and creatures (dict)
    restrictive : if True, the function will only return one hero (the closest one with several conditions to remove the ambiguity).
                      else, the function will return the list of the closest heroes (bool).
    mode : the target mode of the function. (str)

    Returns:
    -------
    closest_heroes : a list containing the closest heroes, which are in of format (player (str), hero (str)) (list)

    Notes
    -----
    For the format of 'players', see 'rapport_gr_02_part_2'.
    A typical 'coord' tuple is in the format ( row (int), column (int) ).
    The possible modes are the following:
        - 'creatures': only target creatures
        - 'heroes': only target heroes
        - 'any': target any entity

    Version:
    -------
    specification : Guillaume Nizet, Martin Danhier (v.2 02/05/19)
    implementation : Guillaume Nizet, Jonathan Nhouyvanisvong, Martin Danhier (v.3 02/05/19)
    """
    # Initialize the data
    closest_heroes = []
    temp_closest_heroes = []
    step = 0

    while closest_heroes == [] or len(closest_heroes) > 1:
        min = -1
        if step != 0 and step <= 4:
            temp_closest_heroes = closest_heroes
        # For each hero
        for player in players:
            # Apply mode filters
            if (player != 'creatures' and mode == 'heroes') or (player == 'creatures' and mode == 'creatures') or (mode == 'any'):
                for hero in players[player]:
                    if (player, hero) in temp_closest_heroes or step == 0:
                        # Step 0 : Check the distance to get the closest heroes
                        if step == 0:
                            checked_value = math.floor(get_distance(
                                players[player][hero]['coords'], coords))
                        # Step 1 : If the checked hero is one of the several closest heroes with the same distance
                        elif step == 1:
                            checked_value = players[player][hero]['hp']

                        # Step 2 : If the checked hero is one of the several closest heroes with the same HP
                        elif step == 2:
                            checked_value = players[player][hero]['xp']

                        # Step 3 : If the checked hero is one of the several closest heroes with the same HP and victory points
                        elif step == 3:
                            checked_value = hero.lower()

                        # Step 4 : If the checked hero is one of the several closest heroes with the same HP, victory points and name
                        else:
                            checked_value = player.lower()

                        # First checked hero : initialisation
                        if min == -1:
                            closest_heroes = [(player, hero)]
                            min = checked_value

                        # If the checked value is smaller than the current min
                        elif checked_value < min:
                            # Reset the closest heroes and save the current one
                            closest_heroes = [(player, hero)]
                            min = checked_value

                        # If the checked value is equal to the current min
                        elif checked_value == min:
                            # save this hero as well
                            closest_heroes.append((player, hero))

        # Only return the list of the closest heroes (there might be more than one hero)
        if not restrictive:
            return closest_heroes
        step += 1

    # restrictive == True: The single closest hero has been found
    return closest_heroes

def get_distance(coords1, coords2):
    """ Get the distance between two coordinates.

    Parameters
    ----------
    coords1: the first pair of coordinates. (tuple)math.ceil
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