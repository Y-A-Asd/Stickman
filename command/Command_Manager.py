from core.Actions import Damage, Money_Status, Army_Status, Add_Troops, Enemy_Status
from abc import ABC,abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass


class AddTroopsCommand(Command):
    def execute(self, troops_type, timestamps):
        return Add_Troops.add_troop(troops_type, timestamps)


class DamageCommand(Command):
    def execute(self, idx, d, timestamps):
        return Damage.damage(idx, d, timestamps)


class EnemyStatusCommand(Command):
    def execute(self, timestamps):
        return Enemy_Status.enemy_status(timestamps)


class ArmyStatusCommand(Command):
    def execute(self, timestamps):
        return Army_Status.army_status(timestamps)


class MoneyStatusCommand(Command):
    def execute(self, timestamps):
        return Money_Status.money_status(timestamps)


class CommandManager:
    def __init__(self):
        self.commands = {
            "add": AddTroopsCommand(),
            "damage": DamageCommand(),
            "enemy-status": EnemyStatusCommand(),
            "army-status": ArmyStatusCommand(),
            "money-status": MoneyStatusCommand()
        }

    def command_manager(self, req_list):
        for request in req_list:
            command_name = request[0]
            args = request[1:]

            if command_name in self.commands:
                command = self.commands[command_name]
                result = command.execute(*args)
                print(result)
            else:
                print(f"Unknown command: {command_name}")
