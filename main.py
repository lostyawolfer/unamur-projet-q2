<<<<<<< Updated upstream
def get_raw_board_data():
    """ Get the initial raw board data from the .lon file.
    
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
            section_data.append(line[:-1])
    
    raw_data.append([section_name, section_data])
    raw_data.pop(0)
    
    return raw_data


def get_game_rules(raw_data):
    """ Get the game rules from the raw data of the .lon file.
    
    Parameters:
    -----------
    raw_data: Raw data retrieved from the .lon file. (list)

    """

    pass


def update_visuals():
    """Syncs the rendered visuals in terminal with the saved game state."""
    ...
=======
from data.game_state import get_all_creatures

print(get_all_creatures())
>>>>>>> Stashed changes
