ORGINALBALANCE = 500
ORGINALHEALTH = 0


class Troops:
    troops = dict()
    troops_id = 0
    troops_capacity = 50

    def __init__(self, health, type, starttime):
        Troops.troops_id += 1
        self.health = health
        self.type = type
        self.starttime = starttime
        self.accessible = True
        Troops.troops[Troops.troops_id] = self


def attack_enemy(func):
    def wrapper(*args):
        attack(args[-1])
        result = func(*args)
        return result

    return wrapper


def check_enemy(func):
    def wrapper(*args):
        global ORGINALBALANCE
        global ORGINALHEALTH
        if ORGINALHEALTH <= 0:
            return "game over"
        result = func(*args)
        return result

    return wrapper


def check_money(func):
    def wrapper(*args):
        money_auto(args[-1])
        result = func(*args)
        return result

    return wrapper


def income(num):
    global ORGINALBALANCE
    global ORGINALHEALTH
    ORGINALBALANCE += num


def gamebasedmoney(time_in_second):
    delta_time = time_in_second - GameBasedMoney.starttime
    income = GameBasedMoney.income
    speed = GameBasedMoney.speed
    set_start_time(GameBasedMoney, runtime(GameBasedMoney, time_in_second))
    return delta_time // speed * income


def money_auto(timestamps):
    time_in_seconds = Timestaps(timestamps)
    amount = 0
    miner_counter = 0
    for ids in Troops.troops:
        if Troops.troops[ids].accessible:
            if miner_counter < 8:
                if Troops.troops[ids].type == "miner":
                    troop_income = Troops.troops[ids].income
                    speed = Troops.troops[ids].speed
                    delta_time = time_in_seconds - Troops.troops[ids].starttime
                    amount += delta_time // speed * troop_income
                    set_start_time(Troops.troops[ids], runtime(Troops.troops[ids], time_in_seconds))
                    miner_counter += 1
    amount += gamebasedmoney(time_in_seconds)
    income(amount)


def attack(timestamps):
    global ORGINALBALANCE
    global ORGINALHEALTH
    time_in_seconds = Timestaps(timestamps)
    attack_damage: int = 0
    for ids in Troops.troops:
        if Troops.troops[ids].accessible:
            if Troops.troops[ids].type == "miner":  # if Troops.troops[ids].type != "miner":
                continue
            power = Troops.troops[ids].power
            speed = Troops.troops[ids].speed
            delta_time = time_in_seconds - Troops.troops[ids].starttime
            attack_damage += delta_time // speed * power
            set_start_time(Troops.troops[ids], runtime(Troops.troops[ids], time_in_seconds))
    ORGINALHEALTH -= attack_damage


def get_commands():
    global ORGINALBALANCE
    global ORGINALHEALTH
    q, h = map(int, input().split())  # تو یک خط با فاصله
    ORGINALHEALTH = h
    req_list = []
    for _ in range(q):
        request = input().split()
        req_list.append(request)
    CommandManager.command_manager(req_list)


def runtime(troop: Troops, time_in_seconds):
    I = troop.starttime
    while I < time_in_seconds:
        I += troop.speed
    return round(I - troop.speed)


def kill_troop(troops_id: int, time_in_seconds):
    Troops.troops[troops_id].accessible = False
    return "dead"


def set_start_time(troops: Troops, last_time_use: int):
    troops.starttime = last_time_use


def Timestaps(timestamps):
    minutes, seconds, milliseconds = map(int, timestamps.split(':'))
    time_in_seconds = minutes * 60 + seconds + milliseconds / 1000
    return time_in_seconds


class Miner(Troops):
    health = 100
    cost = 150
    speed = 10
    income = 100
    unit = 1

    def __init__(self, starttime):
        super().__init__(Miner.health, "miner", starttime)


class Archidon(Troops):
    health = 80
    cost = 300
    power = 10
    speed = 1
    unit = 1

    def __init__(self, starttime):
        super().__init__(Archidon.health, "archidon", starttime)


class GameBasedMoney:
    speed = 20
    starttime = 0
    income = 180


