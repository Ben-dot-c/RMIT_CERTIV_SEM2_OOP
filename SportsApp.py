from teamAGG import Team
from playerAGG import Player
class SportsApp:
    @staticmethod

    def main():
        teams = []
        players = []

        t1 = Team("Saints", "AFL", "St Kilda")
        t2 = Team("Man U", "Footy", "Manchester")
        t3 = Team("Raptors", "Basketball", "Toronto")
        t4 = Team("Sharks", "Rugby", "Sydney")
        t5 = Team("Lions", "Cricket", "Brisbane")
        t6 = Team("Wolves", "Soccer", "Birmingham")
        

        teams.append(t1)
        teams.append(t2)
        teams.append(t3)
        teams.append(t4)
        teams.append(t5)
        teams.append(t6)

        p1 = Player("John F Kennedy", "Capitan", t1)
        p2 = Player("Smith Johnson", "Center", t2)
        p3 = Player("Alice Walker", "Forward", t3)
        p4 = Player("Brian O'Neil", "Hooker", t4)
        p5 = Player("Maya Patel", "Bowler", t5)
        p6 = Player("Liam Nguyen", "Striker", t6)


        players.append(p1)
        players.append(p2)
        players.append(p3)
        players.append(p4)
        players.append(p5)
        players.append(p6)

        n = 0
        for i in teams:
            print(f"----------Team {n + 1}----------")
            print(teams[n])
            n += 1
        print("\n")
        x = 0
        for i in players:
            print(f"\n----------Player {x + 1}----------")
            print(players[x])
            print(f"----------Player {x + 1} Team Details----------")
            print(players[x].get_teamObj())
            x += 1

SportsApp.main()
#test