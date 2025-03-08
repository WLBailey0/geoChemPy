import matplotlib.pyplot as plt


def make_tas_graph(user_values):

    rock_name = get_rock_names()

    lines = get_line_values()
    for line in lines:
        plt.plot(lines[line][0], lines[line][1], color='black')
    for key, value in rock_name.items():
        plt.text(rock_name[key][0], rock_name[key][1], key, fontsize=8)

    for usr_input in user_values:
        plt.scatter(int(usr_input[0]), int(usr_input[1]), marker='.')
    plt.xlabel(r'$SiO_{2}$')
    plt.ylabel(r'$Na_{2}O + K_{2}O$')
    plt.show()


def get_rock_names():
    rock_name = {'Rhyolite': [71, 9], 'Basalt': [47, 3], 'Picro-\nbasalt': [41.25, 1.5],
                 'Trachy-\nbasalt': [47.2, 5.25], 'Foidite': [41, 9.75], 'Tephrite\n\nBasanite': [42, 5.5],
                 'Phono-\ntephryte': [47.5, 8.75], 'Tephry-\nphonolite': [50.5, 11.5], 'Phonolite': [55, 14],
                 'Basaltic\n Trachy-\n andesite': [51, 6], 'Trachy-\nandesite': [56, 8], 'Trachyte': [61.5, 11.5],
                 'Trachydacite': [62.5, 9], 'Basaltic\nAndesite': [52.5, 3], 'Andesite': [58, 4], 'Dacite': [65.5, 4.5]}
    return rock_name


def get_line_values():
    lines = {1: [[41, 41], [1, 7]], 2: [[45, 45], [1, 5]], 3: [[52, 52], [1, 5]], 4: [[57, 57], [1, 6]],
             5: [[63, 63], [1, 7]], 6: [[69, 69], [8, 13]], 8: [[63, 69], [7, 8]], 9: [[45, 52], [5, 5]],
             10: [[52, 57], [5, 6]], 11: [[63, 57], [7, 6]], 12: [[41, 45], [7, 9]], 13: [[45, 49], [9, 11.5]],
             14: [[50, 52], [15, 14]], 15: [[52, 57.5], [14, 11.5]],
             16: [[60, 57.5], [13, 11.5]], 17: [[45, 49], [9, 7]], 18: [[49, 52], [7, 5]], 19: [[45, 49], [5, 7]],
             20: [[49, 53], [11.5, 9.5]], 21: [[49, 53], [7, 9.5]], 22: [[53, 57.5], [9.5, 11.5]],
             23: [[57.5, 63], [11.5, 7]], 24: [[53, 57], [9.5, 6]], 25: [[41, 45], [3, 3]], 26: [[52, 49], [14, 11.5]],
             27: [[77, 69], [1, 8]]}
    return lines
