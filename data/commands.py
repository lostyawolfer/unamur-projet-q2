#-------------Exemple de commande------------------#
#albert:*32-4 denver:@34-4 daniel:energise

from data_structures import creatures
from data_structures import heroes
from data_structures import game_rules

def is_legal_position(pos: tuple[int, int]) -> bool:
    """
    Checks if the specified position exists within confines of the map.

    Parameters
    ----------
    pos: tuple[int, int] - position to check

    Returns
    -------
    bool - True if position is within the map, False otherwise
    """
    if not 1 <= pos[0] <= game_rules["map-size"][0]: return False
    if not 1 <= pos[1] <= game_rules["map-size"][1]: return False
    return True

#-------------Structure de donnée------------------#

actions = { "shifting" : [] , "attack" : [] , "special_attack" : []}

stats = {
    "barbarian": {
        'health': 10,
        'damage': 3,
        'abilities': ('energize', 'stun')
    },
    "healer": {
        'health': 10,
        'damage': 2,
        'abilities': ('invigorate', 'immunise')
    },
    "mage": {
        'health': 10,
        'damage': 2,
        'abilities': ('fulgura', 'ovibus')
    },
    "rogue": {
        'health': 10,
        'damage': 2,
        'abilities': ('reach', 'burst')
    }
}


#-----------------------------Fonctions--------------------------------#
#--------------Gestion de commandes----------------#


def get_commande_separed (orders : str) -> list:
    """Return in a list every order in the string
    
    Parameters:
    -----------
    orders (str): order send by players

    Return:
    -------
    list: Every element is an order witch is a list, the first element is hero's name or creature's name and the second is the action or the type of hero

    Version:
    --------
    Lisette DEVILLERS (v.1 14/02/2026)
    """
    orders_list = []
    simple_list_orders = orders.split () # ordres sous cette forme : ["albert:*32-4" , "denver:@34-4" , "daniel:energise"]
    for ordre in simple_list_orders:
        orders_list += [ordre.split(":")]
    return orders_list

# On a donc une liste comme ceci: [['albert', '*32-4'], ['denver', '@34-4'], ['daniel', 'reach' , '33-24']]
ovibus = [False , ""]

def get_in_dict_orders (orders : list , player : str) -> dict:
    """
    Create a dictionnary with for differents actions, a list wich contain all action's orders
    
    Parameters:
    -----------
    orders(list): a list wich contain all orders. On order is a list, the first element is hero's name or creature's name and the second is the action

    player(str): player's name

    Return:
    -------
    dict: one key is for the list of orders of one action's type.

    Version:
    --------
    Lisette DEVILLERS (v.2 21/02/2026)
    """
    list_heroes = []
    if ovibus [0]== True: #le héro ciblé par ovibus ne receverra pas de commandes
        list_heroes += ovibus [1]
        ovibus = [False , ""]
    for order in orders :
        if not order [0] in list_heroes:
            if order [1] [0] == "*" :
                coord = order[1].split("-")
                actions ["shifting"] += (player, order[0] , (coord[0] , coord[1]))
            elif order [1] [0] == "@":
                coord = order[1].split("-")
                actions ["attack"] += (player, order[0] , (coord[0] , coord[1]))
            elif order[1] in stats[heroes [player][order[0]] ["class"]] : #nom attack  se trouve dans les sorts possibles par le hero
                if order [1] in ["immunise" , "fulgura" , "ovibus" , "reach"]:
                    actions ["special_attack"] += (player , order[0] , order[1] , order[2])
                else:
                    actions ["special_attack"] += (player , order[0] , order[1] )
        list_heroes += order [0]

    # dico sous cette forme: action: { shifting : [ (player, name , (x , y)) , (player, name , (x , y)) ....] , attack : [(player, name , (x , y)) , (player, name , (x , y)) .... ] , special_attack : [(player, name , type) , (player, name , type) ....]}


#--------------Aplition de commandes---------------#

def execute_orders (orders : dict): 
    """
    Execute the orders

    Parameters:
    -----------
    orders (dict): a dictionnary wich associate for differents actions, a list wich contain all action's orders

    PS: Use tree other function: shifting, attack, special attack

    Version:
    --------
    Lisette DEVILLERS (v.1 14/02/2026)
    """
    for order in orders["special_attack"]:
        special_attack (order)
    for order in orders ["attack"]:
        attack (order)
    for order in orders ["shifting"]:
        shifting (order)

def shifting (order : list ):
    """
    Move a character
    
    Parameter:
    ----------
    order (list): the first element is hero's name or creature's name and the second is the coordinates where the character want to go

    Version:
    --------
    Lisette DEVILLERS (v.1 14/02/2026)
    """

def attack (order : list):
    """
    Attack a character

    Parameter:
    ----------
    order (list): the first element is hero's name or creature's name who want to attack and the second is the victime's coordinates

    Version:
    --------
    Lisette DEVILLERS (v.1 14/02/2026)
    """


niveau_requis = 0
def special_attack (order : list):
    """
    Execute the special attack
    
    Parameter:
    ----------
    order (list): the first element is hero's name and the second is attack's name

    Version:
    --------
    Lisette DEVILLERS (v.1 14/02/2026)
    """
    player = order[0]
    hero = order [1]
    attack = order [2]
    if not exised_or_not (hero):
        print(f"Le héro {hero} n'existe pas")
    elif heroes [player] [hero] ['level'] < niveau_requis :
        print(f"Le héro {hero} ne possède pas un niveau suffisament élevé")
    
    if attack == "energise":
        for coord in near (heroes [player] [hero] ['position']):
            for heroe in heroes [player] [hero] :
                if heroes [player] [heroe] ['position'] == coord:
                   heroes [player] [heroe] ['energise'] = True



# [(player, name , type) , (player, name , type , coord) ....]}


def get_entities_at(pos: tuple[int, int]) -> dict:
    """
    Gets all entities at the specified position.

    Parameters
    ----------
    pos: tuple[int, int] - position to check

    Returns
    -------
    dict - container of all entities that exist in that position.

    {
        "creatures": { (creature name): {(all creature info in a dict...)} },
        "heroes": {
            "player_1": { (hero name): {(all hero info in a dict...)} },
            "player_2": { (hero name): {(all hero info in a dict...)} }
        }
    }

    """
    res = {
        "creatures": {},
        "heroes": {
            "player_1": {},
            "player_2": {}
        }
    }

    for creature in creatures:
        if creatures[creature]["position"] == pos:
            res['creatures'][creature] = creatures[creature].copy()

    for player in heroes:
        for hero in heroes[player]:
            if heroes[player][hero]['position'] == pos:
                res['heroes'][player][hero] = heroes[player][hero].copy()

    return res


def exised_or_not (name : str) -> bool:
    """ check if the character is real
    Parameters:
    -----------
    name (str): character's name

    Return:
    -------
    bool: True if the character exist
    Version:
    --------
    Lisette DEVILLERS (v.1 22/02/2026)
    """
    for creature in creatures:
        if name == creature:
            return True
    for player in heros:
        for hero in player:
            if name == hero:
                return True
    return False

def near (coord : list) -> list:
    """ Return a list with every coordinate near the first
    """
    all_coord = [ [coord [0] +1 ,coord [1] ] , [coord [0] +1 ,coord [1] +1] ,[coord [0] +1 ,coord [1] -1 ] ,[coord [0] ,coord [1] +1] ,[coord [0] ,coord [1] -1] ,[coord [0] -1,coord [1] ] ,[coord [0] -1 ,coord [1] -1] ,[coord [0] -1,coord [1] +1] ,]
    return all_coord




    

    