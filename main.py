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
    gamerules: Data structure that countains informations about the game, e.g. map_size, turns_to_win, etc. (dict)
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
            game_rules["map_size"] = (int(map_data[0]), int(map_data[1]))
            game_rules["turns_to_win"] = int(map_data[2])

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
                                               "range": int(creature_data[5]),
                                               "effects": []}

    return game_rules, creatures


def display_board(creature, game_rules):
    """ Displays the initial board.

    Parameters:
    -----------
    creatures: Data structure that countains informations about the creatures, e.g. name, damage, etc. (dict)
    gamerules: Data structure that countains informations about the game, e.g. map_size, turns_to_win, etc. (dict)

    Version:
    --------
    Romain PEZZUTTO (v.1 15/02/2026)
    """

    print(term.home + term.clear, end="")

    # Empty map
    for line in range(game_rules["map_size"][0]):
        for column in range(game_rules["map_size"][1]):
            if (line + column) % 2 == 0:
                print(term.on_color_rgb(BACK_1[0], BACK_1[1], BACK_1[2])(" "), end="")    # Can we use the unpacking operator? If yes, `BACK_1[0], BACK_1[1], BACK_1[2]` becomes `*BACK_1`.
            else:
                print(term.on_color_rgb(BACK_2[0], BACK_2[1], BACK_2[2])(" "), end="")
        print()

    # Spawnpoint
    for player in game_rules["spawn"]:
        spawn = game_rules["spawn"][player]
        print(term.move_yx(spawn[0], spawn[1]) + term.on_color_rgb(SPAWN_COL[0], SPAWN_COL[1], SPAWN_COL[2])(" "))

    # Spur
    for spur in game_rules["spur"]:
        if (spur[0] + spur[1]) % 2 == 0:
            print(term.move_yx(spur[0], spur[1]) + term.on_color_rgb(SPUR_1[0], SPUR_1[1], SPUR_1[2])(" "))
        else:
            print(term.move_yx(spur[0], spur[1]) + term.on_color_rgb(SPUR_2[0], SPUR_2[1], SPUR_2[2])(" "))

    # Creatures
    for creature in creatures:
        pos = creatures[creature]["position"]
        parity = True if (pos[0] + pos[1]) % 2 == 0 else False

        # Creature on Spur or Nothing
        if parity:
            if pos in game_rules["spur"]:
                print(term.move_yx(pos[0], pos[1]) + term.on_color_rgb(SPUR_1[0], SPUR_1[1], SPUR_1[2])(CREATURE_CHAR))
            else:
                print(term.move_yx(pos[0], pos[1]) + term.on_color_rgb(BACK_1[0], BACK_1[1], BACK_1[2])(CREATURE_CHAR))
        else:
            if pos in game_rules["spur"]:
                print(term.move_yx(pos[0], pos[1]) + term.on_color_rgb(SPUR_2[0], SPUR_2[1], SPUR_2[2])(CREATURE_CHAR))
            else:
                print(term.move_yx(pos[0], pos[1]) + term.on_color_rgb(BACK_2[0], BACK_2[1], BACK_2[2])(CREATURE_CHAR))

        # Creature on Spawnpoint
        for player in game_rules["spawn"]:
            if pos == game_rules["spawn"][player]:
                print(term.move_yx(pos[0], pos[1]) + term.on_color_rgb(SPAWN_COL[0], SPAWN_COL[1], SPAWN_COL[2])(CREATURE_CHAR))

    # Heroes health & effects
    # ...
    
    # Relocate cursor below
    map_size = game_rules["map_size"]
    print(term.move_y(map_size[0]))      # TO DO: Add lines to compensate "Heroes health & effects"


def update_render(heroes):
    """ Updates the rendered visuals in the terminal with the saved game state.

    Parameters:
    -----------
    heroes: Data structure that countains informations about the heroes of the players, e.g. name, health, etc. (dict)

    Version:
    --------
    Romain PEZZUTTO (v.1 15/02/2026)
    """

    pass


if __name__ == "__main__":

    term = blessed.Terminal()

    # =============== CUSTOMISATION ===============
    
    BACK_1 = (0, 215, 0)
    BACK_2 = (215, 215, 215)
    SPUR_1 = (85, 85, 85)
    SPUR_2 = (120, 120, 120)
    P1_COLOR = (0, 0, 255)
    P2_COLOR = (150, 0, 215)
    SPAWN_COL = (150, 0, 220)

    BARBARIAN_CHAR = "∞"
    HEALER_CHAR = "∏"
    MAGE_CHAR = "∑"
    ROGUE_CHAR = "∂"
    CREATURE_CHAR = term.color_rgb(215, 0, 0)("∫")

    STUN_CHAR = "⚡"
    IMMUNISE = "🛡️"
    OVIBUS = "🚫"

    # =============================================

    raw_data = get_raw_board_data()
    game_rules, creatures = clean_raw_board_data(raw_data)

    # FOR TESTING PURPOSES (to delete later):
    heroes = {"player_1": {"Zet-Li":{"class":"healer", "prev_position": [8, 15], "position":[7, 15], "health":10, "max_health":10, "damage":3, "level":1, "effects":[]}, "turns_on_spur":0},
              "player_2": {"Nev":{"class":"mage", "prev_position": [8, 20], "position":[7, 20], "health":10, "max_health":10, "damage":3, "level":1, "effects":[]}, "turns_on_spur":0}}

    display_board(creatures, game_rules)
    update_render(heroes)
