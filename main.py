import blessed

def get_raw_board_data():
    """ Get the initial raw board data from the .lon file.

    Return:
    -------
    raw_data: Raw data retrieved from the .lon file. (list)

    Version:
    --------
    Romain Pezzutto (v.1 08/02/2026)
    """

    f = open("board.lon", "r")
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


def clean_raw_board_data(raw_data):
    """ Transforms the raw board data into more flexible data structures.
    
    Parameters:
    -----------
    raw_data: Raw data retrieved from the .lon file. (list)

    Return:
    -------
    gamerules: Data structure that countains informations about the game, e.g. map-size, turns-to-win, etc. (dict)
    creatures: Data structure that countains informations about the creatures, e.g. name, damage, etc. (dict)

    Version:
    --------
    Romain PEZZUTTO (v.1 08/02/2026)
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
            game_rules["spawn"] = {"player_1": spawn_1, "player_2": spawn_2}

        elif section_name == "spur":
            spur = []
            for spur_case in section_data:
                spur_case = (int(spur_case[0]), int(spur_case[1]))
                spur.append(spur_case)
            game_rules["spur"] = tuple(spur)

        else:
            for creature_data in section_data:
                creatures[creature_data[0]] = {"position": (int(creature_data[1]), int(creature_data[2])),
                                               "health": int(creature_data[3]),
                                               "damage": int(creature_data[4]),
                                               "range": int(creature_data[5])}

    return game_rules, creatures


def display_board(game_rules, creatures, heroes):
    """ Displays the initial board.

    Parameters:
    -----------
    gamerules: Data structure that countains informations about the game, e.g. map-size, turns-to-win, etc. (dict)
    creatures: Data structure that countains informations about the creatures, e.g. name, damage, etc. (dict)
    heroes: Data structure that countains informations about the heroes of the players, e.g. name, health, etc. (dict)

    Version:
    --------
    Romain PEZZUTTO (v.1 15/02/2026)
    """

    print(term.home + term.clear)

    background_1 = term.on_color_rgb(BACK_1[0], BACK_1[1], BACK_1[2])(" ")       # Can we use the unpacking operator? If yes, `BACK_1[0], BACK_1[1], BACK_1[2]` becomes `*BACK_1`.
    background_2 = term.on_color_rgb(BACK_2[0], BACK_2[1], BACK_2[2])(" ")

    for line in range(game_rules["map-size"][0]):
        for column in range(game_rules["map-size"][1]):
            if (line + column) % 2 == 0:
                print(background_1, end="")
            else:
                print(background_2, end="")
        print()

    # Still Working on it.
    # Reminder: print(term.on_color_rgb(0, 215, 0)(CREATURE_CELL))


def update_render(game_rules, creatures, heroes):
    """ Updates the rendered visuals in the terminal with the saved game state.

    Parameters:
    -----------
    gamerules: Data structure that countains informations about the game, e.g. map-size, turns-to-win, etc. (dict)
    creatures: Data structure that countains informations about the creatures, e.g. name, damage, etc. (dict)
    heroes: Data structure that countains informations about the heroes of the players, e.g. name, health, etc. (dict)

    Version:
    --------
    """

    pass


if __name__ == "__main__":

    term = blessed.Terminal()

    # =============== CUSTOMISATION ===============
    
    BACK_1 = (0, 215, 0)
    BACK_2 = (215, 215, 215)
    SPUR_1 = (120, 120, 120)
    SPUR_2 = (85, 85, 85)
    P1_COLOR = (0, 0, 255)
    P2_COLOR = (150, 0, 215)

    BARBARIAN_CHAR = "∞"
    HEALER_CHAR = "∏"
    MAGE_CHAR = "∑"
    ROGUE_CHAR = "∂"
    CREATURE_CHAR = term.color_rgb(215, 0, 0)("∫")

    # =============================================

    raw_data = get_raw_board_data()
    game_rules, creatures = clean_raw_board_data(raw_data)

    # FOR TESTING PURPOSES (to delete later):
    heroes = {"player_1": {"Zet-Li":{"class":"healer", "position":[5, 5], "health":10, "max_health":10, "damage":3, "level":1}, "turns_on_goal":0},
              "player_2": {"Nev":{"class":"mage", "position":[15, 15], "health":10, "max_health":10, "damage":3, "level":1}, "turns_on_goal":0}}

    display_board(game_rules, creatures, heroes)
