from sys.database.connection import Connection, load_virtual_env

host, user, password, database = load_virtual_env()
print(host, user, password, database)
# CRUD
class Service:
    def __init__(self):
        self.connection = Connection(host, user, password, database)
        self.cursor = self.connection.connect()    
    
    def create(self, cliente, categoria, status, descricao):
        query = """INSERT INTO ATENDIMENTO (cliente, categoria, status, descricao) VALUES ('{}', '{}', '{}', '{}')".format(cliente, categoria, status, descricao)"""
        
        try:
            self.connection.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
        
    def read_all(self):
        query = 'SELECT * FROM ATENDIMENTO'
        
        try:
            self.connection.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
        
    def read_one(self, id):
        query = 'SELECT * FROM ATENDIMENTO WHERE id = {}'.format(id)
        
        try:
            self.connection.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
            
    def update(self, id, cliente, categoria, status, descricao):
        query = """UPDATE ATENDIMENTO SET cliente = '{}', categoria = '{}', status = '{}', descricao = '{}' WHERE id = {}""".format(cliente, categoria, status, descricao, id)
        
        try:
            self.connection.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
            
    def delete(self, id):
        query = 'DELETE FROM ATENDIMENTO WHERE id = {}'.format(id)
        
        try:
            self.connection.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
            
    def close(self):
        self.connection.disconnect()
    
    def __del__(self):
        self.close()
