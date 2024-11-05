import sqlite3

def Connect():
    connection = sqlite3.connect('sgpy.db')
    cursor = connection.cursor()
    return connection, cursor

def Create_Table():
    connection, cursor = Connect()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tables (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(50) NOT NULL
                        )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        description VARCHAR(255) NOT NULL,
                        date DATE NOT NULL,
                        ID_tables INTEGER,
                   
                        FOREIGN KEY (ID_tables) REFERENCES tables(ID)
                   )''')
    connection.commit()
    connection.close()

def Insert_Table(name):
    connection, cursor = Connect()
    cursor.execute("INSERT INTO tables (name) VALUES (?)", (name,))
    connection.commit()
    connection.close()

def Insert_Task(description, date, tableId):
    connection, cursor = Connect()
    cursor.execute("INSERT INTO tasks (description, date, ID_tables) VALUES (?, ?, ?)", (description, date, tableId))
    connection.commit()
    connection.close()

def Update_Task(description, id):
    connection, cursor = Connect()
    cursor.execute("UPDATE tasks SET description=? WHERE ID=?", (description, id))
    connection.commit()
    connection.close()

def Delete_Task(id):
    connection, cursor = Connect()
    cursor.execute("DELETE FROM tasks WHERE ID=?", (id,))
    connection.commit()
    connection.close()

def Select_Task():
    connection, cursor = Connect()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"\nID: {task[0]}\nDescrição: {task[1]}\nData: {task[2]}\nID da Tabela: {task[3]}\n")
    connection.close()
    return tasks