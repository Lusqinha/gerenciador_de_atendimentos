async function cadastrarSistema() {
    const sis_name = document.getElementById("sis_name").value;
    const resultado = await eel.sis_create(sis_name)();

    alert(resultado);
}

async function listarSistemas() {
    const resultado = await eel.sis_read_all()();

    alert(resultado);
}

async function buscarSistema() {
    const sis_name = document.getElementById("sis_name").value;
    const resultado = await eel.sis_search(sis_id)();

    alert(resultado);
}

async function atualizarSistema() {
    const sis_id = document.getElementById("sis_id").value;
    const sis_name = document.getElementById("sis_name").value;
    const resultado = await eel.sis_update(sis_id, sis_name)();

    alert(resultado);
}

async function deletarSistema() {
    const sis_id = document.getElementById("sis_id").value;
    const resultado = await eel.sis_delete(sis_id)();

    alert(resultado);
}
