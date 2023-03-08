async function cadastrarStatus() {
    const sta_name = document.getElementById("sta_name").value;
    const resultado = await eel.sta_create(sta_name)();

    alert(resultado);
}

async function listarStatus() {
    const resultado = await eel.sta_read_all()();

    alert(resultado);
}

async function buscarStatus() {
    const sta_name = document.getElementById("sta_name").value;
    const resultado = await eel.sta_search(sta_id)();

    alert(resultado);
}

async function atualizarStatus() {
    const sta_id = document.getElementById("sta_id").value;
    const sta_name = document.getElementById("sta_name").value;
    const resultado = await eel.sta_update(sta_id, sta_name)();

    alert(resultado);
}

async function deletarStatus() {
    const sta_id = document.getElementById("sta_id").value;
    const resultado = await eel.sta_delete(sta_id)();

    alert(resultado);
}
