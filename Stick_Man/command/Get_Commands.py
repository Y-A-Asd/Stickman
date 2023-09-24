from Stick_Man.core.Enemy import Enemy
from Stick_Man.command.Command_Manager import command_manager


def get_commands():
    q, h = map(int, input().split()) #تو یک خط با فاصله
    Enemy.ORGINALHEALTH = h
    req_list = []
    for _ in range(q):
        request = input().split()
        req_list.append(request)
    command_manager(req_list)