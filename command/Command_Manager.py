from core.Actions import Damage, Money_Status, Army_Status, Add_Troops, Enemy_Status


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
        return Add_Troops.add_troop(troops_type, timestamps)

    @staticmethod
    def damage(idx, d, timestamps):
        return Damage.damage(idx, d, timestamps)

    @staticmethod
    def enemy_status(timestamps):
        return Enemy_Status.enemy_status(timestamps)

    @staticmethod
    def army_status(timestamps):
        return Army_Status.army_status(timestamps)

    @staticmethod
    def money_status(timestamps):
        return Money_Status.money_status(timestamps)

    @staticmethod
    def command_manager(req_list):
        for request in req_list:
            controller_name = request[0].replace("-", "_")
            args = request[1:]
            controller = getattr(CommandManager, controller_name)
            result = controller(*args)
            print(result)
