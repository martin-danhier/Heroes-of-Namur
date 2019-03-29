from heroes_namur_gr_02 import *
main('test.hon', (True, True))

# database = {
#     'barbarian': {
#         '1': {'victory_pts': 0, 'hp': 10, 'dmg': 2, 'abilities':[]},
#         '2': {'victory_pts': 100, 'hp': 13, 'dmg': 3, 'abilities': [{'name': 'energise', 'radius': 1, 'x': 1, 'cd': 1}]},
#         '3': {'victory_pts': 200, 'hp': 16, 'dmg': 4, 'abilities': [{'name': 'energise', 'radius': 2, 'x': 1, 'cd': 1}, {'name': 'stun', 'radius': 1, 'x': 1, 'cd': 1}]},
#         '4': {'victory_pts': 400, 'hp': 19, 'dmg': 5, 'abilities': [{'name': 'energise', 'radius': 3, 'x': 2, 'cd': 1}, {'name': 'stun', 'radius': 2, 'x': 2, 'cd': 1}]},
#         '5': {'victory_pts': 800, 'hp': 22, 'dmg': 6, 'abilities': [{'name': 'energise', 'radius': 4, 'x': 2, 'cd': 1}, {'name': 'stun', 'radius': 3, 'x': 3, 'cd': 1}]}
#     },
#     'healer': {
#         '1': {'victory_pts': 0, 'hp': 10, 'dmg': 2, 'abilities':[]},
#         '2': {'victory_pts': 100, 'hp': 11, 'dmg': 2, 'abilities': [{'name': 'invigorate', 'radius': 1, 'x': 1, 'cd': 1}]},
#         '3': {'victory_pts': 200, 'hp': 12, 'dmg': 3, 'abilities': [{'name': 'invigorate', 'radius': 2, 'x': 2, 'cd': 1}, {'name': 'immunise', 'radius': 1, 'cd': 3}]},
#         '4': {'victory_pts': 400, 'hp': 13, 'dmg': 3, 'abilities': [{'name': 'invigorate', 'radius': 3, 'x': 3, 'cd': 1}, {'name': 'immunise', 'radius': 2, 'cd': 3}]},
#         '5': {'victory_pts': 800, 'hp': 14, 'dmg': 4, 'abilities': [{'name': 'invigorate', 'radius': 4, 'x': 4, 'cd': 1}, {'name': 'immunise', 'radius': 3, 'cd': 3}]}
#     },
#     'mage': {
#         '1': {'victory_pts': 0, 'hp': 10, 'dmg': 2, 'abilities':[]},
#         '2': {'victory_pts': 100, 'hp': 12, 'dmg': 3, 'abilities': [{'name': 'fulgura', 'radius': 1, 'x': 3, 'cd': 1}]},
#         '3': {'victory_pts': 200, 'hp': 14, 'dmg': 4, 'abilities': [{'name': 'fulgura', 'radius': 2, 'x': 3, 'cd': 1}, {'name': 'ovibus', 'radius': 1, 'x': 1, 'cd': 3}]},
#         '4': {'victory_pts': 400, 'hp': 16, 'dmg': 5, 'abilities': [{'name': 'fulgura', 'radius': 3, 'x': 4, 'cd': 1}, {'name': 'ovibus', 'radius': 2, 'x': 2, 'cd': 3}]},
#         '5': {'victory_pts': 800, 'hp': 18, 'dmg': 6, 'abilities': [{'name': 'fulgura', 'radius': 4, 'x': 4, 'cd': 1}, {'name': 'ovibus', 'radius': 3, 'x': 2, 'cd': 3}]}
#     },
#     'rogue': {
#         '1': {'victory_pts': 0, 'hp': 10, 'dmg': 2, 'abilities':[]},
#         '2': {'victory_pts': 100, 'hp': 12, 'dmg': 3, 'abilities': [{'name': 'reach', 'radius': 1, 'cd': 1}]},
#         '3': {'victory_pts': 200, 'hp': 14, 'dmg': 4, 'abilities': [{'name': 'reach', 'radius': 2, 'cd': 1}, {'name': 'burst', 'radius': 1, 'x': 1, 'cd': 1}]},
#         '4': {'victory_pts': 400, 'hp': 16, 'dmg': 5, 'abilities': [{'name': 'reach', 'radius': 3, 'cd': 1}, {'name': 'burst', 'radius': 2, 'x': 2, 'cd': 1}]},
#         '5': {'victory_pts': 800, 'hp': 18, 'dmg': 6, 'abilities': [{'name': 'reach', 'radius': 4, 'cd': 1}, {'name': 'burst', 'radius': 3, 'x': 3, 'cd': 1}]}
#     }
# }


# players, map = read_file('test.hon')
# create_character(players, map, 'a:mage b:barbarian c:healer d:rogue', 'Player 1')
# create_character(players, map, 'c:mage d:barbarian e:healer a:rogue', 'Player 2')
# players['Player 1']['b']['level'] = '3'
# players['Player 1']['b']['cooldown'] = [0, 0]
# players['Player 1']['b']['active_effects'] = {'energise' : (2, 3), 'immunise' : (1, 1), 'stun' : (1, 1), 'ovibus': (2, 1)}
# players['creatures']['bear']['active_effects']['stun'] = (2, 1)
# map['player_colors'] = {'Player 1' : 'green', 'Player 2' : 'red' }

# print(create_stats(players, map, database))


# # import colored
# # test = colored.stylize('bonjour', colored.fg('light_goldenrod_1')) + ' et voila c\'est ' + colored.stylize('rouge',colored.fg('light_red')) + ' !!'
# # print (test)
# # print('longueur normale : %d' % len('bonjour et voila c\'est rouge !!'))
# # print('longueur détectée : %d' % len(test))

# # player_colors = {'Player 1' : 'green', 'Player 2' : 'red'}
# # colors = ['light_goldenrod_1', 'light_magenta'] + ['light_' + player_colors[player] for player in player_colors]
# # color_codes_length = 0
# # for color in colors:
# #     color_codes_length += len(colored.fg(color)) * (len(test.split(colored.fg(color))) - 1 )
# # color_codes_length += 4 * (len(test.split(colored.attr('reset'))) - 1)
# # print('longueur calculée : %d' % (len(test) - color_codes_length))