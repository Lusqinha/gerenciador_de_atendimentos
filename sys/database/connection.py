import mysql.connector

class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print('Connection successful')
            return self.cursor
        except Exception as e:
            print('Connection failed', e)
            return None
    
    def disconnect(self):
        try:
            self.connection.close()
            print('Connection closed')
        except Exception as e:
            print('Connection not closed', e)
            
    def execute(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
            
# Path: sys\database\database.py
