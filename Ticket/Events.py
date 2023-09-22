from Date import Date
import sqlite3
from tickets import Tickets
import pickle

class Events:
    def __init__(self, name, capacity, start):
        self.name = name
        self.capacity = capacity
        self.start = Date.date(start.split(","))
        self.available = True if Date.today() < Date.date(start.split(",")) else False
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()
        # cursor.execute('''
        #     CREATE TABLE IF NOT EXISTS Clients
        #         (
        #             id      integer not null
        #                 constraint Clients_pk
        #                     primary key autoincrement,
        #             id_code integer not null,
        #             event   TEXT default None
        #         );
        #
        #     CREATE TABLE IF NOT EXISTS events
        #         (
        #             id        INTEGER
        #                 primary key autoincrement,
        #             name      TEXT,
        #             capacity  INTEGER,
        #             start     TEXT,
        #             available BOOLEAN,
        #             obj       BLOB
        #         );
        #
        #         ''')

    def addEvent(self):
        """
        علت ریختن آبجکت در دیتابیس:
        چون در کلاس تیکت ما نیاز به آبجکت داریم برای اد کردن ایونت ها
        """
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT name FROM events WHERE name   =?''', (self.name,))
        if cursor.fetchone() is None:
            event_pickled = pickle.dumps(self)#زخیره سازی آبجکت در دیتا بیس
            cursor.execute('''INSERT INTO events (name, capacity, start, available,obj)
                        VALUES (?, ?, ?, ?, ?)''', (self.name, self.capacity, self.start, self.available,event_pickled))
            conn.commit()
            return "Event added successfully"
        else:
            raise Exception("Event already exists")


    @staticmethod
    def removeEvent(event_name):
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM events WHERE name = ?', (event_name,))
        if not cursor.fetchall():
            raise Exception("Event not found!")
        cursor.execute('''SELECT * FROM Clients ''')
        clients = cursor.fetchall() #clients[i][2]->events /clients[i][1] ->id_code
        for client in clients:
            t = Tickets()
            t.removeTicket(client[1], event_name)
        cursor.execute('DELETE FROM events WHERE name = ?', (event_name,))
        conn.commit()
        return "Event removed successfully"
    @staticmethod
    def showEvent():
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()
        cursor.execute('SELECT name,capacity,start FROM events')
        events = cursor.fetchall()
        return events

    @staticmethod
    def filterEvents(date):
        date = Date.date(date.split(","))
        today = Date.today()
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()
        if date > today:
            cursor.execute("SELECT name, capacity, start FROM events WHERE DATE(start) BETWEEN DATE(?) AND DATE(?)", (today, date))
            events = cursor.fetchall()
        elif date < today:
            cursor.execute("SELECT name, capacity, start FROM events WHERE DATE(start) < DATE(?) AND DATE(start) >= DATE(?)",(today, date))
            events = cursor.fetchall()
        else:
            cursor.execute("SELECT name, capacity, start FROM events WHERE DATE(start) = DATE(?)", (today,))
            events = cursor.fetchall()
        return events



# Events.removeEvent()
"""--init__"""#TODO:DONE
# e = Events("Event 1",100,"2020,01,01").addEvent()
# e1 = Events("Event 2",200,"2024,05,01").addEvent()
"""addEvent()"""#TODO:DONE
# e3 = Events("Event 3",100,"2025,05,01").addEvent()
"""removeEvent()"""#TODO:DONE
# Events.emoveEvent("Event 3")
"""showEvent()"""#TODO:DONE
# print('\n'.join(map(str, Events.showEvent())))
"""filterEvents()"""#TODO:DONE
# print('\n'.join(map(str, Events.filterEvents("2020,01,02"))))

