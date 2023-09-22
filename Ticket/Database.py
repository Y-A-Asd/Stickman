import sqlite3

def database():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clients
            (
                id      integer not null
                    constraint Clients_pk
                        primary key autoincrement,
                id_code integer not null,
                event   TEXT default None
            );''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events
            (
                id        TEXT
                    primary key autoincrement,
                name      TEXT,
                capacity  INTEGER,
                start     TEXT,
                available BOOLEAN,
                obj       BLOB
            );''')
    conn.commit()
    conn.close()