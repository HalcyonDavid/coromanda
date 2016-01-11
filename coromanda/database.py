import matlab.engine
eng = matlab.engine.start_matlab()

def getname(gid, home=True):
    """
    If home is true return name of home team
    if home id false return name of away team
    """
    if home:
        name = eng.getinfo('home', gid)
    else:
        name = eng.getinfo('away', gid)
    
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
    winner = eng.getinfo('winner', gid)
    print winner
    if winner == getname(gid):
        return 1
    else:
        return 0;

def getodds(gid, home=True):
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

def w5(gid, home=True):
    if home:
        stat = eng.getstat('W5', getname(gid), gid)
    else:
        stat = eng.getstat('W5', getname(gid, home=False), gid)
    print(stat)
    return stat
    
if __name__ == "__main__":
    pass
