from datetime import date
from peewee import MySQLDatabase, SqliteDatabase, Model, CharField, DateField, ForeignKeyField
from dotenv import load_dotenv
from os import getenv

load_dotenv()
host = getenv('DB_HOST')
user = getenv('DB_USER')
password = getenv('DB_PASSWORD')
database = getenv('DB_DATABASE')

def set_db():
    # db = MySQLDatabase(database, user=user, password=password, host=host, port=3306, autorollback=True, autoconnect=True)
    
    
    return db

db = SqliteDatabase('sistem.db')

class Sistema(Model):
    sis_nome = CharField(max_length=50)

    class Meta:
        database = db
        
class Categoria(Model):
    cat_nome = CharField(max_length=50)

    class Meta:
        database = db

class Status(Model):
    sta_nome = CharField(max_length=50)

    class Meta:
        database = db

class Cliente(Model):
    cli_nome = CharField(max_length=50)
    cli_celular = CharField(max_length=20)
    cli_email = CharField(max_length=100)
    cli_acesso = CharField(max_length=20)
    cli_sistema = ForeignKeyField(Sistema, backref='clientes')

    class Meta:
        database = db

class Atendimento(Model):
    ate_data_criacao = DateField(default=date.today)
    ate_descricao = CharField(max_length=256)
    ate_categoria = ForeignKeyField(Categoria, backref='atendimentos')
    ate_cliente = ForeignKeyField(Cliente, backref='atendimentos')
    ate_status = ForeignKeyField(Status, backref='atendimentos')

    class Meta:
        database = db

with db:
    db.create_tables([Sistema, Cliente, Categoria, Status, Atendimento])
