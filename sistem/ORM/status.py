from sistem.ORM.model.models import Status
import eel

@eel.expose
def sta_create(sta_nome:str)->str:
    try:
        status = Status(sta_nome=sta_nome)
        status.save()
        return "Status criado com sucesso!"
    except Exception as e:
        print(e)
        return "erro ao criar o status"

@eel.expose
def sta_read_all():
    try:
        sta = []
        for status in Status.select():
            print(status.sta_nome)
            sta.append(status.sta_nome)
        return sta
    except Exception as e:
        print(e)
        return "Erro ao ler os status"
    
@eel.expose
def sta_update(sta_id:int, sta_nome:str)->str:
    try:
        status = Status.get(Status.id == sta_id)
        status.sta_nome = sta_nome
        status.save()
        return "Status atualizado com sucesso!"
    except Exception as e:
        print(e)
        return "Erro ao atualizar o status"
    
@eel.expose
def sta_delete(sta_id:int)->str:
    try:
        status = Status.get(Status.id == sta_id)
        status.delete_instance()
        return "Status deletado com sucesso!"
    except Exception as e:
        print(e)
        return "Erro ao deletar o status"

@eel.expose
def sta_search(sta_nome:str)->str:
    try:
        status = Status.select().where(Status.sta_nome.contains(sta_nome))
        return status
    except Exception as e:
        print(e)
        return "Erro ao pesquisar o status"
    
    
eel.init('web')

