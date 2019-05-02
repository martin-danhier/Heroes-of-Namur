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
            actions.append(process_barbarian(players, map, database, player, hero))

        elif hero_type == 'healer':
            actions.append(process_healer(players, map, database, player, hero))

        elif hero_type == 'mage':
            actions.append(process_mage(players, map, database, player, hero))

        elif hero_type == 'rogue':
            actions.append(process_rogue(players, map, database, player, hero))
    # Generate a command string for those actions
    return generate_command_string(actions)

def process_barbarian(players, map, database, player, hero):
    """ Generates an action dictionary for the given barbarian.

    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
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
    return farm_creatures(players, map, database, player, hero)

def process_healer(players, map, database, player, hero):
    """ Generates an action dictionary for the given healer.

    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
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
    return farm_creatures(players, map, database, player, hero)

def process_mage(players, map, database, player, hero):
    """ Generates an action dictionary for the given mage.

    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
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
    """
    # NOTE
    # nb: check level beginning with the higher levels
    # because if there is nothing to do at a level, try to do the actions of the previous one and so on

    # If there are no creatures left OR level == 4 => return rush_citadel
    # else : voir le tableau
    return farm_creatures(players, map, database, player, hero)

def process_rogue(players, map, database, player, hero):
    """ Generates an action dictionary for the given rogue.

    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
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
    # NOTE
    # nb: check level beginning with the higher levels
    # because if there is nothing to do at a level, try to do the actions of the previous one and so on

    # If there are no creatures left OR level == 4 => return rush_citadel
    # else : voir le tableau
    return farm_creatures(players, map, database, player, hero)


def farm_creatures(players, map, database, player, hero):
    """ Hunt creatures to earn victory points.
    
    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
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

    



    return {}

def rush_citadel(players, map, database, player, hero):
    """ Try to conquer and defend the citadel.

    Parameters
    ----------
    players : data of player heroes and creatures (dict)
    map: data of the map (spawns, spur, size, etc...) (dict)
    database : data of hero classes (dict)
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
        'spur' if the tile is in the spur.
        'clear' if the tile is clear.# If there is no hero in the radius, get the closest # If there is no hero in the radius, get the closest heroes# If there is no hero in the radius, get the closest heroesheroes
    For the formats of players and map, see rapport_gr_02_part_02.
    A typical 'coord' tuple is in the format ( row (int), column (int) ).

    Version
    -------
    specification: Martin Danhier (v.2 16/03/2019)
    implementation: Martin Danhier (v.2 09/04/2019)
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