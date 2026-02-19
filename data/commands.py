#-------------Exemple de commande------------------#
#albert:*32-4 denver:@34-4 daniel:energise


#-------------Structure de donnée------------------#

actions = { "shifting" : [] , "attack" : [] , "special_attack" : []}

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

# On a donc une liste comme ceci: [['albert', '*32-4'], ['denver', '@34-4'], ['daniel', 'energise']]


def get_in_dict_orders (orders : list) -> dict:
    """
    Create a dictionnary with for differents actions, a list wich contain all action's orders
    
    Parameters:
    -----------
    orders(list): a list wich contain all orders. On order is a list, the first element is hero's name or creature's name and the second is the action

    Return:
    -------
    dict: one key is for the list of orders of one action's type.

    Version:
    --------
    Lisette DEVILLERS (v.1 14/02/2026)
    """
    "heros" = []
    for order in orders :
        if not order [0] in "heros":
            if order [1] [0] == "*" :
                coord = order[1].split("-")
                actions ["shifting"] += ( order[0] , (coord[0] , coord[1]))
            elif order [1] [0] == "@":
                coord = order[1].split("-")
                actions ["attack"] += ( order[0] , (coord[0] , coord[1]))
            elif order [1] in "pouvoir":
                if 
            "heros" += order [0]




    # dico sous cette forme: action: { shifting : [ (name , (x , y)) , (name , (x , y)) ....] , attack : [(name , (x , y)) , (name , (x , y)) .... ] , special_attack : [(name , type) , (name , type) ....]}


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







    



    

    