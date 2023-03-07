from sistem.database.connection import Connection, load_virtual_env
import eel
host, user, password, database = load_virtual_env()
print(host, user, password, database)
# CRUD
class Service:
    def __init__(self):
        self.connection = Connection(host, user, password, database)
    
    @eel.expose
    def create(self, cliente:int, categoria:int, status:int, descricao:str):
        query = """INSERT INTO ATENDIMENTO (cliente, categoria, status, descricao) VALUES ('{}', '{}', '{}', '{}')".format(cliente, categoria, status, descricao)"""
        
        try:
            self.connection.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
    @eel.expose    
    def read_all(self):
        query = 'SELECT * FROM ATENDIMENTO'
        
        try:
            self.connection.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
    @eel.expose   
    def read_one(self, id:int):
        query = 'SELECT * FROM ATENDIMENTO WHERE id = {}'.format(id)
        
        try:
            self.connection.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
    @eel.expose        
    def update(self, id:int, cliente:int, categoria:int, status:int, descricao:str):
        query = """UPDATE ATENDIMENTO SET cliente = '{}', categoria = '{}', status = '{}', descricao = '{}' WHERE id = {}""".format(cliente, categoria, status, descricao, id)
        
        try:
            self.connection.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
    @eel.expose        
    def delete(self, id):
        query = 'DELETE FROM ATENDIMENTO WHERE id = {}'.format(id)
        
        try:
            self.connection.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
    @eel.expose        
    def close(self):
        self.connection.disconnect()
    def __del__(self):
        self.close()

eel.init('web')