from sistem.database.connection import Connection, load_virtual_env
import eel
host, user, password, database = load_virtual_env()
print(host, user, password, database)
# CRUD
class Service:
    def __init__(self):
        self.conn = Connection(host, user, password, database)
    
    @eel.expose
    def sql_create(self, cliente:int, categoria:int, status:int, descricao:str):
        query = """INSERT INTO ATENDIMENTO (cliente, categoria, status, descricao) VALUES ('{}', '{}', '{}', '{}')".format(cliente, categoria, status, descricao)"""
        
        try:
            self.conn.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
    @eel.expose    
    def sql_read_all(self):
        query = 'SELECT * FROM ATENDIMENTO'
        print(query)
        try:
            content = self.conn.execute(query)
            print(content)
            print('Query executed')
            return content
        except Exception as e:
            print('Query not executed', e)
    @eel.expose   
    def sql_read_one(self, id:int):
        query = 'SELECT * FROM ATENDIMENTO WHERE id = {}'.format(id)
        
        try:
            self.conn.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
    @eel.expose        
    def sql_update(self, id:int, cliente:int, categoria:int, status:int, descricao:str):
        query = """UPDATE ATENDIMENTO SET cliente = '{}', categoria = '{}', status = '{}', descricao = '{}' WHERE id = {}""".format(cliente, categoria, status, descricao, id)
        
        try:
            self.conn.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
    @eel.expose        
    def sql_delete(self, id):
        query = 'DELETE FROM ATENDIMENTO WHERE id = {}'.format(id)
        
        try:
            self.conn.execute(query)
            print('Query executed')
        except Exception as e:
            print('Query not executed', e)
    @eel.expose        
    def sql_close(self):
        self.conn.disconnect()
    def __del__(self):
        self.sql_close()

eel.init('web')