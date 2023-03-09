from sistem.ORM.model.models import Cliente, set_db
import eel

@eel.expose
def cli_create(cli_nome:str, cli_celular:str, cli_email:str, cli_acesso:str, cli_sistema:int)->str:
    db = set_db()
    with db.connection():
        try:
            cliente = Cliente(cli_nome=cli_nome, cli_celular=cli_celular, cli_email=cli_email, cli_acesso=cli_acesso, cli_sistema=cli_sistema)
            cliente.save()
            return "Cliente criado com sucesso!"
        except Exception as e:
            print(e)
            return "erro ao criar o cliente"

@eel.expose
def cli_read_all():
    db = set_db()
    with db.connection():
        try:
            cli = []
            for cliente in Cliente.select():
                print(cliente.cli_nome)
                cli.append(cliente.cli_nome)
            return cli
        except Exception as e:
            print(e)
            return "Erro ao ler os clientes"
    
@eel.expose
def cli_update(cli_id:int, cli_nome:str, cli_celular:str, cli_email:str, cli_acesso:str, cli_sistema:int)->str:
    db = set_db()
    with db.connection():
        try:
            cliente = Cliente.get(Cliente.id == cli_id)
            cliente.cli_nome = cli_nome
            cliente.cli_celular = cli_celular
            cliente.cli_email = cli_email
            cliente.cli_acesso = cli_acesso
            cliente.cli_sistema = cli_sistema
            cliente.save()
            return "Cliente atualizado com sucesso!"
        except Exception as e:
            print(e)
            return "Erro ao atualizar o cliente"

@eel.expose
def cli_delete(cli_id:int)->str:
    db = set_db()
    with db.connection():
        try:
            cliente = Cliente.get(Cliente.id == cli_id)
            cliente.delete_instance()
            return "Cliente deletado com sucesso!"
        except Exception as e:
            print(e)
            return "Erro ao deletar o cliente"
        
@eel.expose
def cli_search(cli_nome:str)->str:
    db = set_db()
    with db.connection():
        try:
            cliente = Cliente.select().where(Cliente.cli_nome.contains(cli_nome))
            return cliente
        except Exception as e:
            print(e)
            return "Erro ao pesquisar o cliente"
    
eel.init('web')