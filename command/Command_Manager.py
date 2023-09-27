from core.Actions import Damage, Money_Status, Army_Status, Add_Troops, Enemy_Status
from abc import ABC,abstractmethod


class StateManager(ABC):
    @abstractmethod
    def execute(self, manager, args):
        pass


class AddTroopsState(StateManager):
    def execute(self, manager, args):
        troops_type, timestamps = args
        result = Add_Troops.add_troop(troops_type, timestamps)
        print(result)


class DamageState(StateManager):
    def execute(self, manager, args):
        idx, d, timestamps = args
        result = Damage.damage(idx, d, timestamps)
        print(result)


class EnemyStatusState(StateManager):
    def execute(self, manager, args):
        timestamps = args[0]
        result = Enemy_Status.enemy_status(timestamps)
        print(result)


class ArmyStatusState(StateManager):
    def execute(self, manager, args):
        timestamps = args[0]
        result = Army_Status.army_status(timestamps)
        print(result)


class MoneyStatusState(StateManager):
    def execute(self, manager, args):
        timestamps = args[0]
        result = Money_Status.money_status(timestamps)
        print(result)


class CommandManager:
    def __init__(self):
        self.states = {
            "add": AddTroopsState(),
            "damage": DamageState(),
            "enemy-status": EnemyStatusState(),
            "army-status": ArmyStatusState(),
            "money-status": MoneyStatusState()
        }

    def command_manager(self, req_list):
        for request in req_list:
            command = request[0]
            args = request[1:]

            if command in self.states:
                state = self.states[command]
                state.execute(self, args)
            else:
                print(f"Unknown command: {command}")



