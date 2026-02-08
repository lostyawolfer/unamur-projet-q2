def get_raw_board_data():
    """ Get the initial raw board data from the .lon file.

    Return:
    -------
    raw_data: Raw Data from the .lon file in the forme of []

    Version:
    --------
    Romain Pezzutto (v.1 08/02/2026)
    """

    f = open("data/board.lon", "r")
    board_file = f.readlines()
    f.close()

    raw_data = []
    section_name = ""
    section_data = []

    for line in board_file:
        if line[-2] == ":":
            raw_data.append([section_name, section_data])
            section_name = line[:-2]
            section_data = []
        else:
            section_data.append(line[:-1].split(" "))
    
    raw_data.append([section_name, section_data])
    raw_data.pop(0)
    
    return raw_data


def get_data_structure(raw_data):
    """ Transforms the raw data into more flexible data structures.
    
    Parameters:
    -----------
    raw_data: Raw data retrieved from the .lon file. (list)

    Return:
    -------
    gamerules: Data structure that countains informations about the game, e.g. map-size, turns-to-win, etc. (dict)
    creatures: Data structure that countains informations about the creatures, e.g. name, damage, etc. (dict)

    Version:
    --------
    Romain Pezzutto (v.1 08/02/2026)
    """

    game_rules = {}
    creatures = {}

    for section in raw_data:

        section_name = section[0]
        section_data = section[1]

        if section_name == "map":
            map_data = section_data[0]
            game_rules["map-size"] = (int(map_data[0]), int(map_data[1]))
            game_rules["turns-to-win"] = int(map_data[2])

        elif section_name == "spawn":
            spawn_1 = (int(section_data[0][0]), int(section_data[0][1]))
            spawn_2 = (int(section_data[1][0]), int(section_data[1][1]))
            game_rules["spawn"] = (spawn_1, spawn_2)

        elif section_name == "spur":
            spur = []
            for spur_case in section_data:
                spur_case = (int(spur_case[0]), int(spur_case[1]))
                spur.append(spur_case)
            game_rules["spur"] = tuple(spur)

        else:
            for creature_data in section_data:
                creatures[creature_data[0]] = {"position": (creature_data[1], creature_data[2]),
                                               "health": creature_data[3],
                                               "damage": creature_data[4],
                                               "range": creature_data[5]}

    return game_rules, creatures


def display_board():
    """ Displays the initial board.
    """

    pass


def update_visuals():
    """ Updates the rendered visuals in the terminal with the saved game state.
    """

    pass


raw_data = get_raw_board_data()
game_rules, creatures = get_data_structure(raw_data)
