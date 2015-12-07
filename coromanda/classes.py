import stats as st

class Game(object):
    def __init__(self, home, away):
        self.away_team = away
        self.home_team = home
    def winning_team(self):
        winner = self.home_team
        return winner

class Team(object):
    def __init__(self, name):
        self.team_name = name
        self.stats = {'stat1': st.stat1(name),
                      'stat2': st.stat2(name),
                      'stat3': st.stat3(name),}
            
    def __str__(self):
        return self.team_name
    
    
    

if __name__ == '__main__':
    print('hello')