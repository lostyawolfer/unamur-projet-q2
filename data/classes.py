barbarian = 'barbarian'
healer = 'healer'
mage = 'mage'
rogue = 'rogue'

def class_exists(cls: str) -> bool:
    """
    Validates the hero class name.

    Parameters
    ----------
    cls: str - name of the class

    Returns
    -------
    bool: True if class exists, False if it doesn't
    """
    class_list = (barbarian, healer, mage, rogue)
    if not cls in class_list:
        return False
    return True

stats = {
    barbarian: {
        'health': 10,
        'damage': 3,
        'abilities': ('energize', 'stun')
    },
    healer: {
        'health': 10,
        'damage': 2,
        'abilities': ('invigorate', 'immunise')
    },
    mage: {
        'health': 10,
        'damage': 2,
        'abilities': ('fulgura', 'ovibus')
    },
    rogue: {
        'health': 10,
        'damage': 2,
        'abilities': ('reach', 'burst')
    }
}