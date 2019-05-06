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

         
    if players[player][hero]['level'] >= '3':
        allies_in_range_energise = 0
        enemies_in_range_energise = 0
        enemies_in_range_stun = 0

        energise_range = database['barbarian'][str(players[player][hero]['level'])]['abilities'][0]['radius']
        stun_range = database['barbarian'][str(players[player][hero]['level'])]['abilities'][1]['radius']

        for checked_player in players:
            for checked_hero in players[checked_player]:                
                if math.floor(get_distance(players[player][hero]['coords'], players[checked_player][checked_hero]['coords'])) <= energise_range:

                    # Check the allies
                    if checked_player == player: 
                        allies_in_range_energise += 1

                    # Check the enemies (enemy players + creatures)
                    else:
                        enemies_in_range_energise += 1

                if math.floor(get_distance(players[player][hero]['coords'], players[checked_player][checked_hero]['coords'])) <= stun_range:

                    # Only check the enemies (enemy players + creatures)
                    if checked_player != player:
                        enemies_in_range_stun += 1

        # Prevent the barbarian from counting itself in the allies in range
        allies_in_range_energise -= 1

        # If there are heroes in range of energise, then they automatically are in range of stun because the radius of stun is smaller
        if allies_in_range_energise > 0 and enemies_in_range_energise > 0 and players[player][hero]['cooldown'][0] == 0 and players[player][hero]['cooldown'][1] == 0:
            if allies_in_range_energise >= enemies_in_range_stun:

                # Use energise
                return { 'hero' : hero, 'action' : 'energise' }

            else:

                # Use stun
                return { 'hero' : hero, 'action' : 'stun' }


    if players[player][hero]['level'] >= '2':
        allies_in_range = 0
        enemies_in_range = 0

        energise_range = database['barbarian'][str(players[player][hero]['level'])]['abilities'][0]['radius']

        for checked_player in players:
            for checked_hero in players[checked_player]:                
                if math.floor(get_distance(players[player][hero]['coords'], players[checked_player][checked_hero]['coords'])) <= energise_range:

                    # Check the allies
                    if checked_player == player: 
                        allies_in_range += 1

                    # Check the enemies (enemy players + creatures)
                    else:
                        enemies_in_range += 1

        # Prevent the barbarian from counting itself in the allies in range
        allies_in_range -= 1

        if allies_in_range > 0 and enemies_in_range > 0 and players[player][hero]['cooldown'][0] == 0:

            # Use energise 
            return { 'hero' : hero, 'action' : 'energise' }

    if players[player][hero]['level'] == '5' or len(players['creatures']) == 0:
        return rush_citadel(players, map, database, orders, player, hero)
    else:
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


    # Define a 'danger amount' for every hero except for the healer that represents how much they are in danger
    # Danger amount = max_hp/hp + nb_enemies_in_radius/2
    # Where radius = 3 + 1/3(distance_from_healer)
    # The healer will go towards a hero to heal/immunise him if his danger amount exceeds 2

    # The data will be stored in a list of the type [(coords, hp, danger_amount)]

    data_allies = []
    danger_amounts = []

    for checked_player in players:
        for checked_hero in players[checked_player]:

            # Check the allies 
            if checked_player == player:

                # Don't check the healer
                if checked_hero != hero:

                    hp = players[checked_player][checked_hero]['hp']
                    coords = players[checked_player][checked_hero]['coords']
                    max_hp = database[players[checked_player][checked_hero]['type']][players[checked_player][checked_hero]['level']]['hp']
                    radius = math.floor(3 + 1/3 * get_distance(players[player][hero]['coords'], coords))
                    nb_enemies_in_radius = 0
                    
                    # Get the number of enemy heroes in the radius

                    for checked_player_2 in players:
                        for checked_hero_2 in players[checked_player_2]:

                            # Check the enemies

                            if checked_player_2 != player:
                                if math.floor(get_distance(coords, players[checked_player_2][checked_hero_2]['coords'])) <= radius:
                                    nb_enemies_in_radius += 1

                    data_allies.append((coords, hp, max_hp, max_hp/hp + nb_enemies_in_radius/2))
                    danger_amounts.append(max_hp/hp + nb_enemies_in_radius/2)

    if players[player][hero]['level'] >= '3':
        pass
        


    if players[player][hero]['level'] >= '2':

        # If an ally is in danger
        if max(danger_amounts) >= 2:

            for ally in data_allies:
                if ally[3] == max(danger_amounts):

                    # If he is in the radius of 'invigorate' 
                    if math.floor(get_distance(ally[0], players[player][hero]['coords'])) <= database['healer'][players[player][hero]['level']]['abilities'][0]['radius']:
                        
                        # If he needs to be healed
                        if ally[1] < ally[2] and players[player][hero]['cooldown'][0] == 0:

                            # Use invigorate
                            return { 'hero' : hero, 'action' : 'invigorate' }

                    else:

                        # Go towards him
                        order = find_path(players, map, orders, players[player][hero]['coords'], ally[0], False)
                        order['hero'] = hero
                        return order
                    
    
    if players[player][hero]['level'] == '5' or len(players['creatures']) == 0:
        return rush_citadel(players, map, database, orders, player, hero)
    else:
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

    if hero_lvl >= '3':
        # Support ally -> Check closest ally
        hero_coords = players[player][hero]['coords']
        # list_target = get_closest_entity(hero_coords, players, player, False, 'allies')
        # join closest ally

        # Target creature
        ovibus_range = database['mage'][str(players[player][hero]['level'])]['abilities'][0]['radius']
        ovibus_cooldown = players[player][hero]['cooldown'][1]

        # Check if creature -> use ovibus
        for player_checked in players:
            if player_checked == 'creatures':
                for creature in players[player_checked]:
                    coords_creature = players[player_checked][creature]['coords']
                    distance = math.floor(get_distance(players[player][hero]['coords'], coords_creature))
                    if distance <= ovibus_range and ovibus_cooldown == 0:
                        x = coords_creature[0]
                        y = coords_creature[1]
                        return {'hero': hero, 'action': 'ovibus', 'target': (x, y)}

    if hero_lvl >= '2':
        fulgura_range = database['mage'][str(players[player][hero]['level'])]['abilities'][0]['radius']
        fulgura_cooldown = players[player][hero]['cooldown'][0]

        # Check if enemy -> use fulgura
        for player_checked in players:
            if player_checked != player:
                for hero_checked in players[player_checked]:
                    distance = math.floor(get_distance(players[player][hero]['coords'], players[player_checked][hero_checked]['coords']))
                    if distance <= fulgura_range and fulgura_cooldown  == 0:
                        return {'hero': hero, 'action': 'fulgura', 'target': players[player_checked][hero_checked]['coords']}
                
    if hero_lvl >= '5' or len(players['creatures']) == 0:
        return rush_citadel(players, map, database, orders, player, hero)
    else:
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

    if hero_lvl >= '3':
        
        hero_coords = players[player][hero]['coords']
        closest_enemies = get_closest_entity(hero_coords, players, player, False, 'all_enemies')
        distance_min_enemies = math.floor(get_distance(players[closest_enemies[0][0]][closest_enemies[0][1]]['coords'], hero_coords))

        if distance_min_enemies == 1:
            if len(closest_enemies) == 1:
                # (player, hero)
                coords_enemy = players[closest_enemies[0][0]][closest_enemies[0][1]]['coords']
                x = coords_enemy[0]
                y = coords_enemy[1]
                return {'hero': hero, 'action': 'attack', 'target': (x, y)}
            else:

                # more than one enemy
                low_hp_creatures = []
                low_hp_enemies = []
                low_hp_healers = []

                for enemy in closest_enemies:
                    if players[enemy[0]][enemy[1]]['hp'] <= 4:
                        if enemy[0] == 'creatures':
                            low_hp_creatures.append(enemy)
                        elif players[enemy[0]][enemy[1]]['type'] == 'healer':
                            low_hp_healers.append(enemy)
                        else:
                            low_hp_enemies.append(enemy)
                
                if len(low_hp_creatures) != 0 or len(low_hp_healers) != 0 or len(low_hp_enemies) != 0:
                    if len(low_hp_creatures) > 0:
                        target = low_hp_creatures[0]
                        # (player, hero)
                    elif len(low_hp_healers) > 0:
                        target = low_hp_healers[0]
                    elif len(low_hp_enemies) > 0:
                        target = low_hp_enemies[0]

                    x = players[target[0]][target[1]]['coords'][0]
                    y = players[target[0]][target[1]]['coords'][1]
                    return {'hero': hero, 'action': 'attack', 'target': (x, y)}
                else:
                    if players[player][hero]['cooldown'][1] == 0:
                        return {'hero': hero, 'action': 'burst'}
    

        # index = 0
        # healer_exists = False
        # while index < len(list_target) and not healer_exists:
        #     checked_hero = players[list_target[index][0]][list_target[index][1]]
        #     if checked_hero['type'] == 'healer':
        #         target = checked_hero
        #         healer_exists = True
        #     index += 1

        # if not healer_exists:
        #     target = get_closest_entity(hero_coords, players, True, 'enemy_heroes')

        # !! Recheck
        # several_enemies = False
        # enemies_counter = 0
        # dict_enemies = {}
        # for player_checked in players:
        #     if player_checked != player:
        #         for hero_checked in players[player_checked]:
        #             if get_distance(hero_coords, players[player_checked][hero_checked]['coords']) == 1:
        #                 dict_enemies[player_checked].append(hero_checked)
        #                 enemies_counter += 1
        #                 if enemies_counter > 1:
        #                     several_enemies = True 

        # if not several_enemies:
        #     # coords_target = players[]
        #     return {'hero': hero, 'action': 'attack', 'target': (x, y)}
        # elif several_enemies:
        #     # Check list of target
        #     if hero_hp <= 4:
        #         if hero_checked in players['creatures']:
        #             return {'hero': hero, 'action': 'attack', 'target': (x, y)}
        #         elif hero_checked not in players['creatures']:
        #             return {'hero': hero, 'action': 'attack', 'target': (x, y)}
        #     else:
        #         # Use burst
        #         return {'hero': hero, 'action': 'burst'}
                
        # elif players[player][hero]['cooldown'][0] == 0 and get_distance(hero_coords, players[player_checked][healer_founded]) > 1:
        #     # Use reach where ?
        #     return {'hero': hero, 'action': 'reach', 'target': (x, y)}
        

    # If there are no creatures left OR level == 4 => return rush_citadel
    # else : voir le tableau

    
    if hero_lvl >= '5' or len(players['creatures']) == 0:
        return rush_citadel(players, map, database, orders, player, hero)
    else:
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
    too_close = False
    # Check if a hero is to close to the citadel
    for tile in map['spur']:
        # For each hero
        for checked_player in players:
            if checked_player != 'creatures':
                for checked_hero in players[checked_player]:
                    # If the enemy is too close to the citadel
                    if get_distance(players[checked_player][checked_hero]['coords'], tile) < 5:
                        too_close = True
    if too_close:
        return rush_citadel(players, map, database, orders, player, hero)
    # Else, target creatures
    else:
        target = get_closest_entity(players[player][hero]['coords'], players, player, True, 'creatures')[0]
        
        # Get target coords and order
        target_coords = players[target[0]][target[1]]['coords']
        
        # Can reach be done ?
        if players[player][hero]['type'] == 'rogue' and int(players[player][hero]['level']) >= 3 and players[player][hero]['cooldown'][0] == 0:
            order = find_path(players, map, orders, players[player][hero]['coords'], target_coords, True, database['rogue'][players[player][hero]['level']]['abilities'][0]['radius'])
        else:
            order = find_path(players, map, orders, players[player][hero]['coords'], target_coords)
        order['hero'] = hero
        return order

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

    if players[player][hero]['coords'] not in map['spur']:
        # The hero is not on the spur

        # Get the spur tiles sorted by distance
        first_iteration = True
        spur_sorted = []
        for tile in map['spur']:
            dist = get_distance(tile, players[player][hero]['coords'])
            if first_iteration:
                    spur_sorted.append((tile, dist))
                    first_iteration = False
            else:
                sorted = False
                index = 0
                while index < len(spur_sorted) and not sorted:
                    
                    if dist < spur_sorted[index][1]:
                        spur_sorted = spur_sorted[:index] + [(tile, dist)] + spur_sorted[index:]
                        sorted = True
                    elif index == len(spur_sorted) - 1:
                        spur_sorted.append((tile, dist))
                        sorted = True
                    index += 1

        index = 0
        order_generated = False
        
        while index < len(spur_sorted) and not order_generated:
            nearest_tile = spur_sorted[index][0]
            # Get the info of that tile
            info = get_tile_info(nearest_tile, players, map, orders)
            if info == 'player':
                # Check if the hero on the tile is an ally player or not
                ally_on_nearest_tile = False
                for checked_hero in players[player]:
                    if players[player][checked_hero]['coords'] == nearest_tile:
                        ally_on_nearest_tile = True
                
                if not ally_on_nearest_tile:
                    # if it is an ennemy

                    # check if there is a clear tile on the spur to cancel the enemy victory counter
                    spur_is_full = True
                    for spur_tile in map['spur']:
                        if get_tile_info(spur_tile, players, map, orders) == 'spur':
                            spur_is_full = False
                    if spur_is_full:
                        # If the spur is full, attack the enemy

                        # Can reach be done ?
                        if players[player][hero]['type'] == 'rogue' and int(players[player][hero]['level']) >= 3 and players[player][hero]['cooldown'][0] == 0:
                            order = find_path(players, map, orders, players[player][hero]['coords'], nearest_tile, True, database['rogue'][players[player][hero]['level']]['abilities'][0]['radius'])
                        else:
                            order = find_path(players, map, orders, players[player][hero]['coords'], nearest_tile, True)
                        order_generated = True
            else:
                # Can reach be done ?
                if players[player][hero]['type'] == 'rogue' and int(players[player][hero]['level']) >= 3 and players[player][hero]['cooldown'][0] == 0:
                    order = find_path(players, map, orders, players[player][hero]['coords'], nearest_tile, False, database['rogue'][players[player][hero]['level']]['abilities'][0]['radius'])
                else:
                    order = find_path(players, map, orders, players[player][hero]['coords'], nearest_tile, False)
                order_generated = True
            index += 1
            
        order['hero'] = hero
        return order
    else:
        # The hero is on the spur

        # Target the closest enemy
        target = get_closest_entity(players[player][hero]['coords'], players,player, True, 'enemy_heroes')[0]
        target_coords = players[target[0]][target[1]]['coords']
    
        # Can reach be done ?
        if players[player][hero]['type'] == 'rogue' and int(players[player][hero]['level']) >= 3 and players[player][hero]['cooldown'][0] == 0:
            order = find_path(players, map, orders, players[player][hero]['coords'], target_coords, True, database['rogue'][players[player][hero]['level']]['abilities'][0]['radius'])
        else:
            order = find_path(players, map, orders, players[player][hero]['coords'], target_coords, True)
        order['hero'] = hero
        if (order['action'] == 'move' and order['target'] in map['spur']) or order['action'] == 'attack':
            # if the hero should move on another spur tile, or if the hero should attack, let it do it
            return order
        else:
            # if the hero should move outside of the spur, do not let it do it (move on the same tile)
            return {'hero':hero, 'action':'move', 'target': players[player][hero]['coords']}
    

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
def find_path(players, map, orders, source, target, attack_target = True, walkable_distance = 1):
    """
    orders: the orders already given to the allies (list of dict)
    attack_target: if True, attack the target tile when it is in range. if False, move to that target tile. (bool, default True)
    walkable_distance: the maximal distance that the hero can move in a single turn (int, default 1)

    Notes
    -----
    If walkable_distance > 1, the hero must be a rogue and its reach cooldown must be equal to 0.
    """
    order = {}
    distance = math.floor(get_distance(source, target))
    # If the source is next to the target
    if distance == 1 and attack_target:
        # The source attacks the target
        order['action'] = 'attack'
        order['target'] = target
    else:
        
        # The source moves towards the target

        # The source can move on more on less tiles depending on the walkable distance
        first_loop = True

        # Get the distances sorted by insertion sort
        distances = []
        for x_coord in range(source[0] - walkable_distance, source[0] + walkable_distance + 1):
            for y_coord in range(source[1] - walkable_distance, source[1] + walkable_distance + 1):
                if (x_coord, y_coord) != source:
                    # Get the distance between the checked tile and the target
                    tile_distance = get_distance((x_coord, y_coord), target)
                    source_distance = math.floor(get_distance((x_coord, y_coord), source))
                    if source_distance <= walkable_distance:
                        if first_loop:
                            distances.append(((x_coord, y_coord), tile_distance))
                            first_loop = False
                        else:
                            index = 0
                            sorted = False
                            while not sorted and index < len(distances):
                                if tile_distance <= distances[index][1]:
                                    distances =  distances[:index] + [((x_coord, y_coord), tile_distance)] + distances[index:]
                                    sorted = True
                                elif index == len(distances) - 1:
                                    distances.append(((x_coord, y_coord), tile_distance))
                                    sorted = True
                                else:
                                    index += 1

        # Go to the clear tile nearest to the target
        found = False
        index = 0
        while not found and index < len(distances):
            info = get_tile_info(distances[index][0], players, map, orders)

            if info == 'clear' or (info == 'spur' and map['nb_turns'] > 20):
                order['target'] = distances[index][0]
                found = True
            elif index == len(distances):
                return {}
            else:
                index += 1

        distance_from_source = math.floor(get_distance(order['target'], source))
        if distance_from_source <= 1:
            order['action'] = 'move'
        else:
            order['action'] = 'reach'
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
    counter = 0
    for action in actions:
        counter += 1
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
            if counter < len(actions):
                command += ' '
    return command

