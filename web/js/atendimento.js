async function cadastrarAtendimento() {
    const ate_data = document.getElementById("ate_data").value;
    const ate_cliente = document.getElementById("ate_cliente").value;
    const ate_descricao = document.getElementById("ate_descricao").value;
    const ate_categoria = document.getElementById("ate_categoria").value;
    const ate_status = document.getElementById("ate_status").value;

    if (ate_data == "") {
        const resultado = await eel.ate_create(ate_descricao, ate_categoria, ate_cliente, ate_status)();
    }

    const resultado = await eel.ate_create(ate_data, ate_hora, ate_cliente, ate_descricao)();

    alert(resultado);
}

async function listarAtendimentos() {
    const resultado = await eel.ate_read_all()();
    console.log(resultado);
}

async function atualizarAtendimento() {
    const ate_id = document.getElementById("ate_id").value;
    const ate_data = document.getElementById("ate_data").value;
    const ate_cliente = document.getElementById("ate_cliente").value;
    const ate_descricao = document.getElementById("ate_descricao").value;
    const ate_categoria = document.getElementById("ate_categoria").value;
    const ate_status = document.getElementById("ate_status").value;

    const resultado = await eel.ate_update(ate_id, ate_data, ate_cliente, ate_descricao, ate_categoria, ate_status)();

    alert(resultado);
}

async function deletarAtendimento() {
    const ate_id = document.getElementById("ate_id").value;

    const resultado = await eel.ate_delete(ate_id)();

    alert(resultado);
}

async function buscarAtendimento() {
    const ate_id = document.getElementById("ate_id").value;

    const resultado = await eel.ate_read(ate_id)();

    alert(resultado);
}
