from core.Enemy import Enemy
from command.Command_Manager import CommandManager


def get_commands():
    q, h = map(int, input().split()) #تو یک خط با فاصله
    Enemy.ORGINALHEALTH = h
    req_list = []
    for _ in range(q):
        request = input().split()
        req_list.append(request)
    manager = CommandManager()
    manager.command_manager(req_list)