import mysql.connector

from dotenv import load_dotenv
from os import getenv


# This function loads the environment variables from the .env file, will return in following order: host, user, password, database
def load_virtual_env():

    load_dotenv()

    host = getenv('DB_HOST')
    user = getenv('DB_USER')
    password = getenv('DB_PASSWORD')
    database = getenv('DB_DATABASE')
    
    return host, user, password, database


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
            self.cursor.execute("".join(query), multi=True)
            self.connection.commit()
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
            
# Path: sys\database\database.py

if __name__ == "__main__":
    
    host, user, password, database = load_virtual_env()
    
    print(host, user, password, database)
    
    
    db = Connection(host, user, password, database)
    db.connect()
    db.execute(f"use {database};  SELECT * FROM STATUS;")