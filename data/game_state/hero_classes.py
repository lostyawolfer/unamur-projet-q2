barbarian = 'barbarian'
healer = 'healer'
mage = 'mage'
rogue = 'rogue'

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

def class_exists(hcls: str) -> bool:
    """
    Validates the existence of given hero class name.

    Parameters
    ----------
    hcls: str - name of the hero class

    Returns
    -------
    bool - True if class exists, False if it doesn't
    """
    class_list = (barbarian, healer, mage, rogue)
    if not hcls in class_list:
        return False
    return True


def get_abilities(hcls: str) -> tuple[str, str]:
    """
    Gets the ability list of a given haro class.

    Parameters
    ----------
    hcls: str - name of the hero class

    Returns
    -------
    tuple -

    Raises
    ------
    ValueError: class doesn't exist - if hcls is an invalid hero class
    """
    if not class_exists(hcls): raise ValueError(f"class {hcls} doesn't exist")
    return stats[hcls]['abilities']