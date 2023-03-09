async function cadastrarSistema() {
    const sis_name = document.getElementById("sis_name").value;
    const resultado = await eel.sis_create(sis_name)();

    return resultado;
}

async function listarSistemas() {
    const resultado = await eel.sis_read_all()();
    return resultado;
}

async function buscarSistema() {
    const sis_name = document.getElementById("sis_name").value;
    const resultado = await eel.sis_search(sis_id)();

    return resultado;
}

async function atualizarSistema() {
    const sis_id = document.getElementById("sis_id").value;
    const sis_name = document.getElementById("sis_name").value;
    const resultado = await eel.sis_update(sis_id, sis_name)();

    return resultado;
}

async function deletarSistema() {
    const sis_id = document.getElementById("sis_id").value;
    const resultado = await eel.sis_delete(sis_id)();

    return resultado;
}

function read_list() {
    var x = listarSistemas().then(function (result) {
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

read_list()


