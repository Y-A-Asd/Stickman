from tickets import Tickets
import Events
import Admin


def client_menu():
    try:
        client = int(input("Enter your personal id: "))
        ticket = Tickets()
        while True:
            #TODO:
            # print(ticket.add_ticket_to_client(client,input('event name: ')))
            # print('\n'.join(map(str, event.showEvent())))
            options = ["print(ticket.add_ticket_to_client(client,input('event name: ')))",#DONE
                       "print(ticket.removeTicket(client, input('event name: ')))",#DONE
                       """print('\\n'.join(map(str, Events.Events.showEvent())))""",#DONE
                       """print('\\n'.join(map(str, Events.Events.filterEvents(input('date(yyyy,mm,dd): ')))))""",#DONE
                       "print(ticket.showTicket(client))",#DONE
                       "break",#DONE
                       ]
            num_options = [1, 2, 3, 4, 5, 6]
            try:
                print("\n1. REGISTER EVENTS")
                print("2. UNREGISTER EVENTS")
                print("3. SHOW EVENTS")
                print("4. FITER EVENTS")
                print("5. SHOW MY EVENTS")
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
    except Exception as error:
        print(error)
def admin_menu():
    try:
        ticket = Tickets()
        admin = Admin.Admin(input("Enter your username: "),input("Enter your password: "))
        if not admin.status:
            exit("Invalid username or password.")
        else:
            print("Logged in as: ",admin.username)
        while True:
            #TODO:
            # print(ticket.add_ticket_to_client(client,input('event name: ')))
            # print('\n'.join(map(str, event.showEvent())))
            options = ["print(Events.Events(input('event name: '),int(input('event capacity: ')),input('start date(yyyy,mm,dd): ')).addEvent())",#DONE
                       "print(Events.Events.removeEvent(input('event name: ')))",#DONE
                       """print('\\n'.join(map(str, Events.Events.showEvent())))""",#DONE
                       """print('\\n'.join(map(str, Events.Events.filterEvents(input('date(yyyy,mm,dd): ')))))""",#DONE
                       "print(ticket.showTicket(int(input('person id: '))))",#DONE
                       "break",#DONE
                       ]
            num_options = [1, 2, 3, 4, 5, 6]
            try:
                print("\n1. ADD EVENTS")
                print("2. REMOVE EVENTS")
                print("3. SHOW EVENTS")
                print("4. FITER EVENTS")
                print("5. SHOW CLIENTS EVENTS")
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
    except Exception as error:
        print(error)

def menu():
    while True:
        status = int(input("1. Admin \n2.User \n3.EXIT\noption:"))
        if status == 1:
            admin_menu()
        elif status == 2:
            client_menu()
        elif status == 3:
            break
        else:print("INVALID INPUT")

menu()