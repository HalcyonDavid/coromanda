def getname(gid, home=False):
    """
    If home is true return name of home team
    if home id false return name of away team
    """
    return 'aaa'
    
def getdate(gid):
    """
    Returns date of game id in format dd-mm-yy
    """
    return 11-11-11

def win(gid):
    """
    Returns 1 if the home team won
    or 0 if the away team won
    
    Parameter
    ---------
    gid : int 
    """
    return 1

def getodds(gid, home=False):
    """
    Returns a dictionary mapping the name of website
    to the payout.
    ex. {'name': 1.9, # if name will pay out 1.9
         'name2': 2}
    """
    return {'aaaa': 2}

def getgidsfromdate(date):
    """
    Returns a list of gids on the date
    """
    return [123,124]
    
if __name__ == "__main__":
    pass
