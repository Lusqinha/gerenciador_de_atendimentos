async function cadastrarCategoria() {
    const cat_name = document.getElementById('cat_name').value;
    const resultado = await eel.cat_create(cat_name)();
    return resultado;
}

async function listarCategorias() {
    const resultado = await eel.cat_read_all()();
    return resultado;
}

async function buscarCategoria() {
    const cat_name = document.getElementById('cat_name').value;
    const resultado = await eel.cat_search(cat_name)();
    return resultado;
}

async function atualizarCategoria() {

    const cat_id = document.getElementById('cat_id').value;
    const cat_name = document.getElementById('cat_name').value;
    const resultado = await eel.cat_update(cat_id, cat_name)();
    return resultado;
}

async function deletarCategoria() {
    const cat_id = document.getElementById('cat_id').value;
    const resultado = await eel.cat_delete(cat_id)();
    return resultado;
}


function read_list_categoria() {
    var x = listarCategorias().then(function (result) {
        var table = document.getElementById("myTable").getElementsByTagName('tbody')[0];
        table.innerHTML = "";
        var content = []
        for (var i = 0; i < result.length; i++) {
            content.push(result[i])
            console.log(result[i])

            var row = table.insertRow(i);
            var indexCell = row.insertCell(0);
            var valueCell = row.insertCell(1);
            indexCell.innerHTML = i + 1;
            valueCell.innerHTML = result[i];
        }
        return content;
    });
    return x;
}

read_list_categoria()