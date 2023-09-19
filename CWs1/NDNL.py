class People():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        assert self.age > 0,"Age must be greater than 0"
class SoccerPlayer(People):
    def __init__(self,name,age, position,pay,overall):
        super().__init__(name, age)
        self.position = position
        self.pay = pay
        self.overall = overall
        assert self.pay > 0,"Pay must be greater than 0"
        assert  30 > self.age > 15,"Age must be greater than 15 and less then 30"
        assert 100 > self.overall > 0,"Overall must be between 0 and 100"
        assert self.position in ["Goalkeeper", "Defender", "Midfielder", "Attacker"], "Position must be Goalkeeper, Defender, Midfielder or Attacker"
class Manager(People):
    def __init__(self,name,age,pay,start,end):
        super().__init__(name, age)
        self.pay = pay
        self.start = start
        self.end = end
        assert self.pay > 0,"Pay must be greater than 0"
        assert self.end > self.start,"End of contract must be greater than start"
class Team():
    instance = []

    list_of_players = []
    def __init__(self,balance):
        self.balance = balance
        self.players = {}
        self.managers = {}
        self.__class__.instance.append(self)
    def add_player(self, player):
        self.players["name"] = player.name
        self.players["position"] = player.position
        self.players["age"] = player.age
        self.players["pay"] = player.pay
        self.players["overall"] = player.overall
        Team.list_of_players.append(self.players)
    def set_manager(self, manager):
        # if manager.name in self.managers:
        self.managers["name"] = manager.name
        self.managers["age"] = manager.age
        self.managers["pay"] = manager.pay
        self.managers["start"] = manager.start
        self.managers["end"] = manager.end
    @classmethod
    def check_player(self):
        if len(self.list_of_players) == 11:
            return False
        else:
            return True
    def Transfer_player(self,player,team_from):
        self.balance = self.balance - player.pay
        team_from.balance = team_from.balance + player.pay





class League():pass






team1 = Team(20000000000)
team1.add_player(SoccerPlayer("HARRY MAGUIRE", 20, "Goalkeeper", 1000, 12))
team1.add_player(SoccerPlayer("ROMALDO", 29, "Attacker", 300000, 92))
team1.add_player(SoccerPlayer("MOUSA", 29, "Attacker", 300000, 92))
team1.add_player(SoccerPlayer("EMAD", 27, "Attacker", 300000, 92))
team1.add_player(SoccerPlayer("AHMAD", 29, "Defender", 302000, 35))
team1.add_player(SoccerPlayer("AMIN", 29, "Defender", 3000, 35))
team1.add_player(SoccerPlayer("SAMAN", 22, "Defender", 300000, 73))
team1.add_player(SoccerPlayer("MATIN", 29, "Defender", 31000, 15))
team1.add_player(SoccerPlayer("AZMOON", 22, "Midfielder", 800000, 99))
team1.add_player(SoccerPlayer("AFSHAR", 29, "Midfielder", 300000, 92))
team1.add_player(SoccerPlayer("HAURT", 20, "Midfielder", 300000, 92))
team1.set_manager(Manager("yousof", 69, 4000, 2019, 2020))
team2 = Team(25000000000)
team2.add_player(SoccerPlayer("HARRY MAGUIRE", 25, "Goalkeeper", 1000, 12))
team2.add_player(SoccerPlayer("ROMALDO", 25, "Midfielder", 300000, 92))
team2.add_player(SoccerPlayer("MOUSA", 25, "Midfielder", 300000, 92))
team2.add_player(SoccerPlayer("REZA", 25, "Attacker", 300000, 92))
team2.add_player(SoccerPlayer("AHMAD", 25, "Defender", 302000, 35))
team2.add_player(SoccerPlayer("AMIN", 29, "Defender", 3000, 35))
team2.add_player(SoccerPlayer("SAMAN", 22, "Midfielder", 300000, 73))
team2.add_player(SoccerPlayer("EMAD", 29, "Defender", 31000, 15))
team2.add_player(SoccerPlayer("AZMOON", 22, "Attacker", 800000, 99))
team2.add_player(SoccerPlayer("EHSAN", 29, "Attacker", 300000, 92))
team2.add_player(SoccerPlayer("AMIR", 20, "Defender", 300000, 92))
team2.set_manager(Manager("ali", 58, 4000, 2020, 2025))






print("\n".join(str(team1.list_of_players).split("}")))

print(team1.managers)
for i in Team.instance:
    print (i.list_of_players)