class Giant(Troops):
    health = 1000
    cost = 1500
    power = 150
    speed = 4
    unit = 4

    def __init__(self, starttime):
        super().__init__(Giant.health, "giant", starttime)


class Magikill(Troops):
    health = 80
    cost = 1200
    power = 200
    speed = 5
    unit = 4

    def __init__(self, starttime):
        super().__init__(Magikill.health, "magikill", starttime)


class Spearton(Troops):
    health = 250
    cost = 500
    power = 35
    speed = 3
    unit = 2

    def __init__(self, starttime):
        super().__init__(Spearton.health, "spearton", starttime)


class Swordwrath(Troops):
    health = 120
    cost = 125
    power = 20
    speed = 1
    unit = 1

    def __init__(self, starttime):
        super().__init__(Swordwrath.health, "swordwrath", starttime)


@check_money
@check_enemy
@attack_enemy
def add_troop(troops_type: str, timestamps):  # type == one of trups class names
    global ORGINALBALANCE
    global ORGINALHEALTH
    troops_type = eval(troops_type.capitalize())
    time_in_seconds = Timestaps(timestamps)
    if ORGINALBALANCE - troops_type.cost < 0:
        return "not enough money!"
    elif Troops.troops_capacity - troops_type.unit < 0:
        return "too many troops!"
    else:
        Troops.troops_capacity -= troops_type.unit
        ORGINALBALANCE -= troops_type.cost
        troops_type(starttime=time_in_seconds)
        return Troops.troops_id


@check_money
@check_enemy
@attack_enemy
def army_status(timestamps):
    time_in_seconds = Timestaps(timestamps)
    troops_dict = {"giant": 0, "magikill": 0, "spearton": 0, "archidon": 0, "swordwrath": 0, "miner": 0}
    for i in list(Troops.troops.items()):
        if i[1].accessible:
            troop = i[1].type
            troops_dict[troop] += 1
    return " ".join(map(str, reversed(list(troops_dict.values()))))


@check_money
@check_enemy
@attack_enemy
def damage(troops_id: int, power: int, timestamps):
    time_in_seconds = Timestaps(timestamps)
    troops_id = int(troops_id)
    power = int(power)
    try:
        if not Troops.troops[troops_id].accessible:
            raise Exception()
        Troops.troops[troops_id].health -= power
    except:
        return "no matter"
    if Troops.troops[troops_id].health <= 0:
        return kill_troop(troops_id, time_in_seconds)
    else:
        return Troops.troops[troops_id].health


@check_money
@check_enemy
@attack_enemy
def enemy_status(timestamps):
    time_in_seconds = Timestaps(timestamps)
    return int(ORGINALHEALTH)


@check_money
@check_enemy
@attack_enemy
def money_status(timestamps):
    return int(ORGINALBALANCE)


class CommandManager:
    # command_functions = {
    #     "add": Add_Troops.add_troop,
    #     "damage": Damage.damage,
    #     "enemy-status": Enemy_Status.enemy_status,
    #     "army-status": Army_Status.army_status,
    #     "money-status": Money_Status.money_status}
    # @staticmethod
    # def command_manager(req_list):
    #     for requests in req_list:
    #         command = requests[0]
    #         command_func = CommandManager.command_functions[command]
    #         args = requests[1:]
    #         result = command_func(*args)
    #         print(result)
    @staticmethod
    def add(troops_type, timestamps):
        return add_troop(troops_type, timestamps)

    @staticmethod
    def damage(idx, d, timestamps):
        return damage(idx, d, timestamps)

    @staticmethod
    def enemy_status(timestamps):
        return enemy_status(timestamps)

    @staticmethod
    def army_status(timestamps):
        return army_status(timestamps)

    @staticmethod
    def money_status(timestamps):
        return money_status(timestamps)

    @staticmethod
    def command_manager(req_list):
        for request in req_list:
            controller_name = request[0].replace("-", "_")
            args = request[1:]
            controller = getattr(CommandManager, controller_name)
            result = controller(*args)
            print(result)


if __name__ == '__main__':
    get_commands()
