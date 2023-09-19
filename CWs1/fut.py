import random
import  itertools



class PlayerNotFound(Exception):
    pass
class Morethen11Player(Exception):
    pass








class Person:
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            raise ValueError("Age can't be negative")
        self.age = age


class Player(Person):
    all_players = []
    def __init__(self, name, age, salary, post, performance):
        super().__init__(name, age)
        if salary < 0:
            raise ValueError("salary can't be negative")
        self.salary = salary
        self.post = post
        Player.all_players.append(self.name)
        if not 0 < performance < 100:
            raise ValueError("performance should be between 0 to 100")
        self.performance = performance
        if not 15 < age < 30:
            raise ValueError("age of player should be between 15 to 30")


class Coach(Person):
    def __init__(self, name, age, salary, start, end):
        super().__init__(name, age)
        if salary < 0:
            raise ValueError("salary can't be negative")
        self.salary = salary
        self.salary = salary
        self.start = start
        self.end = end
        if not 30 < age < 65:
            raise ValueError("age of coach should be between 30 to 65")


class Team:
    coaches = []
    player_dict = {}
    teams_dict = {}

    def __init__(self, point, name, balance, coach):
        self.total_player = []
        self.point = point
        self.name = name
        if coach in Team.coaches:
            raise ValueError("already exist")
        self.coach = coach
        Team.coaches.append(coach)
        self.balance = balance
        Team.teams_dict[self.name] = self

    def check(self):
       if 7 <= len(self.total_player) <= 11:
           raise Morethen11Player

    def add_player(self, player):
        if len(self.total_player) <= 11:
            check_player_available = True
            for key in Team.player_dict.keys():
                if player in Team.player_dict[key]:
                    check_player_available = False

            if check_player_available:
                self.total_player.append(player)
                if not Team.player_dict.get(self.name) == None:
                    Team.player_dict[self.name].append(player)
                else:
                    Team.player_dict[self.name] = [player]
            else:
                raise Exception("Player is used before")
        else:
            raise Exception("Team already has 11 players")
    def make_player(self,name):
        a = Team.player_dict.values()
        print(a)
        for b in a:
            for c in b:
                if c.name == name:
                    return c
    def buy(self, player, price):
        if self.balance >= price:
            flag = False
            for k in Team.player_dict:
                if player in Team.player_dict[k] and  k != self.name: # پیدا کردن پلیر و چک کردن در تیم خودش نباشه
                    Team.player_dict[k].remove(player)
                    self.add_player(player)
                    self.balance = self.balance - price
                    flag = True
                    break
            if not flag :
                raise PlayerNotFound

        else:
            raise ValueError("NOT ENOUGH MONEY")

    def __lt__(self, other):
        return self.point < other.point

    def __gt__(self, other):
        return self.point > other.point

    def __eq__(self, other):
        return self.point == other.point


class League:
    def __init__(self,name):
        self.name = name
        self.num = random.randint(1,1000000000000000000)
        self.teams = []

    def match(self, team1: Team, team2: Team):
        team1.check()
        team2.check()
        random_match = random.randint(0, 2)
        if random_match == 0:
            team1.point += 1
            team2.point += 1
        elif random_match == 1:
            team1.point += 3
        else:
            team2.point += 3

    def add_team(self, team):
        self.teams.append(team)

    def show_point(self):
        sorted_teams = sorted(self.teams, reverse=True)
        for team in sorted_teams:
            print(f"team {team.name} :{team.point}")

h1 = Person("armin", 27)
p1 = Player("armin", 27, 1, 1000, 10)
p2 = Player("asghar", 26, 1, 1000, 10)
c1 = Coach("armin", 57, 3000, 15, 17)
c2 = Coach("ahmad", 47, 2000, 15, 17)
team1 = Team(0, "real", 1000, "fergosen")
team2 = Team(0, "barca", 1000, "moorinio")
team1.add_player(p1)
team1.add_player(p2)
lig1 = League("a")
lig1.add_team(team1)
lig1.add_team(team2)
# for i in Team.player_dict.values():
#     for j in i :
#         print(j.name)
print([i.name for i in Team.player_dict["real"]])
# print(a.name for a in Team.player_dict.values())
# lig1 = League("a")
# lig1.match(team1,team2)
# lig1.add_team(team1)
# lig1.add_team(team2)
# lig1.match(team1,team2)
# lig1.show_point()
# print(Team.teams_dict["real"])



def team_menu():
    try:
        team = input("choose yous team")
        if team in Team.teams_dict:
            team = Team.teams_dict[team]
        else:
            point, balance, coach = input("this team dosnt exist put team point,balance and coach").split(",")
            team = Team(point, team, balance, coach)
        while True:
            options = ["Player(input('name: '), int(input('age: ')),float(input('salary: ')),input('post:  '),int(input('performance: ')))",
                       "print(Player.all_players)",
                       "print([i.name for i in Team.player_dict[team.name]])",
                       "team.buy(Team.make_player(name = input('name: ')), int(input('price: ')))",
                       "print(Team.teams_dict.keys())",
                       "break"
                       ]
            num_options = [1, 2, 3, 4, 5, 6]
            try:
                print("\n1. ADD PLAYER")
                print("2. SHOW LIST OF PLAYER")
                print("3. SHOW PLAYERS IN A TEAM")
                print("4. BUY PLAYER")
                print("5. SHOW LIST OF TEAM")
                print("6. LOGOUT")
                option = zip(num_options, options)
                user_choose = int(input("SELECT YOUR CHOICE (1-6): "))
                if 1 <= user_choose <= 6:
                    pass
                else:
                    print("Invalid input. Please enter a number between 1 and 6.")
                for munes, funcs in option:
                    if user_choose == munes:
                        eval(funcs)
            except ValueError:
                print("Please try again, your input is invalid.")
        defult_menu()
    except Exception as error:
        print(error)
def league_menu():
    try:
        league = League(input("name: "))
        while True:
            options = ["league.add_team(Team.teams_dict[input('name:')])",
                       "league.match(Team.teams_dict[input('name team home:')],Team.teams_dict[input('name team away:')])",
                       "league.show_point()",
                       "break"
                       ]
            num_options = [1, 2, 3, 4]
            try:
                print("\n1. ADD TEAM TO LEAGUE")
                print("2. MATCH")
                print("3. SHOW TABLES")
                print("4. LOGOUT")
                option = zip(num_options, options)
                user_choose = int(input("SELECT YOUR CHOICE (1-4): "))
                if 1 <= user_choose <= 4:
                    pass
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
                for munes, funcs in option:
                    if user_choose == munes:
                        eval(funcs)
            except ValueError:
                print("Please try again, your input is invalid.")
        defult_menu()
    except Exception as error:
        print(error)

def defult_menu():
    while True:
        status = int(input("1. CREATE TEAM \n2.CREATE LEAGUE \n3.EXIT\noption:"))
        if status == 1:
            team_menu()
        elif status == 2:
            league_menu()
        elif status == 3:
            break
        else:print("INVALID INPUT")

# defult_menu()

