async function cadastrarStatus() {
    const sta_name = document.getElementById("sta_name").value;
    const resultado = await eel.sta_create(sta_name)();

    return resultado;
}

async function listarStatus() {
    const resultado = await eel.sta_read_all()();

    return resultado;
}

async function buscarStatus() {
    const sta_name = document.getElementById("sta_name").value;
    const resultado = await eel.sta_search(sta_id)();

    return resultado;
}

async function atualizarStatus() {
    const sta_id = document.getElementById("sta_id").value;
    const sta_name = document.getElementById("sta_name").value;
    const resultado = await eel.sta_update(sta_id, sta_name)();

    return resultado;
}

async function deletarStatus() {
    const sta_id = document.getElementById("sta_id").value;
    const resultado = await eel.sta_delete(sta_id)();

    return resultado;
}


function read_list_status() {
    var x = listarStatus().then(function (result) {
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

read_list_status()