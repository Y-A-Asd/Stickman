def main():

    q, h = map(int, input().split()) #تو یک خط با فاصله
    enemy.health = h
    for _ in range(q):
        request = input().split()
        command = request[0]
        if command == "add":
            role, timestamp = request[1], request[2]
            result = Action.add_troop(role)
        elif command == "damage":
            idx, d, timestamp = int(request[1]), int(request[2]), request[3]
            result = Action.damage(idx, d)
        elif command == "enemy-status":
            timestamp = request[1]
            result = enemy.health
        elif command == "army-status":
            timestamp = request[1]
            result = Action.rmy_status()
        elif command == "money-status":
            timestamp = request[1]
            result = player.balance

        print(result)