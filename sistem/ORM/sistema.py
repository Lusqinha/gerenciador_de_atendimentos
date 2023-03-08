from sistem.ORM.model.models import Sistema
import eel

@eel.expose
def sis_create(sis_nome:str)->str:
    try:
        sistema = Sistema(sis_nome=sis_nome)
        sistema.save()
        return "Sistema criado com sucesso!"
    except Exception as e:
        print(e)
        return "erro ao criar o sistema"

@eel.expose    
def sis_read_all():
    try:
        sis = []
        for sistema in Sistema.select():
            print(sistema.sis_nome)
            sis.append(sistema.sis_nome)
        return sis
    except Exception as e:
        print(e)
        return "Erro ao ler os sistemas"
    

@eel.expose   
def sis_update(sis_id:int, sis_nome:str)->str:
    try:
        sistema = Sistema.get(Sistema.id == sis_id)
        sistema.sis_nome = sis_nome
        sistema.save()
        return "Sistema atualizado com sucesso!"
    except Exception as e:
        print(e)
        return "Erro ao atualizar o sistema"
 
@eel.expose    
def sis_delete(sis_id:int)->str:
    try:
        sistema = Sistema.get(Sistema.id == sis_id)
        sistema.delete_instance()
        return "Sistema deletado com sucesso!"
    except Exception as e:
        print(e)
        return "Erro ao deletar o sistema"

@eel.expose    
def sis_search(sis_nome:str)->str:
    try:
        sistema = Sistema.select().where(Sistema.sis_nome.contains(sis_nome))
        return sistema
    except Exception as e:
        print(e)
        return "Erro ao pesquisar o sistema"
    
eel.init('web')