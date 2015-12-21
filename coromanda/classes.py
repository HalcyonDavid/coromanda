import stats as st

class Game(object):
    def __init__(self, home, away, gameid):
        self.away_team = away
        self.home_team = home
        self.gameid = gameid
        
    def __str__(self):
        return str(self.id) + 'Home: ' + self.home_team +  ' Away: ' + self.away_team
        
    def winner(self):
        winner = self.home_team.name
        chance = 1
        return winner, chance
    
    def online_odds(self):
        winner = self.winner()
        return {}
    
    def best_odds(self):
        odds = self.online_odds()
        best = min(odds, key=odds.get)
        return best, odds[best]

class Team(object):
    def __init__(self, name):
        self.team_name = name
        
        self.home_stats = {'shots_for': st.shots_for(name),
                           'shots_against': st.shots_against(name),
                           'goals_for': st.goals_for(name),
                           'goals_against': st.goals_against(name),
                           'wins': st.wins(name),
                           'win_percentage': st.win_percentage(name),                    
                           }
        
        self.away_stats = {'shots_for': st.shots_for(name, home=False),
                           'shots_against': st.shots_against(name, home=False),
                           'goals_for': st.goals_for(name, home=False),
                           'goals_against': st.goals_against(name, home=False),
                           'wins': st.wins(name, home=False),
                           'win_percentage': st.win_percentage(name, home=False),                    
                           }

        self.total_stats = {'shots_for': st.shots_for(name, home=None),
                           'shots_against': st.shots_against(name, home=None),
                           'goals_for': st.goals_for(name, home=None),
                           'goals_against': st.goals_against(name, home=None),
                           'wins': st.wins(name, home=None),
                           'win_percentage': st.win_percentage(name, home=None),                    
                           }
    def __str__(self):
        return self.team_name

if __name__ == '__main__':
    pass
