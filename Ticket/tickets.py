from Clients import Clients
import sqlite3
import pickle

class Tickets:
    """مدیریت اتصال رویداد با کاربران"""
    def __init__(self):
        """
        self.client: Clients
        self.event: Events
        این دو ویژگی کلاس آبجکتی از دو کلاس دیگر هستند
        """

    def add_ticket_to_client(self,client,event_name):
        """
        ست کردن دیتابیس بر اساس کلاینت و ایونت ورودی و اد کردن ایونت به ایونت های مربوط به کاربر
        """
        try:

            conn = sqlite3.connect('tickets.db')
            cursor = conn.cursor()
            cursor.execute('SELECT id FROM events WHERE name = ?', (event_name,))
            if not cursor.fetchall():
                raise Exception("Event not found!")
            self.client = Clients(client)
            self.event = Tickets.get_obj_from_event(event_name)

            if not self.event.available:
                return "Event is not available."

            #به علت قفل شدن دیتابیس به دلیل نامعلوم
            with sqlite3.connect('tickets.db') as conn:
                cursor = conn.cursor()
                if self.event.capacity <= 0:
                    raise Exception("Event is already at full capacity.")
                cursor.execute("UPDATE events SET capacity = capacity - 1 WHERE name = ?", (self.event.name,))
                cursor.execute("SELECT event FROM Clients WHERE id_code = ?", (self.client.id_code,))
                current_event_value = cursor.fetchone()#چون میخواستم ایونت جدید رو به ایونت های قبلی که ثبتنام کرده اضافه کنم
                if current_event_value[0]:
                    events_list = current_event_value[0].split(',')
                    if self.event.name in events_list:
                        return f"{self.event.name} has already been added to the client."
                    else:
                        events_list.append(self.event.name)
                        updated_event_value = ','.join(events_list)
                else:
                    updated_event_value = self.event.name
                cursor.execute("UPDATE Clients SET event = ? WHERE id_code = ?",
                               (updated_event_value, self.client.id_code))
                conn.commit()
            return f"{self.event.name} has been added to the client."
        except Exception as e:
            return str(e)

    @staticmethod
    def get_obj_from_event(event_name):
        # try:
        conn = sqlite3.connect('tickets.db')
        cursor = conn.cursor()
        cursor.execute("SELECT obj FROM events WHERE name =?", (event_name,))
        tickets = cursor.fetchone()
        if tickets[0]:
            return pickle.loads(tickets[0])
        else:
            return "There is no such event."

        # except Exception as e:
        #     return str(e)

    def showTicket(self,client):
        """
        نمایش تیکت های فرد
        """
        try:
            self.client = Clients(client)
            conn = sqlite3.connect('tickets.db')
            cursor = conn.cursor()
            cursor.execute("SELECT event FROM Clients WHERE id_code = ?", (self.client.id_code,))
            tickets = cursor.fetchone()
            conn.close()

            if tickets:
                return f"{self.client.id_code} : {tickets[0]}"
            else:
                return f"No tickets found for the client."

        except Exception as e:
            return str(e)

    def removeTicket(self,client,event_name):
        """
        حذف کردن تیکت برای فرد
        """
        try:
            self.client = Clients(client)
            self.event = Tickets.get_obj_from_event(event_name)
            conn = sqlite3.connect('tickets.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM Clients WHERE id_code = ?",
                           (self.client.id_code,))
            ticket_id = cursor.fetchone()
            if ticket_id:
                cursor.execute("SELECT event FROM Clients WHERE id_code =?", (self.client.id_code,))
                tickets = cursor.fetchone()
                if tickets:
                    current_event_value = tickets[0].split(",")#['Event 2', 'Event 3']
                    if self.event.name in current_event_value:
                        current_event_value.remove(self.event.name)
                        current_event_value = ','.join(current_event_value)
                    else:
                        return f"{self.event.name} is not added to the client."
                    cursor.execute("UPDATE events SET capacity = capacity + 1 WHERE name = ?", (self.event.name,))
                    cursor.execute("UPDATE  Clients SET event = ? WHERE id_code = ?", (current_event_value,self.client.id_code))
                status = input(f"Do you {self.client.id_code} want to remove this ticket? (y/n): ")
                #TODO:اگر از طریق ادمین ران شد دیگر ولیدیشن نمیخواد
                if status.lower() == "y":
                    conn.commit()
                    conn.close()
                else:
                    return f"Process has been cancelled."
                return f"Ticket for {self.event.name} has been removed."

            else:
                raise Exception("Client not found.")

        except Exception as e:
            return str(e)

    @staticmethod
    def confirm():
        """
        تایید تغییرات
        """
        try:
            conn = sqlite3.connect('tickets.db')
            conn.commit()
            conn.close()
            return "Database changes have been confirmed."

        except Exception as e:
            return str(e)


"""addTicketToClient()""""#TODO:DONE"

# t = Tickets()
# print(t.add_ticket_to_client(1,"Event 3"))
"""removeTicket()""""#TODO:DONE"

# t = Tickets()
# print(t.removeTicket(1,"Event 3"))

"""showTicket()""""#TODO:DONE"
# t = Tickets()
# print(t.showTicket(1))

"""confirm()""""#TODO:DONE"

# print(Tickets.confirm())