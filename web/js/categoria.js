async function cadastrarCategoria() {
    const cat_name = document.getElementById('cat_name').value;
    const resultado = await eel.cat_create(cat_name)();
    alert(resultado);
}

async function listarCategorias() {
    const resultado = await eel.cat_read_all()();
    alert(resultado);
}

async function buscarCategoria() {
    const cat_name = document.getElementById('cat_name').value;
    const resultado = await eel.cat_search(cat_name)();
    alert(resultado);
}

async function atualizarCategoria() {

    const cat_id = document.getElementById('cat_id').value;
    const cat_name = document.getElementById('cat_name').value;
    const resultado = await eel.cat_update(cat_id, cat_name)();
    alert(resultado);
}

async function deletarCategoria() {
    const cat_id = document.getElementById('cat_id').value;
    const resultado = await eel.cat_delete(cat_id)();
    alert(resultado);
}

