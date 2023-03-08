from sistem.ORM.model.models import Categoria
import eel

@eel.expose
def cat_create(cat_nome:str)->str:
    try:
        categoria = Categoria(cat_nome=cat_nome)
        categoria.save()
        return "Categoria criada com sucesso!"
    except Exception as e:
        print(e)
        return "erro ao criar a categoria"

@eel.expose
def cat_read_all():
    try:
        cat = []
        for categoria in Categoria.select():
            print(categoria.cat_nome)
            cat.append(categoria.cat_nome)
        return cat
    except Exception as e:
        print(e)
        return "Erro ao ler as categorias"
    
@eel.expose
def cat_update(cat_id:int, cat_nome:str)->str:
    try:
        categoria = Categoria.get(Categoria.id == cat_id)
        categoria.cat_nome = cat_nome
        categoria.save()
        return "Categoria atualizada com sucesso!"
    except Exception as e:
        print(e)
        return "Erro ao atualizar a categoria"
    
@eel.expose
def cat_delete(cat_id:int)->str:
    try:
        categoria = Categoria.get(Categoria.id == cat_id)
        categoria.delete_instance()
        return "Categoria deletada com sucesso!"
    except Exception as e:
        print(e)
        return "Erro ao deletar a categoria"

@eel.expose
def cat_search(cat_nome:str)->str:
    try:
        categoria = Categoria.select().where(Categoria.cat_nome.contains(cat_nome))
        return categoria
    except Exception as e:
        print(e)
        return "Erro ao pesquisar a categoria"
    
eel.init('web')