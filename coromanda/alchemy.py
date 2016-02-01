from sqlalchemy import *

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/halcyonnhl')

def getinfo(info, gid):
  # home, away, winner, gametype
  value = engine.execute('SELECT %s FROM games WHERE gameID=%d' %(info, gid))
  return str(value)

def getstat(stat, team, gid):
  if stat == 'w5':
      values = engine.execute('SELECT COUNT(*) FROM (SELECT * from altgames WHERE team=''%s'' AND gameID < %d ORDER BY gameID DESC LIMIT 5) AS S WHERE result=''%s''' %(team,ID,'W'))
  else:
      values = None
  return values
