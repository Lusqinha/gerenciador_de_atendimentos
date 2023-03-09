from sistem.ORM.model.models import Atendimento, set_db
import eel

@eel.expose
def ate_create(ate_descricao:str, ate_categoria:int, ate_cliente:int, ate_status:int, ate_data_criacao:str|None = None)->str:
    db = set_db()
    with db.connection():
        try:
            atendimento = Atendimento(ate_data_criacao=ate_data_criacao, ate_descricao=ate_descricao, ate_categoria=ate_categoria, ate_cliente=ate_cliente, ate_status=ate_status)
            atendimento.save()
            return "Atendimento criado com sucesso!"
        except Exception as e:
            print(e)
            return "erro ao criar o atendimento"
    
@eel.expose
def ate_read_all():
    db = set_db()
    with db.connection():
        try:
            ate = []
            for atendimento in Atendimento.select():
                print(atendimento.ate_descricao)
                ate.append(atendimento.ate_descricao)
            return ate
        except Exception as e:
            print(e)
            return "Erro ao ler os atendimentos"
    
@eel.expose
def ate_update(ate_id:int, ate_descricao:str, ate_categoria:int, ate_cliente:int, ate_status:int, ate_data_criacao:str|None = None)->str:
    db = set_db()
    with db.connection():
        try:
            atendimento = Atendimento.get(Atendimento.id == ate_id)
            atendimento.ate_data_criacao = ate_data_criacao
            atendimento.ate_descricao = ate_descricao
            atendimento.ate_categoria = ate_categoria
            atendimento.ate_cliente = ate_cliente
            atendimento.ate_status = ate_status
            atendimento.save()
            return "Atendimento atualizado com sucesso!"
        except Exception as e:
            print(e)
            return "Erro ao atualizar o atendimento"
    
@eel.expose
def ate_delete(ate_id:int)->str:
    db = set_db()
    with db.connection():
        try:
            atendimento = Atendimento.get(Atendimento.id == ate_id)
            atendimento.delete_instance()
            return "Atendimento deletado com sucesso!"
        except Exception as e:
            print(e)
            return "Erro ao deletar o atendimento"

@eel.expose
def ate_search(ate_descricao:str)->str:
    db = set_db()
    with db.connection():
        try:
            atendimento = Atendimento.select().where(Atendimento.ate_descricao.contains(ate_descricao))
            return atendimento
        except Exception as e:
            print(e)
            return "Erro ao pesquisar o atendimento"
        
eel.init('web')