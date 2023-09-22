
from tickets import Tickets
import Events
import Admin
import Database
from colorama import Fore, Back, Style
from getpass import getpass
import maskpass
from os import system as terminal, name as os_name


def clear() -> None:
    terminal("clear" if os_name.lower() == "posix" else "clear")


def client_menu():
    try:
        clear()
        print("=" * 42, client_menu.__name__.center(42), "=" * 42, sep="\n")
        # print(os_name)
        client = input("Enter your personal id: ")
        ticket = Tickets()
        while True:
            options = ["print(ticket.add_ticket_to_client(client,input('event name: ')))",  # DONE
                       "print(ticket.removeTicket(client, input('event name: ')))",  # DONE
                       """print('\\n'.join(map(str, Events.Events.showEvent())))""",  # DONE
                       """print('\\n'.join(map(str, Events.Events.filterEvents(input('date(yyyy,mm,dd): ')))))""",  # DONE
                       "print(ticket.showTicket(client))"  # DONE
                       ]
            num_options = [1, 2, 3, 4, 5]
            try:
                print(Fore.RED,"\n1. REGISTER EVENTS")
                print("2. UNREGISTER EVENTS")
                print("3. SHOW EVENTS")
                print("4. FITER EVENTS",Fore.RESET)
                print("5. SHOW MY EVENTS")
                print("6. LOGOUT")
                option = zip(num_options, options)
                user_choose = int(input("SELECT YOUR CHOICE (1-6): "))
                if 1 <= user_choose < 6:
                    pass
                elif user_choose == 6:
                    break
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
        admin = Admin.Admin(input("Enter your username: "),input("password: "))
        if not admin.status:
            exit("Invalid username or password.")
        else:
            print("Logged in as: ", admin.username)
        while True:
            options = [
                "print(Events.Events(input('event name: '),int(input('event capacity: ')),input('start date(yyyy,mm,dd): ')).addEvent())",  # DONE
                "print(Events.Events.removeEvent(input('event name: ')))",  # DONE
                """print('\\n'.join(map(str, Events.Events.showEvent())))""",  # DONE
                """print('\\n'.join(map(str, Events.Events.filterEvents(input('date(yyyy,mm,dd): ')))))""",  # DONE
                "print(ticket.showTicket(int(input('person id: '))))"  # DONE
                ]
            num_options = [1, 2, 3, 4, 5]
            try:
                print("\n1. ADD EVENTS")
                print("2. REMOVE EVENTS")
                print("3. SHOW EVENTS")
                print("4. FITER EVENTS")
                print("5. SHOW CLIENTS EVENTS")
                print("6. LOGOUT")
                option = zip(num_options, options)
                user_choose = int(input("SELECT YOUR CHOICE (1-6): "))
                if 1 <= user_choose < 6:
                    pass
                elif user_choose == 6:
                    break
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
    Database.database()  # ساخت دیتا بیس
    while True:
        status = input("1. Admin \n2. User \n3. EXIT\nOption:")
        if status == "1":
            admin_menu()
        elif status == "2":
            client_menu()
        elif status == "3":
            exit("BYE Ysf.A.Asd")
        else:
            exit("INVALID INPUT")


menu()
