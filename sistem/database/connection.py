import mysql.connector
from dotenv import load_dotenv
from os import getenv
from typing import Tuple, Any

# This function loads the environment variables from the .env file, will return in following order: host, user, password, database
def load_virtual_env() -> Tuple[str|None, str|None, str|None, str|None]:
    load_dotenv()
    host = getenv('DB_HOST')
    user = getenv('DB_USER')
    password = getenv('DB_PASSWORD')
    database = getenv('DB_DATABASE')
    
    return host, user, password, database


class Connection:
    def __init__(self, host:str|None, user:str|None, password:str|None, database:str|None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    def connect(self) -> Any:
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
            print('Connection failed ! >Error in connect func< - ', e)
            return None
    
    def disconnect(self) -> None:
        try:
            self.connection.close()
            print('Connection closed')
        except Exception as e:
            print('Connection not closed! >Error in disconnect func< - ', e)
            
    def execute(self, query:str):
        try:
            self.cursor.execute(f"USE {self.database}; {query}", multi=True)
            self.connection.commit()
            print('Query executed')
        except Exception as e:
            print('Query not executed ! >Error in execute func< - ', e)
            
# Path: sys\database\database.py

if __name__ == "__main__":
    
    host, user, password, database = load_virtual_env()
    
    print(host, user, password, database)
    
    
    db = Connection(host, user, password, database)
    db.connect()
    db.execute(f"use {database};  SELECT * FROM STATUS;")