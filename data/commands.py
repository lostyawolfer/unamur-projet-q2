#-------------Exemple de commande------------------#
#albert:*32-4 denver:@34-4 daniel:energise


#-------------Structure de donnée------------------#


#-------------------Fonctions----------------------#



def get_commande_separed (orders : str) -> list:
    """Return in a list every order in the string
    
    Parameters:
    -----------
    orders (str): order send by players

    Return:
    -------
    list: Every element is an order witch is a list, the first element is hero's name or creature's name and the second is the action or the type of hero
    """
    orders_list = []
    simple_list_orders = orders.split () # ordres sous cette forme : ["albert:*32-4" , "denver:@34-4" , "daniel:energise"]
    for ordre in simple_list_orders:
        orders_list += [ordre.split(":")]
    return orders_list

# On a donc une liste comme ceci: [['albert', '*32-4'], ['denver', '@34-4'], ['daniel', 'energise']]

actions = { "shifting" : [] , "attack" : [] , "special_attack" : []}

def get_in_details_order (order : list):
    """
    Add in action dictionnary the order
    
    Parameters:
    order(list): order is a list, the first element is hero's name or creature's name and the second is the action
    """
    # dico sous cette forme: action: { shifting : [ (name , (x , y)) , (name , (x , y)) ....] , attack : [(name , (x , y)) , (name , (x , y)) .... ] , special_attack : [(name , type) , (name , type) ....]}




def execute_order (order : dict): 
    """
    Execute the order

    Parameters:
    order (dict): One order like this: name_chara : {"action" : type , "target" : (x : y)}

    PS: Use tree other function: shifting, attack, special attack
    """







    



    

    