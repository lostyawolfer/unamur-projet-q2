#-------------Exemple de commande------------------#
#albert:*32-4 denver:@34-4 daniel:energise

#-------------------Fonctions----------------------#



def get_commande_separed (orders : str):
    orders_list = []
    simple_list_orders = orders.split () # ordres sous cette forme : ["albert:*32-4" , "denver:@34-4" , "daniel:energise"]
    for ordre in simple_list_orders:
        orders_list += [ordre.split(":")]
    return orders_list

# On a donc une liste comme ceci: [['albert', '*32-4'], ['denver', '@34-4'], ['daniel', 'energise']]
    

    