def get_closest_entity(coords, players, player, restrictive, mode):
    """ Returns the closest entiti(es) around the given tile.

    Parameters:
    ----------
    coords : the coordinates of a tile (tuple).
    players : data of player heroes and creatures (dict)
    player : the AI player (str)
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
        - 'enemy_heroes': only target enemy heroes
        - 'all_enemies' : only target enmy heroes and creatures
        - 'allies' : only target ally heroes

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
        for checked_player in players:
            # Apply mode filters
            if (checked_player == 'creatures' and mode == 'creatures') or (checked_player not in ('creatures', player) and mode == 'enemy_heroes') or (checked_player != player and mode == 'all_enemies') or (checked_player == player and mode == 'allies'):
                for hero in players[checked_player]:
                    if (checked_player, hero) in temp_closest_heroes or step == 0:
                        # Step 0 : Check the distance to get the closest heroes
                        if step == 0:
                            checked_value = math.floor(get_distance(
                                players[checked_player][hero]['coords'], coords))
                        # Step 1 : If the checked hero is one of the several closest heroes with the same distance
                        elif step == 1:
                            checked_value = players[checked_player][hero]['hp']

                        # Step 2 : If the checked hero is one of the several closest heroes with the same HP
                        elif step == 2:
                            checked_value = players[checked_player][hero]['xp']

                        # Step 3 : If the checked hero is one of the several closest heroes with the same HP and victory points
                        elif step == 3:
                            checked_value = hero.lower()

                        # Step 4 : If the checked hero is one of the several closest heroes with the same HP, victory points and name
                        else:
                            checked_value = checked_player.lower()

                        # First checked hero : initialisation
                        if min == -1:
                            closest_heroes = [(checked_player, hero)]
                            min = checked_value

                        # If the checked value is smaller than the current min
                        elif checked_value < min:
                            # Reset the closest heroes and save the current one
                            closest_heroes = [(checked_player, hero)]
                            min = checked_value

                        # If the checked value is equal to the current min
                        elif checked_value == min:
                            # save this hero as well
                            closest_heroes.append((checked_player, hero))

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